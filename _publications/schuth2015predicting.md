---
author: "Anne Schuth and Katja Hofmann and Filip Radlinski"
booktitle: "Proceedings of SIGIR'15"
date: "2015-08-09"
key: schuth2015predicting
doi: "10.1145/2766462.2767695"
keywords: "A/B testing, evaluation, interleaving, SIGIR"
layout: publication
redirect_from: /publications/schuth_2015_predicting.html
pdf: /assets/fp041-schuthA.pdf
publisher: "ACM"
title: "Predicting Search Satisfaction Metrics with Interleaved Comparisons"
citations: 48
scholar_url: "https://scholar.google.com/citations?view_op=view_citation&hl=en&user=Y3ahb_wAAAAJ&pagesize=100&citation_for_view=Y3ahb_wAAAAJ:VaXvl8Fpj5cC"
type: inproceedings
shield: conference-SIGIR-blue
year: "2015"
---

The gold standard for online retrieval evaluation is AB testing. Rooted in the idea of a controlled experiment, AB tests
compare the performance of an experimental system (treatment) on one sample of the user population, to that of a
baseline system (control) on another sample. Given an online evaluation metric that accurately reflects user
satisfaction, these tests enjoy high validity. However, due to the high variance across users, these comparisons often
have low sensitivity, requiring millions of queries to detect statistically significant differences between systems.
Interleaving is an alternative online evaluation approach, where each user is presented with a combination of results
from both the control and treatment systems. Compared to AB tests, interleaving has been shown to be substantially more
sensitive. However, interleaving methods have so far focused on user clicks only, and lack support for more
sophisticated user satisfaction metrics as used in AB testing.
