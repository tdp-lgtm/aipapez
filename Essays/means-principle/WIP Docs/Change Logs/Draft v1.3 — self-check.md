# Draft v1.3: self-check (Stage 7a, register rewrite)

AI-authored, 2026-09-23. Checks `WIP Docs/Drafts/Draft v1.3.md` against `Old versions/Draft v1.2.md`.

## What was done

- **Rewriters.** Four prose-rewriter subagents (sonnet tier), each in a fresh context, for sections 1, 2, 3 and 4–6. Each was given only:
  - its section, as a clean file in `Scrap/`;
  - the thesis in one sentence;
  - a short glossary of terms from other sections;
  - the register-sample paths;
  - hard constraints: no growth in length; quotations, citations, placeholders and displays fixed; no new labels.
- **Re-run.** A first rewriter on sections 1–2 together stopped at the output-length limit without returning text. The sections were re-run separately, each saving its text to a file.
- **Dispositions.** Every change in every rewriter's table was dispositioned by the drafting agent. The records are `Scrap/7a-changes-s1.md`, `-s2.md`, `-s3.md` and `-s4-s6.md`, next to each rewriter's raw text (`Scrap/7a-output-… (rewriter text).md`) and the applied text (`Scrap/7a-applied-….md`). 19 edits were rejected or corrected because they:
  - changed a claim ("the good is what would justify the loss"; the duties that set the bound; the tu quoque against Ramakrishnan; the cost of burning the log);
  - broke a fixed term ("the permission not to give");
  - added a label ("the criterion camp", "*Smoke*-structured");
  - or produced a grammatical or antecedent error.
- **Substantive additions from the rewriters' flags.**
  - A gloss on Quong's rescue condition, quoted from file 09 L249.
  - The name "the replacement test" in §3's reply to Ramakrishnan's arbitrariness worry, so the reader can tell the view's two features apart.

## Deterministic checks

- **Displays.** The Spending View and the central argument (P1–P4, C) are byte-identical to v1.2.
- **Notes.** References [^1]–[^14] and definitions [^1]–[^14] match, in order.
- **Quotations.** 42 quotations. 41 are verbatim on disk; one is the new Quong quotation, file 09 L249. Harris remains (verify).
- **Words.** 5,818 before the abstract (§1 876, §2 1,303, §3 1,415, §4 646, §5 919, §6 152, notes 497). This is +9 on v1.2: the rewriters' cuts were paid back by restorations and the Quong gloss. 7b must cut at least 270 words, to 5,550 or fewer.

## Per-section ledger (Stage 7)

| Section | 7a (round 1, walked §1 → §6) |
|---|---|
| 1 | TOUCHED (rewritten; 6 edits rejected or corrected) |
| 2 | TOUCHED (rewritten; 8 rejected or corrected) |
| 3 | TOUCHED (rewritten; paragraphs split 9 → 14; 4 rejected) |
| 4 | TOUCHED (rewritten; 1 rejected, 2 corrected) |
| 5 | TOUCHED (rewritten; 3 corrected) |
| 6 | TOUCHED (final sentence realigned to "cost"/"supplies") |
