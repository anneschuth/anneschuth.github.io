---
author: "Anne Schuth and Harrie Oosterhuis and Shimon Whiteson and Maarten de Rijke"
booktitle: "Proceedings of WSDM'16"
date: "2016-02-22"
key: schuth2016multileave
doi: "10.1145/2835776.2835804"
keywords: "learning to rank, Lerot, multileaving, online learning, WSDM"
layout: publication
pdf: /assets/wsdm2016-multileave-gradient-descent.pdf
publisher: "ACM"
title: "Multileave Gradient Descent for Fast Online Learning to Rank"
citations: 109
scholar_url: "https://scholar.google.com/citations?view_op=view_citation&hl=en&user=Y3ahb_wAAAAJ&pagesize=100&citation_for_view=Y3ahb_wAAAAJ:M7yex6snE4oC"
type: inproceedings
shield: conference-WSDM-blue
year: "2016"
---

Modern search systems are based on dozens or even hundreds of ranking features. The dueling bandit gradient descent (
DBGD) algorithm has been shown to effectively learn combinations of these features solely from user interactions. DBGD
explores the search space by comparing a possibly improved ranker to the current production ranker. To this end, it uses
interleaved comparison methods, which can infer with high sensitivity a preference between two rankings based only on
interaction data. A limiting factor is that it can compare only to a single exploratory ranker.
