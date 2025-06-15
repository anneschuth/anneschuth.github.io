---
author: "Anne Schuth and Robert-Jan Bruintjes and Fritjof Büttner and Joost van Doorn and Carla Groenland and Harrie Oosterhuis and Cong-Nguyen Tran and Bas Veeling and Jos van der Velde and Roger Wechsler and David Woudenberg and Maarten de Rijke"
booktitle: "Proceedings of SIGIR'15"
date: "2015-08-09"
key: schuth2015probabilistic
doi: "10.1145/2766462.2767838"
keywords: "evaluation, interleaving, Lerot, multileaving, poster, SIGIR"
layout: publication
redirect_from: /publications/schuth_2015_probabilistic.html
pdf: /assets/schuth-probabilistic-2015.pdf
title: "Probabilistic Multileave for Online Retrieval Evaluation"
type: inproceedings
shield: conference-SIGIR-blue
year: "2015"
---

In this paper we present the first method for integrating user satisfaction metrics with interleaving. We show how
interleaving can be extended to (1) directly match user signals and parameters of AB metrics, and (2) how parameterized
interleaving credit functions can be automatically calibrated to predict AB outcomes. We also develop a new method for
estimating the relative sensitivity of interleaving and AB metrics, and show that our interleaving credit functions
improve agreement with AB metrics without sacrificing sensitivity. Our results, using 38 large-scale online experiments
encompassing over 3 billion clicks in a web search setting, demonstrate up to a 22% improvement in agreement with AB
metrics (constituting over a 50% error reduction), while maintaining sensitivity of one to two orders of magnitude above
the AB tests. This paves the way towards more sensitive and accurate online evaluation.Online evaluation methods for
information retrieval use implicit signals such as clicks from users to infer preferences between rankers. A highly
sensitive way of inferring these preferences is through interleaved comparisons. Recently, interleaved comparisons
methods that allow for simultaneous evaluation of more than two rankers have been introduced. These so-called
multileaving methods are even more sensitive than their interleaving counterparts. Probabilistic interleaving—whose main
selling point is the potential for reuse of historical data—has no multileaving counterpart yet. We propose
probabilistic multileave and empirically show that it is highly sensitive and unbiased. An important implication of this
result is that historical interactions with multileaved comparisons can be reused, allowing for ranker comparisons that
need much less user interaction data. Furthermore, we show that our method, as opposed to earlier sensitive multileaving
methods, scales well when the number of rankers increases.
