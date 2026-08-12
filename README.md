# Deep Drafter

A workspace that turns a one-page brief into a finished, referee-tested academic paper,
written with Claude. The author supplies the thesis, the central arguments, and the judgment
calls; Claude does the execution. Developed by [Simon Goldstein](https://simondgoldstein.com)
with Claude over a series of real papers in philosophy and law, including
["Epistocracy and the Commitment Problem"](https://philpapers.org/rec/GOLEAT-14)
(*Philosophy & Public Affairs*, 2026), his first paper written this
way. This edition is generalized: one setup session calibrates it to your field, your venues,
and your prose.

## How it works

- **Outline first.** A skeleton, then an argument outline, then a paragraph-by-paragraph
  outline at roughly a third of final length. No prose is written until the author approves
  the paragraph outline: structure gets settled where changing it is cheap.
- **Voice.** A style pass rewrites every sentence into the author's voice, calibrated on
  three to six of their own papers collected at setup. The author only ever reads voiced
  prose.
- **Blind referees.** Simulated referee panels receive the manuscript, the venue, and
  nothing else: no summary of the claims, no leading questions.
- **Citation audit.** Every reference is checked against the actual sources. A real-looking
  cite with no backing source is a defect, not a draft.
- **Work audit.** A separate auditor verifies against the files, never the agent's claims,
  that each stage of work genuinely happened.
- **Author sovereignty.** Every version is kept, nothing is overwritten, and the author's
  edits are never reverted.

## Getting started

Note: because the agent uses a lot of tokens, it will only work well if you have a Claude Max account.

1. Clone this repository, or download it with Code > Download ZIP.
2. Open the folder in [Claude Code](https://claude.com/claude-code).
3. Say: "Set up Deep Drafter for me."

Claude interviews you about your field, your venues, your coauthors, and your standing
preferences, collects three to six of your best papers, and builds the Voice Profile it will
imitate when drafting for you. Setup takes one session. After that, starting a paper is a
one-page brief and a short intake. The guide written for authors is `START HERE.docx`. You
never run scripts or read code yourself; Claude does.

## What's inside

- `START HERE.docx`: the author-facing guide.
- `SETUP — Personalize the Agent.docx`: the one-time calibration procedure.
- `CLAUDE.md`: the agent's standing instructions.
- `General Guide to Academic Writing/`: the pipeline, the style modules (philosophy paper,
  law review, Cambridge Element, empirical social science), the prose-register guides, the
  referee templates, and the project template.
- `Writing Guide — House Style.docx`: the stylistic core, personalized at setup.
- `.claude/agents/`: the four subagents (referee, citation auditor, copy critic, paper
  auditor).
- `Behind the scenes (Claude)/`: build scripts and plain-text mirrors of the playbooks.
- `Examples of papers produced using this agent/`: real papers written with the agent.
- `Papers/`: where your papers go.

## Disclosure

Journals and fields differ on disclosure of AI assistance, and the policies are changing
fast. The agent records your standing stance at setup and asks again for each venue;
nothing is submitted until you have settled it.

## License

MIT. Share and adapt freely.
