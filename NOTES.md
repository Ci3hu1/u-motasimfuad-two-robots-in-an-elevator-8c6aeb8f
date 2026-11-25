# Notes — u-motasimfuad-two-robots-in-an-elevator-8c6aeb8f

- Bounty: "Two Robots in an Elevator", $10 total, 10 paid places
  ($3.10/$2.16/$1.51/$1.06/$0.74/$0.52/$0.36/$0.25/$0.18/$0.12).
- Free entry (entry_fee null), no prerequisites. Harness program/v1.
  Entry program writes ONE text to /output/entry.txt, UTF-8,
  1–199 chars, not only whitespace.
- Entries close 2026-11-25 23:00 UTC (26 Nov 06:00 WIB). Blind rounds 3;
  round 1 cutoff 15:19:54 UTC (22:19:54 WIB 25 Nov), round 2 19:09:57 UTC
  (26 Nov 02:09:57 WIB), final 23:00 UTC. Results 18 Dec 2026.
- Judge: house judge, pairwise, both orders; dev grade against house
  texts first (11 games), then final heat: top 500 on the dev board,
  3 Swiss rounds + playoff top 12. Criteria in order: (1) really a
  robot's elevator small-talk line; (2) machine logic / sensors /
  firmware / charging shows through; (3) awkwardness lands (pause,
  forced courtesy, the unnamed thing); (4) funny on first read, a
  surprising turn, not a tired pun; (5) tight, every word earns its
  place. Ties: playoff games, then smaller text, then earlier receipt.
- Field at discovery: 601 submissions. Quota at build time: can_submit
  true, day cap 5 left.

## Chosen line (v1)

> We have ridden this elevator together 214 times. I still don't know your name, and my memory is perfect.

- 104 chars. One specific detail: **214** shared elevator rides.
- Candidates tried and dropped: see STRATEGY.md.

## Live score / rank

- NOT YET SUBMITTED — built only, awaiting Joni's 'Setuju'.
- Blind rounds: no live score until the dev grade is recorded. After
  submit, check `makefun rounds <slug>` after the R1 cutoff, then read
  the judge's hidden reasons (GET /api/submissions/<id>,
  scores[0].judge.heat.matches[].calls[].reason) before building any v2.
