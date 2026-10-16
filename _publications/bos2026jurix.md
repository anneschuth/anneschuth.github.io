---
author: "Floortje Bos and Anne Schuth and Jieying Chen"
booktitle: "Legal Knowledge and Information Systems: JURIX 2026, the Thirty-ninth Annual Conference"
date: "2026-12-09"
key: bos2026jurix
keywords: "rules as code, large language models, explainable AI"
layout: publication
publisher: "IOS Press"
selected: true
title: "From Rules as Executed to Citizen Explanation: Evaluating LLM-Generated Explanations in Rule-Based Government Systems"
type: inproceedings
year: "2026"
shield: conference-JURIX-blue
student: bos-floortje
pdf: /assets/bos-schuth-chen-jurix2026.pdf
repo: https://github.com/Bosfloortje/machine-law-thesis-flora
---

Governments increasingly use automated decision-making systems to apply legislation in domains such as social benefits,
taxation, and licensing. While Rules as Code (RaC) approaches enable legally consistent and transparent decision-making
through executable legislation, they do not automatically generate explanations that are understandable for citizens.
Large language models (LLMs) can support natural-language explanation generation, but may hallucinate facts or exclude
legally relevant information. This paper investigates how Graph-based LLM architectures can generate citizen-focused
explanations from deterministic rule-engine traces. A rule engine evaluates synthetic citizen profiles against
formalised Dutch legislation and produces execution traces, which are transformed into structured decision
representations for explanation generation. The approach is evaluated using automated metrics and human annotation.
Results show that explicitly exposing decisive legal conditions improves faithfulness, and that the full Graph
configuration, which combines a structured decision graph with a constrained prompt, further improves alignment with the
rule-execution trace. Human evaluation shows that explanations perceived as understandable by citizens are not always
considered legally correct by experts. The findings suggest that structured
representations of deterministic legal reasoning can support legally faithful and citizen-focused explanations of
automated government decisions. The source code is published.

Accepted for publication in the proceedings of JURIX 2026. The PDF is the camera-ready version. This is the full paper
based on Floortje's MSc thesis; the [thesis abstract](/publications/bos2026from) appeared at BNAIC/BeNeLearn 2026.
