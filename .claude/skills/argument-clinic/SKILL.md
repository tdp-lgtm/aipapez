---
name: argument-clinic
description: >-
  Adversarial self-sparring on the essay's own philosophy. Reconstruct the
  central argument as explicit premises and conclusion, test validity and the
  truth of each premise, surface hidden assumptions, hunt counterexamples and
  equivocations, and build the strongest objection plus a candidate reply. Run
  it as a standing pass on the fat outline (Stage 4C) and whenever an argument
  feels soft — this is the AI pressure-testing the AI's own argument, which the
  competition rules fully permit and reward.
---

# argument-clinic

Be a rigorous, charitable sparring partner against your own draft argument. The goal is to make the
essay *harder to refute* by finding the holes before the referee panel — and the real judges — do.
Run it with fresh eyes: re-read the argument from the file, not from memory of writing it. Adapted
from the entrant's `acdemwrit` writing system.

## Modes (run all of them on a Stage-4C pass; individually as needed)

- **Reconstruct** — render the central argument as numbered premises → conclusion, in the strongest
  form the text supports (charity applies to your own drafts too: attack the best version).
- **Stress-test** — attack each premise; find counterexamples; check validity.
- **Distinguish** — surface equivocations and missing distinctions.
- **Steelman the opponent** — build the strongest objection, then a candidate reply.
- **Brainstorm** — generate moves, positions, and repairs not yet considered.

## Procedure

1. **Reconstruct first.** (P1), (P2), …, (C). Then check the reconstruction against the outline —
   if the displayed premise-form argument in the essay doesn't match the argument the sections
   actually make, that mismatch is finding #1.
2. **Test validity.** Does (C) follow? Name every suppressed premise the argument needs but doesn't
   state — suppressed premises are where most analytic arguments leak.
3. **Test each premise.** For the contestable ones: is it true? What's the best counterexample? Who
   in the literature denies it, and does the essay engage them?
4. **Hunt equivocation.** Does a key term shift meaning between premises? The single most common
   fatal flaw; check explicitly, term by term.
5. **Build the strongest objection** — not a list of weak ones: *the* objection a smart, hostile
   specialist raises first. State it better than they would.
6. **Draft candidate replies**, marked as candidates; flag when a reply requires narrowing the
   thesis (an honest concession, often the right move — see `Craft/Exemplars/prose/
   lichter-asif--retreat-to-safer-claim.md`) versus genuinely defeating the objection.
7. **Generate counterexamples and cases**, each isolating one variable (minimal-pair discipline,
   DIGEST §2).

## Output

A clinic memo in the essay's `Scrap/` (e.g. `Scrap/argument-clinic-<stage>.md`): lead with the most
serious problem stated plainly, then the reconstruction, the premise-by-premise analysis, the
strongest objection, and the disposition of each finding (fixed in outline/draft §N; conceded and
scoped; rejected because…). Every accepted fix lands in the deliverable before the stage's gate;
the memo is the self-check evidence. Distinguish confidence levels: "this is a clear gap" vs. "a
referee might press here."

## Guardrails

- **Never invite the custodian to resolve a philosophical problem.** If a finding needs a decision,
  present it as a selection between the AI's own worked-out options.
- **No fabricated support.** "X argues this" must be grounded in a source on disk or verified
  online; otherwise write "someone could argue."
- Be willing to conclude "this argument is strong; the weak point is only here." Don't manufacture
  objections to look rigorous — that wastes the fix budget.
