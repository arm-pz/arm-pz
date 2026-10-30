# Abdul Rahman P Z

**Senior backend developer: .NET, AWS and custom MCP servers.**
About 10 years of experience. Based in Coimbatore. [Available immediately / open to roles in ...]

[Email](mailto:info@caffeinity.com) · [LinkedIn:](https://www.linkedin.com/in/itsarm/) · [Skills site](https://skills.caffeinity.com)

---

## Backend and cloud work

I build cloud-native services on .NET and AWS, and custom MCP servers that connect AI agents to real systems.


---

## Open-source agent skills

On the side I write plain-markdown skills that teach AI coding agents (Claude Code, Cursor, Codex) one craft each. They are free, need no API keys and have nothing to run. Every skill states what it will not do, and none applies changes without your approval.

<!-- skills:start -->
_45 skills and 7 mods in 9 groups. This block is generated from the [skills site](https://skills.caffeinity.com) manifest; edit the manifest, not this README._

### Start Here

| Skill | What it does |
|---|---|
| [caffeinity-routing](https://skills.caffeinity.com/caffeinity-routing/) | Start here. Tell it the outcome you want and it picks one of eleven brews (workflows), lists the skills in order with what each hands the next, and names the ones you have not installed instead of improvising their work. [source](https://github.com/arm-pz/caffeinity-skills) |

### Skill Authoring

| Skill | What it does |
|---|---|
| [draft-skill](https://skills.caffeinity.com/draft-skill/) | Creates a new agent skill from a plain idea: confirms the purpose before writing anything, checks the installed siblings for overlap, splits scripts from references from assets, writes a description that actually triggers, then validates it with check_skill.py. [source](https://github.com/arm-pz/draft-skill) |
| [prompts-to-skill](https://skills.caffeinity.com/prompts-to-skill/) | Turns a list of your own prompts into a finished, tested skill, one skill per prompt: an intent interview, an overlap check against what is already installed, a draft written with draft-skill, trigger test cases that include near-misses, and a tune-skill gate at the end. [source](https://github.com/arm-pz/prompts-to-skill) |
| [tune-skill](https://skills.caffeinity.com/tune-skill/) | Audits and fine-tunes a skill that already exists: the description that never fires, overlap with installed siblings, stale names and counts, handoff contracts that do not hand off. [source](https://github.com/arm-pz/tune-skill) |
| [prompts-to-skill-release](https://skills.caffeinity.com/prompts-to-skill-release/) | Packages a finished skill for release: runs its trigger test cases and records which passed and which did not, sets the version and CHANGELOG, builds the archive, writes the README, and ends with a per-platform install checklist. [source](https://github.com/arm-pz/prompts-to-skill-release) |
| [skill-to-mod](https://skills.caffeinity.com/skill-to-mod/) | Checks whether a skill should become a Claude Code mod, then builds the plugin with your skill unchanged and a thin trigger, validates and tests it, and lists what it can touch. [source](https://github.com/arm-pz/skill-to-mod) |
| [skill-launch](https://skills.caffeinity.com/skill-launch/) | The full pipeline from idea to launched skill: Draft-Skill writes it, Tune-Skill gates it through the validator, Findable-Polish polishes its discovery surfaces. [source](https://github.com/arm-pz/skill-launch) |
| [tune-and-polish](https://skills.caffeinity.com/tune-and-polish/) | For a skill that both misfires and hides: Tune-Skill fixes the triggering description, sibling overlaps and stale counts, gated on check_skill.py with zero FAILs; then Findable-Polish audits and polishes the README, About and site copy against real queries. [source](https://github.com/arm-pz/tune-and-polish) |
| [tune-skill-mod](https://skills.caffeinity.com/tune-skill-mod/) · Claude Code mod | Arms when Claude edits a SKILL.md, then holds git push, PRs and releases until tune-skill has validated the change. [source](https://github.com/arm-pz/caffeinity-skills) |
| [skill-release-mod](https://skills.caffeinity.com/skill-release-mod/) · Claude Code mod | Holds gh release create and npm publish in Claude Code until prompts-to-skill-release has run the skill's test cases since your last edit. [source](https://github.com/arm-pz/caffeinity-skills) |

### Publish & Discover

| Skill | What it does |
|---|---|
| [findable](https://skills.caffeinity.com/findable/) | Sets up discovery for a GitHub repo, skill, plugin or MCP server so it gets found by what it does, not only by its name. [source](https://github.com/arm-pz/findable) |
| [publish-pipeline](https://skills.caffeinity.com/publish-pipeline/) | Turns a pile of skill repos into a published site: a committed manifest decides what is public, discovery opens a pull request, and a green merge deploys generated pages, both discovery indexes, a sitemap and a verified build. [source](https://github.com/arm-pz/publish-pipeline) |
| [upstream-check](https://skills.caffeinity.com/upstream-check/) | Finds local commits that never reached GitHub, pushes only clean fast-forwards after a secret screen, then checks that the site index, the homepage, the marketplace and the READMEs agree with the repos that actually ship a SKILL.md. [source](https://github.com/arm-pz/upstream-check) |
| [findable-polish](https://skills.caffeinity.com/findable-polish/) | Chains Findable and Wordsmith: audits a README, skill page or landing copy against the queries a real stranger types, then writes two or three alternatives per finding that fix it without inventing a fact. [source](https://github.com/arm-pz/findable-polish) |
| [upstream-polish](https://skills.caffeinity.com/upstream-polish/) | Chains Upstream-Check — fetch-based push verdicts, fast-forward only, screened for credential-shaped lines — with Wordsmith rewriting drifted descriptions, topics and README rows, so repos and listings tell the same story again. [source](https://github.com/arm-pz/upstream-polish) |
| [skill-estate](https://skills.caffeinity.com/skill-estate/) | The whole-collection sweep: inventory every skill repo, reconcile the site, marketplace and README, tune the family, close workflow gaps, wire self-publishing, add trigger tests and listings, and leave a maintenance loop. [source](https://github.com/arm-pz/caffeinity-skills) |

### Build & Ship

| Skill | What it does |
|---|---|
| [site-prompt](https://skills.caffeinity.com/site-prompt/) | Turns a website topic into one self-contained, paste-and-build prompt: it builds and verifies the site in a scratch folder first, then embeds every file verbatim with a pinned stack and the checks that actually ran. [source](https://github.com/arm-pz/site-prompt) |
| [production-code](https://skills.caffeinity.com/production-code/) | Delivers code as a finished artifact rather than a snippet: complete scripts, bug fixes with the root cause, reviews, API integrations and SQL, each with the run instructions and the edge cases handled. [source](https://github.com/arm-pz/production-code) |
| [web-preflight](https://skills.caffeinity.com/web-preflight/) | Checks a site you own before you ship it, without pretending a status code is a finding. [source](https://github.com/arm-pz/web-preflight) |
| [pre-ship-security-red-team](https://skills.caffeinity.com/pre-ship-security-red-team/) | Red-teams a web app you own before launch, in an isolated local environment. [source](https://github.com/arm-pz/pre-ship-security-red-team) |
| [pre-ship-performance-audit](https://skills.caffeinity.com/pre-ship-performance-audit/) | Audits and fixes a web app's real-world speed before launch: four read-only subagents sweep twenty known slow-downs across images, bundles, database queries and servers, then the same mobile Lighthouse protocol, three runs per page, proves each fix before and after. [source](https://github.com/arm-pz/pre-ship-performance-audit) |
| [release-gate-chair](https://skills.caffeinity.com/release-gate-chair/) | One answer to “can we deploy?”: runs web-preflight, the security red team and the performance audit in order, keeps three separate verdicts, and computes HOLD or ready with a script instead of judgement. [source](https://github.com/arm-pz/release-gate-chair) |
| [release-gate-ledger](https://skills.caffeinity.com/release-gate-ledger/) | The release gate where each lane writes its own rows into one ledger through a validating recorder, so a malformed or missing verdict is rejected the moment it is written. [source](https://github.com/arm-pz/release-gate-ledger) |
| [release-gate-validator](https://skills.caffeinity.com/release-gate-validator/) | The cheapest release gate: turns three pre-launch reports that already exist into one posture, HOLD or ready, without running any lane or sending a single request. [source](https://github.com/arm-pz/release-gate-validator) |
| [ship-sentinel](https://skills.caffeinity.com/ship-sentinel/) · Claude Code mod | A Claude Code mod that holds git push, PR, publish and deploy commands until your pre-ship check skills have run since the last edit. [source](https://github.com/arm-pz/ship-sentinel) |
| [paper-trail](https://skills.caffeinity.com/paper-trail/) | Privacy policy, terms, refund and cookie pages written only from facts you confirm, then checked for placeholders, missing sections and emails nobody supplied. [source](https://github.com/arm-pz/caffeinity-skills) |
| [release-gate-mod](https://skills.caffeinity.com/release-gate-mod/) · Claude Code mod | Holds production deploys and PR merges in Claude Code until the release-gate chair has run web-preflight, the security red team and the performance audit since your last edit. [source](https://github.com/arm-pz/caffeinity-skills) |
| [web-preflight-mod](https://skills.caffeinity.com/web-preflight-mod/) · Claude Code mod | Reminds Claude Code to run web-preflight (exposed .env files, source maps, admin and debug surfaces) before a production deploy. [source](https://github.com/arm-pz/caffeinity-skills) |
| [pre-ship-security-red-team-mod](https://skills.caffeinity.com/pre-ship-security-red-team-mod/) · Claude Code mod | Holds production deploys in Claude Code until the pre-ship security red team has run since your last edit. [source](https://github.com/arm-pz/caffeinity-skills) |
| [pre-ship-performance-audit-mod](https://skills.caffeinity.com/pre-ship-performance-audit-mod/) · Claude Code mod | Reminds Claude Code to run the pre-ship performance audit before a production deploy. [source](https://github.com/arm-pz/caffeinity-skills) |

### SEO & Search

| Skill | What it does |
|---|---|
| [seo-crawl](https://skills.caffeinity.com/seo-crawl/) | Crawls a site you own and returns deterministic, evidence-backed technical SEO findings, with blocked or unrun checks reported INCONCLUSIVE rather than a pass. [source](https://github.com/arm-pz/seo-crawl) |
| [keyword-guard](https://skills.caffeinity.com/keyword-guard/) | Plans topic clusters and kills keyword cannibalization so exactly one page wins each query. [source](https://github.com/arm-pz/keyword-guard) |
| [keyword-resolver](https://skills.caffeinity.com/keyword-resolver/) | Resolves keyword cannibalization with Keyword-Guard, then rewrites titles, H1s and meta descriptions with Wordsmith. [source](https://github.com/arm-pz/keyword-resolver) |
| [seo-polish](https://skills.caffeinity.com/seo-polish/) | seo-crawl's measured findings, an optional seo-audit diagnosis, then Wordsmith drafts optimized alternatives for every High and Medium finding: titles, meta descriptions, headings and internal-link anchors. [source](https://github.com/arm-pz/seo-polish) |

### Writing & Content

| Skill | What it does |
|---|---|
| [wordsmith](https://skills.caffeinity.com/wordsmith/) | Teaches your agent to edit, not just generate: 44 commands across 5 disciplines that tighten, rewrite, critique and proofread while keeping the author's meaning, hedges and voice intact. [source](https://github.com/arm-pz/wordsmith) |
| [platform-content](https://skills.caffeinity.com/platform-content/) | Writes platform-native content packs from one brief: X threads, LinkedIn posts, YouTube and TikTok scripts, Instagram captions, newsletters and blog articles, each shaped to how that platform is actually read. [source](https://github.com/arm-pz/platform-content) |
| [sales-copy](https://skills.caffeinity.com/sales-copy/) | Writes buyer-facing conversion assets: long-form sales pages, landing pages, launch and abandoned-cart email sequences and ad variations, built on the offer and the objections you can actually back. [source](https://github.com/arm-pz/sales-copy) |

### Outbound

| Skill | What it does |
|---|---|
| [cold-email-list-gate](https://skills.caffeinity.com/cold-email-list-gate/) | Gate a cold-email lead list before it loads: sample ten rows, check company, title, size, and mailbox against the ICP, compare data providers on the same criteria, and return a GO or HOLD decision with the fail pattern and the re-run… [source](https://github.com/arm-pz/cold-email-list-gate) |
| [cold-email-ops](https://skills.caffeinity.com/cold-email-ops/) | Plan and audit a cold-email program at volume and keep it from degrading: computes inbox and domain capacity from a monthly send target, sets per-domain reply-rate floors, burn-replacement cadence, shadow-ban tests, and automation error… [source](https://github.com/arm-pz/cold-email-ops) |

### Career

| Skill | What it does |
|---|---|
| [recruiter-lens](https://skills.caffeinity.com/recruiter-lens/) | Reviews resumes, CVs and LinkedIn profiles the way recruiters actually screen them: first-impression scans, ATS compatibility, rejection-pattern diagnosis, and interview prep. [source](https://github.com/arm-pz/recruiter-lens) |
| [applicant-kit](https://skills.caffeinity.com/applicant-kit/) | Writes the better version: decoded job description, tailored resume, bullets rewritten as action-task-result-impact, honest keyword placement, five summaries, a LinkedIn rewrite and twenty interview answers, all built from real experience. [source](https://github.com/arm-pz/applicant-kit) |
| [application-pilot](https://skills.caffeinity.com/application-pilot/) | Runs the job search around the applications: turns role criteria into a live shortlist, scores each role for fit with evidence, keeps a reviewable tracker with submission and follow-up dates, flags roles that have gone quiet, drafts the follow-up and the interview briefing, and reads the funnel weekly. [source](https://github.com/arm-pz/application-pilot) |
| [career-track](https://skills.caffeinity.com/career-track/) | For the moves around a career: a positioning line you can repeat, the case for the next level, review and promotion narratives, salary negotiation scripts and a ninety-day plan. [source](https://github.com/arm-pz/career-track) |

### Thinking & Learning

| Skill | What it does |
|---|---|
| [research-brief](https://skills.caffeinity.com/research-brief/) | Answers “what is known about this” with a sourced brief: overviews, competitor and industry analysis, fact checks with conflicts flagged, every claim tied to a dated source and every unknown named. [source](https://github.com/arm-pz/research-brief) |
| [data-readout](https://skills.caffeinity.com/data-readout/) | Turns the numbers you already own into a readout you can act on: it opens the real file first, then gives findings with the business implication of each, chart specs and the caveats that matter. [source](https://github.com/arm-pz/data-readout) |
| [crash-test](https://skills.caffeinity.com/crash-test/) | Crash-tests a decision before you build it. [source](https://github.com/arm-pz/crash-test) |
| [do-better](https://skills.caffeinity.com/do-better/) | When an answer is bad, don't ask twice: N sub-agents (100 by default, 16 with --quick) get the exact same task with different strategy cards, then attack, defend and judge each other in a single-elimination bracket until one solution survives. [source](https://github.com/arm-pz/do-better) |
| [strategy-memo](https://skills.caffeinity.com/strategy-memo/) | Turns a business question into a decision document: situation analysis, a recommendation written as ranked options, the risks, and a roadmap someone can execute. [source](https://github.com/arm-pz/strategy-memo) |
| [solo-income-blueprint](https://skills.caffeinity.com/solo-income-blueprint/) | Turns “I want to make money online” into one plan: a business model that fits your skills, time and budget, one offer, a demand check, a minimal tool stack and a seven-day launch. [source](https://github.com/arm-pz/solo-income-blueprint) |
| [topic-primer](https://skills.caffeinity.com/topic-primer/) | A world-class teacher for any topic, from zero background toward expert depth. [source](https://github.com/arm-pz/topic-primer) |
| [study-system](https://skills.caffeinity.com/study-system/) | Builds the system around a skill you are acquiring: the minimum components, a beginner-to-practitioner roadmap, deliberate practice, spaced repetition and an honest mastery check. [source](https://github.com/arm-pz/study-system) |
| [course-builder](https://skills.caffeinity.com/course-builder/) | A course for a class or cohort: measurable outcomes, modules in prerequisite order, an assessment for every outcome and a time budget that fits, checked by a script before the first session. [source](https://github.com/arm-pz/caffeinity-skills) |

### Brews

Skills hand work to each other in brews (workflows). Start with [caffeinity-routing](https://skills.caffeinity.com/caffeinity-routing/) if you are not sure which you need.

- **Brew 1 · Pour-over:** Build a skill and make it installable: draft-skill or prompts-to-skill → tune-skill → prompts-to-skill-release → skill-to-mod (optional)
- **Brew 2 · Bloom:** Get a repo, skill or plugin found: findable → publish-pipeline → upstream-check
- **Brew 3 · Espresso:** Decide whether a site is safe to launch: web-preflight → pre-ship-security-red-team → pre-ship-performance-audit → release-gate-chair or release-gate-ledger or release-gate-validator
- **Brew 4 · Cold brew:** Grow organic search traffic: seo-crawl → keyword-guard → wordsmith → pre-ship-performance-audit (optional) → platform-content (optional)
- **Brew 5 · French press:** Land a job: recruiter-lens → applicant-kit → application-pilot → career-track (optional)
- **Brew 6 · Cupping:** Make a decision: research-brief → data-readout (optional) → crash-test or do-better → strategy-memo
- **Brew 7 · Slow drip:** Learn a skill: topic-primer → study-system → course-builder (optional)
- **Brew 8 · Nitro:** Run cold outbound: cold-email-list-gate → cold-email-ops → sales-copy
- **Brew 9 · Moka pot:** Launch a one-person product: solo-income-blueprint → site-prompt → production-code → paper-trail → release-gate-chair → platform-content
- **Brew 10 · Descale:** Maintain the skill family: tune-skill → prompts-to-skill-release (optional) → upstream-check
- **Brew 11 · Estate roast:** Stand up or audit a skill estate: skill-estate

<!-- skills:end -->

Each skill has a page on the [skills site](https://skills.caffeinity.com) with its exact install command.

---

## Install

```bash
npx skills add arm-pz/<skill-name>
```

The installer detects your agent and puts the skill in the right folder. Add `--dry-run` to preview. Some repos also need `--skill <skill-name>`; each skill's page shows the exact command.

---

## How I work

- **Honest claims.** Skills optimize what is true and never fabricate numbers, stars or results.
- **Stated limits.** Each README says what the tool does not do.
- **Approval first.** Skills ask before applying changes.

---

## Contact

Hiring or collaborating: [[LinkedIn](https://www.linkedin.com/in/itsarm/)].
Skill problems or ideas: open an issue on the skill's repo.

<sub>If a skill saved you time, you can [buy me a coffee](https://buymeacoffee.com/vagabond_) or star the repo.</sub>


