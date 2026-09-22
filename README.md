# AI Philosophy Competition Workspace

A Claude Code workspace for producing entries to the [AI Philosophy Competition, 1st
Edition](https://zacharygoodsell.com) (submission deadline: October 31, 2026): up to three
6,000-word philosophy essays, each with a methodology report, judged by a panel of academic
philosophers. The competition requires the essays to be **primarily AI generated** — the AI
originates every substantive philosophical contribution; the human entrant chooses topics, selects
among AI outputs, gives generic feedback, and submits.

Forked from Simon Goldstein's [Deep Drafter](https://simondgoldstein.com) (an author-driven academic
writing agent, preserved in `Legacy (original Deep Drafter)/`) and rebuilt for the competition: the
pipeline's proven mechanics — layered fat outlines, blind simulated referee panels, citation
auditing, an independent work auditor — now serve an AI-originated essay, with a compliance layer and
session-by-session methodology logging on top.

## How it works

- **AI-originated ideas.** The pipeline starts by generating many candidate theses, pre-screening
  them for originality against the literature, and writing up the best as argument sketches. The
  human selects; the AI argues.
- **Compliance by construction.** `Competition/Rules — Human Involvement.md` encodes the
  competition's permitted/forbidden lists; the agent flags and quarantines any human message that
  contains philosophical substance, and the human never edits essay text.
- **Everything logged.** Every session is recorded verbatim in a per-essay Process Log, from which
  the required methodology report is assembled — which itself competes for the competition's
  US$5,000 creative-methodology prize pool.
- **Quality machinery.** Outline-first drafting, separated quality and clarity passes keyed to the
  six judging criteria, blind referee panels, citation audits against real sources, and an integrity
  auditor that verifies claimed work against files.

## Layout

- `CLAUDE.md` — the agent's standing instructions.
- `Competition/` — the rules distilled, plus the organizers' PDFs.
- `Playbook/` — pipeline, essay style guide, methodology protocol, project template, referee
  templates (all Markdown).
- `Essays/` — one folder per essay.
- `Model Prose/` — register models (read for sentence shapes, never content).
- `.claude/agents/` — the referee, citation-auditor, copy-critic, and paper-auditor subagents.
- `Behind the scenes (Claude)/Build scripts/` — scaffolding and word-count tools (plus legacy
  Word-era tooling).
- `Legacy (original Deep Drafter)/` — the original workspace, for reference.

## Getting started

Open the folder in [Claude Code](https://claude.com/claude-code) and say "new essay". The agent runs
the intake (topic or topic proposals, autonomy level, timeline) and drives the pipeline from there.
Register on OpenReview early — it can take up to two weeks without institutional affiliation.

## License

MIT. The upstream Deep Drafter is © Simon Goldstein, MIT-licensed.
