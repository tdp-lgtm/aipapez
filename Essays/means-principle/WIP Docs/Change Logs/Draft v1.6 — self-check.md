# Draft v1.6: self-check (fixes after the Stage 7c round 2 cold read)

AI-authored, 2026-09-23. Compares `WIP Docs/Drafts/Draft v1.6.md` against `Old versions/Draft v1.5.md`. The report being answered is `Scrap/7c-report-round2.md`: 13 items, with the one-read test passed.

## Each friction item and its fix

| # | Item | Fix in v1.6 |
|---|---|---|
| 1 | Ramakrishnan's principle is glossed in §1 but quoted only in §2 | No change. §1 gives the criterion in plain words and §2 quotes it at the point of comparison. Stating it twice at full length would repeat it |
| 2 | "Fat Man" in note 10 is untied to any case | "Of a man on the tracks whose body would stop a trolley, he writes: 'If one has no duty to rescue Fat Man, …'" |
| 3 | The case of shortage in §3 is never described | Tied to the case already told: "letting someone die who is a necessary means to others' survival when medicine is short, as with the man whose legs hold the door". "Harming" is corrected to "letting die", which matches that case |
| 4 | Apparatus overload at the Ramakrishnan comparison | "A would-be defeater" is removed from the comparison, since it is quoted and glossed once, in §3. The first difference is now "the view gives a reason for judging supply against the agent's alternatives, and his verdict on the case of twenty behind follows from that reason". The case load of §2 is reduced by moving Liao and Barry's log case to note 7 (see 8) |
| 5 | The four-clause definition of spending in §1 | **Kept.** It is the thesis definition, and its bound must stay inside it (the conclusion equates the principle with forbidding spending). The next two sentences unpack it with the test and the beam |
| 6 | The pill case: two goods in one body | "…and harmless tests on her offer a second way to cure them" |
| 7 | The Alexander step to "forbids" is unshown | The step is shown: "Leaving out the six's escape, which comes from the man's body, he reckons the diversion as if the trolley would run on into the six, and so forbids it … Against what she can choose, the diversion saves the five and costs the six nothing." |
| 8 | The roof and log case | Moved to note 7. The text keeps the flamethrower case, which shows absence tests erring in the other direction from the pill case. The paragraph now says so |
| 9 | The implicit link in "First, …" | Rewritten as one explicit sentence (see 4) |
| 10 | Quong's dilemma is a fork inside a fork | Signposted: "He considers two readings of the rationale. On the first … On the second … This second reading faces a dilemma … it collapses into the first reading" |
| 11 | The three-track wrench case | Spelled out: fifteen can be saved by turning the trolley toward the owner with his wrench, or toward three others with an unowned branch, and "Quong must require the second, which kills three instead of one" |
| 12 | The Otsuka paragraph is the densest | Split in two. The first paragraph gives the endpoint and a one-line map ("two routes, each through one intermediate case, and each step changes only a feature that seems morally irrelevant"). The second gives the routes |
| 13 | Quotable closers and the citation tally | The theft line is flattened ("no one thinks that makes theft arbitrary"). The five-name company list moves into note 12, and the text now reads "…though it is not alone in doing so". "Permissibly, if viciously" is kept: it states the view's verdict, not a flourish |

## Length and reserve cuts spent

- **Word count.** The fixes took the draft to about 5,870 words, over the cap once a 150-word abstract is added. Three reserve cuts from the v1.4 list were spent to bring it back:
  - reserve 1: Steinhoff's alternative right;
  - reserve 3: Parry's externalities sentence;
  - part of reserve 5: the Lazar and order-effects sentences in the notes.
- **Reference list.** Lazar 2019 is removed, since it is no longer cited. The script cross-check of citations against references finds nothing uncited in either direction ("Liao 2012" is flagged, but that is a false alarm: the text cites "Liao et al. 2012").
- **Remaining reserves:**
  - the *Loop* company note (now note 12), about 45 words;
  - the last clause of the §1 two-tracks paragraph, about 25;
  - Costa and the spiteful donor in the notes, about 30.

## Deterministic checks

- **Displays.** Byte-identical to v1.5.
- **Notes.** References and definitions [^1]–[^13] match.
- **Quotations.** 40 in the body; 39 verbatim on disk; Harris remains (verify). The one quotation fewer is the §2 occurrence of "a would-be defeater", removed on purpose; its §3 occurrence stays.
- **Words.** 5,775 before the abstract.
- **Lint.**
  - List triads: 17 (0.9/300w), mostly clause chains, as dispositioned in v1.4.
  - Short sentences: 6 (3 false positives).
  - Uniform-length run: 3 (OK).

## Ledger

| Section | 7a | 7b | 7c-1 | 7c-2 |
|---|---|---|---|---|
| 1 | TOUCHED | PASS | FIXED | PASS (item 5 kept, with reason) |
| 2 | TOUCHED | FIXED | FIXED | FIXED (4, 6, 7, 8, 9) |
| 3 | TOUCHED | FIXED | FIXED | FIXED (3, 10, 13; reserve 1) |
| 4 | TOUCHED | FIXED | FIXED | FIXED (2, 11; reserve 3) |
| 5 | TOUCHED | FIXED | FIXED | FIXED (12, 13) |
| 6 | TOUCHED | FIXED | PASS | PASS (no items) |
