---
author: "Anne Schuth and Eelco Hotting"
booktitle: "Legal Knowledge and Information Systems: JURIX 2026, the Thirty-ninth Annual Conference"
date: "2026-12-09"
key: schuth2026testing
keywords: "formalization of legislation, test oracle, explanatory memorandum, acceptance testing, mutation testing, large language models, rules as code"
layout: publication
pdf: /assets/schuth-hotting-jurix2026.pdf
publisher: "IOS Press"
selected: true
title: "Testing the Rules as Executed against the Rules as Promised"
type: inproceedings
year: "2026"
shield: conference-JURIX-blue
repo: https://github.com/NederlandseDigitaleDienst/regelrecht
---

Where government executes the law from formalized rules, the formalization has to be tested against what the statute
was meant to yield. But the expected outcomes a test needs almost always come from the formalizer, so the tests inherit
the reading they were meant to check. The Dutch legislative record holds an oracle that neither the encoder nor the
executing organization sets: the worked examples with which the government shows parliament what a bill should arrive
at. A full-text harvest scores 5,068 passages in 2,415 documents as candidates, and a recall check suggests the harvest
finds at most about half. We transcribed seventeen examples under a rule that forbids inventing cases and ran fifteen
against a public corpus of encoded statutes. The other two exemplify provisions the corpus does not model. Eleven
reproduce the promised amount. Among the four failures is a household the government's own amendment note had falsified
before the act took effect, and auditing the expectations around it found three defects in our encodings. The same
material shows what the oracle cannot do. An example states a third of the inputs an encoding needs, and rarely places
one on a threshold. Of the 53 faults seeded into the allowance scheme, the encoders' twelve scenarios catch 23 and two
built from the memorandum's arithmetic catch 12, each missing what the other finds. Examples go stale as soon as a
parameter moves, and they rarely touch the open norms where the concretizations live. Worked examples belong in the
record of how a statute becomes executable rules: the specification file the Council of State asked for in 2021,
maintained with the law and layered with the policy rules and judgments that carry what a memorandum cannot.

Accepted for publication in the proceedings of JURIX 2026. The PDF is the camera-ready version.
