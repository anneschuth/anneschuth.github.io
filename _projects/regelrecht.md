---
title: RegelRecht
slug: regelrecht
order: 1
link: https://regelrecht.rijks.app
repo: https://github.com/NederlandseDigitaleDienst/regelrecht
summary: Dutch government exploration into machine-executable legislation; rulework format with the legal text alongside, BDD scenarios, Rust/WebAssembly reference engine.
publications:
  - hotting2026
  - schuth2026testing
  - bos2026jurix
---
RegelRecht is an exploration by the [Nederlandse Digitale Dienst](https://digitaledienst.overheid.nl) into
machine-executable legislation, and one of the three projects in the service's starting selection. The question is
whether a law can be written as code that runs, so that different organizations apply the same law the same way and a
citizen can follow how a decision about them was reached.

Each regulation becomes a *rulework*: a YAML file with the legal text and its machine-executable interpretation side by
side, article by article, one file per version. A versioned JSON Schema guards the structure. The intended outcomes are
written down as Gherkin scenarios that lawyers and developers both read. Where possible they come straight from the
explanatory memorandum, so a table in the parliamentary papers becomes a test that has to keep passing.

The reference engine is written in Rust and compiles to WebAssembly, which gives the same result on a server and in
the browser. It is a reference and not a requirement. RegelRecht fixes the rule format and the expected outcomes; any
implementation that reproduces them on the same rules and data will do.

Two choices weigh more than the technology. Open norms stay visible: where a law leaves room for interpretation, the
rulework marks the open term and records who fills it in, instead of letting a programmer's choice quietly become law.
Judgements that belong to a person, such as a hardship clause, stay with a person. And there is no single central
interpretation. The competent authority publishes its reading, others can publish theirs next to it, and whoever
receives a decision can run the rule again and check the outcome. Eelco Hotting and I work out that argument in
[Rules as Executed](/publications/hotting2026).

Around the engine sit an LLM-assisted converter for existing law, an editor for legal experts that is still taking
shape, a graph of how laws depend on each other, and a [demo](https://demo.regelrecht.rijks.app) with a citizen portal
and a simulation of legislative change. The [roadmap](https://regelrecht.rijks.app/roadmap) splits the work into five
phases, from defining what machine-readable legislation has to do up to anchoring it in institutions.

More at [regelrecht.rijks.app](https://regelrecht.rijks.app). The engine and the encoded corpus live
[on GitHub](https://github.com/NederlandseDigitaleDienst/regelrecht).
