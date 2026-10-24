#!/usr/bin/env python3
"""Rewrite the skills block of README.md from the skills.caffeinity.com manifest.

    python .github/scripts/skills_section.py            # rewrite README.md in place
    python .github/scripts/skills_section.py --check    # exit 1 if README.md is stale
    python .github/scripts/skills_section.py --manifest path/to/skills.json

Only the text between <!-- skills:start --> and <!-- skills:end --> changes. The manifest is the
same file the site is built from, so the profile lists exactly what the site publishes.
"""
import argparse
import json
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path

MANIFEST_URL = "https://raw.githubusercontent.com/arm-pz/skills-site/main/site/skills.json"
SITE = "https://skills.caffeinity.com"
START, END = "<!-- skills:start -->", "<!-- skills:end -->"
README = Path(__file__).resolve().parents[2] / "README.md"


def first_sentence(text):
    """The blurb's first sentence, or its first two when the first is a fragment like 'Start here.'"""
    text = " ".join(text.split())
    parts = re.findall(r".+?[.!?](?=\s|$)", text) or [text]
    lead = parts[0] if len(parts[0]) >= 40 or len(parts) == 1 else f"{parts[0]} {parts[1].strip()}"
    return lead.strip().replace("|", "\\|")


def count(skills):
    mods = sum(1 for s in skills if s.get("kind") == "mod")
    n = len(skills) - mods
    text = f"{n} skill" + ("" if n == 1 else "s")
    return text + (f" and {mods} mod" + ("" if mods == 1 else "s") if mods else "")


def render(manifest):
    order = {g["id"]: g["order"] for g in manifest["groups"]}
    skills = sorted((s for s in manifest["skills"] if s.get("page") != "none"),
                    key=lambda s: (order[s["group"]], s["order"]))
    groups = [g for g in sorted(manifest["groups"], key=lambda g: g["order"])
              if any(s["group"] == g["id"] for s in skills)]
    out = [START,
           f"_{count(skills)} in {len(groups)} groups. This block is generated from the "
           f"[skills site]({SITE}) manifest; edit the manifest, not this README._", ""]
    for g in groups:
        out += [f"### {g['title']}", "", "| Skill | What it does |", "|---|---|"]
        for s in (s for s in skills if s["group"] == g["id"]):
            label = f"[{s['name']}]({SITE}/{s['name']}/)"
            source = f"[source](https://github.com/{s['repo']})" if s.get("repo") else ""
            kind = " · Claude Code mod" if s.get("kind") == "mod" else ""
            out.append(f"| {label}{kind} | {first_sentence(s['blurb'])} {source} |".replace("  ", " "))
        out.append("")
    flows = manifest.get("workflows", [])
    if flows:
        out += ["### Workflows", "",
                "Skills hand work to each other. Start with "
                f"[caffeinity-routing]({SITE}/caffeinity-routing/) if you are not sure which you need.", ""]
        for f in flows:
            steps = " → ".join(" or ".join(step["skills"]) + (" (optional)" if step.get("optional") else "")
                               for step in f["steps"])
            out.append(f"- **{f['id']} {f['title']}:** {steps}")
        out.append("")
    out.append(END)
    return "\n".join(out)


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--manifest", help="read a local manifest instead of the published one")
    a = ap.parse_args(argv)
    if a.manifest:
        manifest = json.loads(Path(a.manifest).read_text(encoding="utf-8"))
    else:
        try:
            with urllib.request.urlopen(MANIFEST_URL, timeout=30) as r:
                manifest = json.load(r)
        except urllib.error.HTTPError as err:
            if err.code != 404:
                raise
            print(f"{MANIFEST_URL} is not published yet; README.md left as it is")
            return 0
    text = README.read_text(encoding="utf-8")
    if START not in text or END not in text:
        raise SystemExit(f"README.md needs {START} and {END} markers")
    new = re.sub(re.escape(START) + r".*?" + re.escape(END), lambda _: render(manifest), text, flags=re.S)
    if a.check:
        print("README.md is current" if new == text else "README.md is stale")
        return 0 if new == text else 1
    if new != text:
        README.write_text(new, encoding="utf-8")
        print("README.md updated")
    else:
        print("README.md already current")
    return 0


if __name__ == "__main__":
    sys.exit(main())
