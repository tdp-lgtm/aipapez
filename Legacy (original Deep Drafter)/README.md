# Legacy — the original Deep Drafter

The workspace this repository was forked from: Simon Goldstein's Deep Drafter, an **author-driven**
academic writing agent (the author supplies the thesis and arguments; the agent executes; drafts are
Word documents the author edits under a tracked-changes protocol).

Kept for reference: the pipeline mechanics here were battle-tested on real published papers, and the
competition edition (`Playbook/`) inherits them. But the premise is inverted for the AI Philosophy
Competition — the AI must originate all substantive philosophy, the human never edits essay text, and
deliverables are Markdown — so **nothing in this folder is operative where it conflicts with the root
`CLAUDE.md` and `Playbook/`**. In particular: the author-round/tracked-changes protocol, the Voice
Profile / Model Prose personalization machinery, and the Word-document build discipline are retired.

Contents: the original playbook (`General Guide to Academic Writing/`), the author-facing guides
(`START HERE.docx`, `SETUP — Personalize the Agent.docx`, `Writing Guide — House Style.docx`),
plain-text mirrors of all of it in `Playbook mirrors/`, and the Word-era tooling in
`Build scripts (legacy)/` (playbook doc generators, the author-round/tracked-changes tools, the
mirror sync). The legacy scripts reference the old folder layout and some import `gen_docx.py`,
which stayed in the live `Behind the scenes (Claude)/Build scripts/` — run them from there if ever
needed.
