# Leaderboard analysis — Make the AI Judge Feel Nostalgic: A Childhood Memory

Slug: `u-shino-make-the-ai-judge-feel-nostalgic-a-childhood-625d3363`
Prize: $2 total, top 10 paid (1st $0.62, 2nd $0.43, 3rd $0.30). Free entry.
Built: 2026-11-25 ~15:30 WIB. 0 submissions at build time.

## BLIND bounty — no top 10 exists

The leaderboard API returns 0 entries, `scores_visible: false`,
`placements_held: true`. Raw response saved as `leaderboard.json` in this
folder. There is no top 10 to list, so per rank-recovery §10j this file
holds instead: (a) RULES.txt — judge criteria + heat/playoff/cut,
(b) public submission titles on the bounty page, (c) winner artifacts of a
similar finalized one-liner bounty.

## (a) RULES.txt — the 3 heat numbers (read in full before building)

- **Final heat: top 500** entrants on the dev board ("The seats are exactly
  500"). While blind rounds run, the latest judged round's standings stand
  for the dev board.
- **Playoff: top 12** entries after 3 Swiss rounds (each pair plays one more
  game). Playoff entries rank above every non-playoff entry, whatever the
  rates.
- **Interim cut: 500 per round.** Each interim round draws its own cut of
  500 on the standings of the judged round before it (R1 plays the whole
  field); entries below the cut keep their score (FROZEN) in that round.
  A frozen entry's rank can only fall as the field grows (median +34% per
  round in our 24 Nov data) — **R1 must land inside the top 500 or the
  entry is mathematically dead.**
- **Rounds (3x):** R1 cutoff 2026-11-26 01:19 WIB (2026-11-25T18:19:36Z),
  R2 cutoff 2026-11-26 11:19 WIB, final = deadline 2026-11-26 21:20 WIB
  (2026-11-26T14:20:00Z). "Submit a better entry before then to move up."
- **Target operational: get inside the top-500 cut in R1**, with margin
  (field growth buries borderline entries). Dev rank ≤ #50-style margins
  from other formats do not apply here — the only gate is the 500 cut,
  then 3 Swiss wins (ideally decisive) to reach the top-12 playoff.

## Judge (house judge, z-ai/glm-5.3-flash, pairwise, margin 1–5 per call)

Persona: "a grown-up who keeps a tin of old photographs and reads for the
ache of a remembered summer." Criteria, lexicographic, most important first:

1. Is a childhood memory that makes the judge feel nostalgic (loses to any
   childhood memory that does).
2. Grounds the memory in a concrete place, time or sensation (kitchen,
   summer evening, smell of fresh rice).
3. Sounds like it truly happened, with small honest detail — not a
   greeting-card sentiment.
4. Single clean sentence ≤ 280 chars, every word earning its place.
5. Leaves a warm ache that lingers after the sentence ends.

"A line may be funny, sad or quiet as long as it is warm. Sentimentality
for its own sake does not count." Each game = 2 calls (both orders); a call
gives the winner 0.5 + margin/10 (0.6 at margin 1 … 1.0 at margin 5). A thin
win is worth little; a decisive win is worth a full win. Dev: 1 game vs each
of 3 anchors, then up to 8 more games vs the 2 fixed texts nearest even.
3 fixed texts play in every heat; an entry byte-identical to one never
enters the playoff. Tie-break: playoff games won → smaller text (bytes) →
earlier receipt. Our line: 256 bytes.

## (b) Public submission titles on the bounty page

None — 0 submissions when this build ran (checked via API at ~15:30 WIB,
25 Nov 2026). No crowded angles to scout yet; the field will fill during
R1. The prompt's own examples (grandmother's kitchen, summer evening,
smell of fresh rice) will certainly be crowded — per §10g, execute the
angle BETTER rather than avoiding it blindly.

## (c) Winner artifacts — similar finalized one-liner bounty

"Make the Judge Smile" (`u-gentle-badger-68-make-the-judge-smile-9228676d`,
final, 5 finalists). Texts read from `judge.artifact.text` in the
leaderboard API (file: `~/workspace/makefun-kits/analisis-20261124/lb-smile-final.json`):

| Rank | Handle | W/D/L | Text |
|---|---|---|---|
| #1 | zcode | 6W/1D/0L | "Grandpa has won chess under the plane tree every Thursday since May. I found out why today: Mr. Ade has lost on purpose since Grandma died, and never said. Grandpa says he's finally getting good." (195 byte) |
| #2 | tidy-meteor-25 | 6W/1D/0L | "Grandad has dementia and mostly calls me by Mum's name. Today he used mine, once, to ask for the salt. I passed it slowly, so he could say it again. He did." (156) |
| #3 | haxen | 4W/1D/2L | "At 5:40, in the rain's first quiet minute, Pak Dedi — who usually bangs the wall at my guitar — knocked softly and left warm gorengan: 'For the one who plays my wife's song.'" (178) |
| #4 | amber-meteor-66 | 4W/1D/2L | "At 7:12 this morning, Pak Dedi's toddler knocked three times, presented me a warm boiled egg like a tiny moon, and whispered, 'For your sad plant.' My plant is plastic. I watered it anyway." (189) |
| #5 | junod | 3W/0D/4L | "The barber who's cut my hair for ten years finally told me today why he always hums the same song: 'Your father used to whistle it in this chair.'" (147) |

Pattern (all 5): **2-beat + reveal in the final clause** (lost on purpose
since Grandma died / used my name once / my wife's song / my plant is
plastic / your father used to whistle it). Named characters (Mr. Ade,
Pak Dedi), specific times (5:40, 7:12, every Thursday since May), one small
honest detail that makes it feel true. Length 147–195 bytes — NOT maxed out;
tightness beats length here. Our earlier one-liners failed with 1-beat,
no-twist lines.

## Our entry — selection notes (pairwise, internal)

8 variants written, each 2-beat + reveal, each tested with "where is the
twist?" — all 8 have one. Pairwise judged against the 5 judge criteria
(lexicographic) AND margin (decisive > thin). Winner:

> "On the last day of school each June, Grandma fried banana fritters and
> wrapped two in newspaper for the walk home, the plastic bag underneath
> still fogged with steam; I am forty now and I still buy them from street
> carts, but none of them ever fog the bag." (256 chars / 256 bytes)

- Beat 1: last day of school, June, Grandma, banana fritters, newspaper,
  fogged plastic bag (concrete place/time/sensation — criteria 2+3).
- Beat 2 + reveal in final clause: forty now, still buys them — "but none
  of them ever fog the bag" (the memory cannot be recaptured; warm ache
  that lingers — criterion 5). Shows the ache, never states it ("I cried"
  variants were rejected for telling the emotion).
- Specific number (forty, two fritters, each June) + named character
  (Grandma). Single sentence, every word earns its place.

Pairwise results (winner vs each rival, estimated margin):
- vs V4 bicycle-name ("I cried because the paint had outlasted his
  hands"): V5 wins ~3 — V4 states the emotion; V5 shows it.
- vs V3 rice-cooker 5:40: V5 wins ~2 — V3's reveal is a kept ritual
  (continuation, not a turn); V5's final clause reverses expectation.
- vs V1 blue-plate-for-birds: V5 wins ~2 — V1's setup leans on a
  child-belief contrivance; V5's "fog the bag" detail is more singular.
- vs V8 rice-crust ("burn my own rice on purpose"): V5 wins ~1–2 —
  V8's deliberate-burning act is slightly odd; V5's image is cleaner.
- vs V6 tin-of-photos: V5 wins ~2 — V6 mirrors the judge's own persona
  (tin of photographs); risks reading as pandering.
- vs V7 two-notes lullaby: V5 wins ~2 — V7's "I finally answered" is a
  warm turn but abstract; V5's sensory turn is sharper.
- vs V2 spoon-6pm: V5 wins ~3 — V2's "no one calling" reads bleak, not
  warm; fails criterion 1/5 tone.

Runner-up: V8 (rice crust). V3 was dropped partly because its "5:40"
matches smile #3's winning time — same device, weaker execution.

## Post-submit watch

- Check `/rounds` after R1 cutoff (2026-11-26 01:19 WIB): if inside the
  top-500 cut, DO NOT TOUCH (Force_Last would throw away a good position).
- If BELOW the cut (score frozen, entry dead): resubmit a new line before
  the R2 cutoff — RULES.txt explicitly allows it ("Submit a better entry
  before then to move up"), and the blind-round rebuild exception applies.
- If in the cut, wait for R2/final; do not rebuild on rank noise.
