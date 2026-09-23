# Draft v1.7: self-check (fixes after the Stage 7c round 3 cold read)

AI-authored, 2026-09-23. Compares `WIP Docs/Drafts/Draft v1.7.md` with `Old versions/Draft v1.6.md`. The report answered is `Scrap/7c-report-round3.md` (11 items; one-read test passed).

## Trend across rounds

Friction has fallen from 14 to 13 to 11. Each fresh reader mostly finds new items, but two spots recur: §2's absence-test material and Otsuka's chain in §5. The chain has been flagged by all three readers, so this round fixes its structure, not its sentences.

## Each friction item and its fix

| # | Item | Fix in v1.7 |
|---|---|---|
| 1 | §1: two claims joined by one "and" | Split: "Ramakrishnan takes his criterion to be primitive; Quong does give a rationale for his, but it attaches to use…" The preview of Quong's dilemma is replaced by a pointer to section 3, which also retires the round 1 item about claims taken "on credit" |
| 2 | Pill case has four moving parts | Retold in order: the tests and the cure; the heart attack left untreated; then the pill, which is why an absence test finds nothing amiss |
| 3 | Flamethrower pronouns come late | Characters named at introduction: "A woman defending herself with a flamethrower kills her attacker and a bystander standing behind him … the bystander's presence costs her nothing … his claim … her act" |
| 4 | Two callbacks in one clause (§3) | Split into three sentences |
| 5 | Permission-as-power packed into one clause | "Suppose that the permission not to give, a standing to favour oneself, works like a power: it takes effect only when the agent uses it in deciding what to do. Premise 3's talk … suggests as much." |
| 6 | Thomson ellipsis | "…does not make anything of the workman's serve the good deed" |
| 7 | "Neither point" | "Neither of Choo's points" |
| 8 | "MP" unglossed | "…'very much like the MP', the means principle itself" |
| 9 | Otsuka's chain overloads | **Structural fix.** The text now runs one chain: *Loop*, then the intermediate case in which the circling trolley trips the same pole, then the toppling case. The second route (the drawbridge case) moves to a new note 11 with its quotation. The map sentence now names one intermediate case |
| 10 | Unearned: why *Loop* yields | The step is shown. Keeping the *Loop* verdict while condemning the toppling case needs a principled difference, and none has been found. So it would mean giving up either the toppling verdict ("a fixed point") or the principle that explains it together with the footbridge case and the other pairs of section 2. "Giving up the single verdict on *Loop* costs less", all the more given the independent rationale |
| 11 | Unearned: non-circularity | The step is shown. The test "picks out spending without mentioning use", and "what makes spending wrong is that it overrides the permission not to give, which no one defines in terms of use" |
| — | Register: "permissibly, if viciously" | Kept. The reader judged it earned; it is one of the essay's two or three permitted landings (with the final sentence) |

## Also in this version (the diff matches)

- **Repeated point removed.** Both the pill paragraph and the flamethrower paragraph said that the test needs no stipulation about empty places. The flamethrower paragraph's clause is cut; the pill paragraph keeps the point with its question-and-answer.
- **Cuts to pay for the added steps.**
  - The note on Kamm's substitution and subordination (Kamm remains engaged in §5).
  - Liao and Barry's log case in note 6.
  - Walen's quotation in the *Loop* company note.
  - The gloss on Thomson's symmetric case in the same note.
  - The sentence restating the Alexander payoff.
- **Notes renumbered 1–13.**

## Deterministic checks

- **Displays:** byte-identical to v1.6.
- **Notes:** references and definitions [^1]–[^13] match.
- **Quotations:** 37 in the body. The two removed (Kamm's and Walen's) were intended, as a Counter diff confirms. 36 are verbatim on disk; Harris is still marked (verify).
- **Words:** 5,754 before the abstract (v1.6: 5,775).
- **Lint:** triads 17 (dispositioned as before); short sentences 6 (3 false positives); uniform-length run 3 (OK).

## Ledger

| Section | 7a | 7b | 7c-1 | 7c-2 | 7c-3 |
|---|---|---|---|---|---|
| 1 | TOUCHED | PASS | FIXED | PASS | FIXED (1) |
| 2 | TOUCHED | FIXED | FIXED | FIXED | FIXED (2, 3, repeated clause) |
| 3 | TOUCHED | FIXED | FIXED | FIXED | FIXED (4, 6, 8, 11) |
| 4 | TOUCHED | FIXED | FIXED | FIXED | PASS (no items) |
| 5 | TOUCHED | FIXED | FIXED | FIXED | FIXED (5, 7, 9, 10) |
| 6 | TOUCHED | FIXED | PASS | PASS | PASS (no items) |
