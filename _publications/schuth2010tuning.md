---
author: "Anne Schuth"
date: "2010-09-01"
key: schuth2010tuning
keywords: ""
layout: publication
pdf: /assets/master-thesis-anne-schuth.pdf
school: "University of Amsterdam"
title: "Tuning Methods in Statistical Machine Translation"
citations: 0
scholar_url: "https://scholar.google.com/citations?view_op=view_citation&hl=en&user=Y3ahb_wAAAAJ&pagesize=100&citation_for_view=Y3ahb_wAAAAJ:Tyk-4Ss8FVUC"
type: mastersthesis
year: "2010"
shield: thesis-Master-red
---

In a Statistical Machine Translation system many models, called features, complement each other in producing natural
language translations. In how far we should rely on a certain feature is governed by parameters, or weights. Learning
these weights is the subfield of SMT, called parameter tuning, that is addressed in this thesis. Three existing methods
for learning such parameters are compared. We recast MERT, MIRA and Downhill Simplex in a uniform framework, to allow
for easy and consistent comparison. Based on our findings and forthcoming opportunities for improvements, we introduce
two new methods. A straightforward sampling approach, Local Unimodal Sampling (LUS), that uniformly samples from a
decreasing area around a constantly updated peak in weightvector space. And a ranking based approach, implementing
SVM-Rank, that focusses on giving, besides the best translations, also its runner-ups a high score. We empirically
compare our own methods to existing methods and find that LUS slightly, but significantly, outperforms the
state-of-the-art MERT method in a realistic setting with 14 features. We claim that this progress, the simplicity of the
radically different approach of the method obtaining this progress and the clear overview of existing work are
contributions to the field. Our SVM-Rank showed no improvement over the-state-of-the-art within our experimental setup.
