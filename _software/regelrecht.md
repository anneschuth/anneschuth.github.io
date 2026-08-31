---
title: RegelRecht
slug: regelrecht
order: 3
link: https://regelrecht.rijks.app
repo: https://github.com/MinBZK/regelrecht
summary: Dutch government exploration into machine-executable legislation; NRML rule format, execution engines, AI converter, simulation.
publications:
  - hotting2026
---
RegelRecht is an exploration by the Dutch Ministry of the Interior (Bureau Architectuur Digitale Overheid) into machine-executable
legislation. The project investigates how we can achieve transparent, unambiguous, and consistent execution of laws -
enabling everyone to understand how decisions are made.

This initiative explores whether laws can be written as directly executable code, eliminating the gap between
legislation and implementation. By creating machine-readable legal specifications, RegelRecht aims to:

- Provide one single source of truth for legal rules that all parties use
- Enable full transparency and traceability of government decisions
- Test new legislation before implementation to detect conflicts and inconsistencies
- Reduce interpretation differences across government organizations

The ecosystem includes NRML (Normalized Rule Model Language) as a JSON-based format for machine-executable laws,
execution engines in multiple programming languages, an AI-powered converter for existing analog law, a visual law
editor, and simulation environments for testing legislative impact.

Learn more at [regelrecht.rijks.app](https://regelrecht.rijks.app). The engine and the encoded corpus live
[on GitHub](https://github.com/MinBZK/regelrecht); the earlier Python proof of concept, which explored the same ideas
under the name poc-machine-law, is [still available](https://github.com/MinBZK/poc-machine-law).
