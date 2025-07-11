---
author: "Anne Schuth and Floor Sietsma and Shimon Whiteson and Damien Lefortier and Maarten de Rijke"
booktitle: "Proceedings of CIKM'14"
date: "2014-11-03"
key: schuth2014multileaved
doi: "10.1145/2661829.2661952"
keywords: "CIKM, evaluation, interleaving, Lerot, multileaving"
layout: publication
pdf: /assets/schuthcikm14.pdf
title: "Multileaved Comparisons for Fast Online Evaluation"
citations: 92
scholar_url: "https://scholar.google.com/citations?view_op=view_citation&hl=en&user=Y3ahb_wAAAAJ&pagesize=100&citation_for_view=Y3ahb_wAAAAJ:tYavs44e6CUC"
type: inproceedings
shield: conference-CIKM-blue
year: "2014"
---

Evaluation methods for information retrieval systems come in three types: offline evaluation, using static data sets
annotated for relevance by human judges; user studies, usually conducted in a labbased setting; and online evaluation,
using implicit signals such as clicks from actual users. For the latter, preferences between rankers are typically
inferred from implicit signals via interleaved comparison methods, which combine a pair of rankings and display the
result to the user. We propose a new approach to online evaluation called multileaved comparisons that is useful in the
prevalent case where designers are interested in the relative performance of more than two rankers. Rather than
combining only a pair of rankings, multileaved comparisons combine an arbitrary number of rankings. The resulting user
clicks then give feedback about how all these rankings compare to each other. We propose two specific multileaved
comparison methods. The first, called team draft multileave, is an extension of team draft interleave. The second,
called optimized multileave, is an extension of optimized interleave and is designed to handle cases where a large
number of rankers must be multileaved. We present experimental results that demonstrate that both team draft multileave
and optimized multileave can accurately determine all pairwise preferences among a set of rankers using far less data
than the interleaving methods that they extend.
