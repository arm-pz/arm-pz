# ArmBot voice script

These are the lines ArmBot says during a call, written in the first person for your cloned voice. Generate each line in Voice Studio, export it with the exact filename shown, and put the files in `assets/voice/` in the arm-pz/arm-pz repo.

When a clip is there, the site plays it with captions timed to it. When a clip is missing, ArmBot reads that line with the browser voice instead, so you can add clips one at a time.

The lines are spelled for the ear ("C sharp", "dot NET", "skillsmith dot tech"), so paste them into Voice Studio as written. The captions show the written forms (C#, .NET, skillsmith.tech) automatically.

## Export settings

- Format: **MP3**, mono, 64 to 128 kbps (44.1 or 48 kHz)
- Trim the silence at the start and end. A clip should begin speaking right away.
- Keep the same voice, speed and style for every line so the call sounds consistent.
- Name each file exactly as shown, all lowercase.

## Lines (18 clips)

| # | File | When it plays | Line |
|---|---|---|---|
| 1 | `greeting.mp3` | Call connects | Hey, this is Abdul Rahman. Well, an AI version of my voice. Ask me about pr-graph, the merge gate I built for agent-written code, my evals and review tools, or how to reach me. |
| 2 | `about.mp3` | "What does he do?" / "who are you" | I build merge gates, review loops and evals for code written by agents in Claude Code and Codex, so it only lands when it can prove itself. Underneath that are ten years shipping C sharp, dot NET and AWS in production. |
| 3 | `prgraph.mp3` | pr-graph, merge gate, evaluation, review loop | pr-graph is my merge gate. Agents review a pull request, fix the blocking findings, and a fresh reviewer checks every fix. Then a Python gate decides. It holds any PR with an open critical or high finding, a stale review, a hold label, or a change to protected files, and it only merges the exact commit that was reviewed. Its tests include thirty-four known-bad states it must refuse. |
| 4 | `experience.mp3` | experience, career, years | I've spent ten years in enterprise delivery. Cognizant from 2016, then Infosys, then Accenture on the Comcast programme. Since late 2024 I've been at Crezantium, working remotely from Coimbatore. |
| 5 | `mcp.mp3` | MCP, model context | I build MCP servers in C sharp with explicit read and write contracts, so AI agents only touch approved business data. At Crezantium that covered trade workflows and a procurement and sales lead tracker. |
| 6 | `skillsmith.mp3` | SkillSmith, skills | SkillSmith is my free, open-source library of more than eighty agent skills, written as plain markdown, plus twelve chained workflows and seven Claude Code mods. You'll find it at skillsmith dot tech. |
| 7 | `deeptutor.mp3` | deep-tutor, teaching | deep-tutor is an open-source teaching skill I wrote. It turns any topic into structured lessons across eight modes, from foundations and staged curricula to readiness checks and graded quizzes. |
| 8 | `aws.mp3` | AWS, cloud, Lambda, Terraform | On AWS I work with Lambda, SQS, SNS, S3, DynamoDB, Cognito and Glue, with Terraform and CloudFormation for infrastructure. At Accenture I built AWS microservices and ASP dot NET Core APIs with automated CI CD. |
| 9 | `coaching.mp3` | coaching, mentoring, enablement | AI coaching and enablement is my focus. I help teams turn Claude Code, Codex and Cursor into simple, repeatable habits. I also mentored junior developers through weekly code reviews at Accenture. |
| 10 | `award.mp3` | award, Accenture | At Accenture I received the Client Champion Award for 2022 to 2023, which put me in the top five percent. |
| 11 | `kaapi.mp3` | Kaapi, coffee, Caffeinity | Kaapi by Caffeinity is a live web app of mine at kaapi dot caffeinity dot com. The brass dabara on my desk links there too. |
| 12 | `shuatlas.mp3` | Shu Atlas, acupuncture, Wu Xing | Shu Atlas is my interactive guide to the Five Elements. It has a twelve-channel metro map of sixty-five points, anatomical overlays, a ten-module course and a sixty-point recall quiz. |
| 13 | `contact.mp3` | contact, hire, reach, LinkedIn | The best way to reach me is LinkedIn, at slash in slash its arm, or on X at abdul rahman p z. I'm available for remote work and can join immediately. |
| 14 | `education.mp3` | education, degree, college | I studied an Integrated M.Sc. in Software Engineering at Sri Krishna College of Engineering and Technology in Coimbatore, from 2010 to 2015. |
| 15 | `ollama.mp3` | Ollama, local models, prompts | I design agent instructions and local model workflows with Ollama, along with preflight checks for tool contracts, failure cases and instruction quality. |
| 16 | `location.mp3` | location, remote, where | I'm based in Coimbatore, India. I work remotely and can join immediately. |
| 17 | `fallback.mp3` | Anything it has no answer for | I can only answer from what's on this site. Try asking about my experience, MCP servers, SkillSmith, AWS, coaching, or how to get in touch. |
| 18 | `goodbye.mp3` | End Call | Thanks for calling. Talk soon! |

## Adding the clips

1. Generate and export all 18 files.
2. Put them in `assets/voice/` in the arm-pz/arm-pz repo. On GitHub: open the repo, then **Add file → Upload files**, drag them in, and set the folder path to `assets/voice/`. Or send them to Claude to add.
3. Commit. GitHub Pages republishes within a minute or two, and the call on https://arm-pz.github.io/arm-pz/ speaks in your voice.

To change a line later, edit `VOICE_LINES` in `index.html` and `studio.html`, update this file, and re-export that one clip.
