---
title: "SIGIR'15 Full Paper on 'Predicting Search Satisfaction Metrics with Interleaved Comparisons' Accepted"
date: '2015-04-17T12:03:02+02:00'
author: Anne
layout: post
permalink: /sigir15-full-paper-on-predicting-search-satisfaction-metrics-with-interleaved-comparisons-accepted/
categories:
    - Paper
    - Publication
---

Our paper [Predicting Search Satisfaction Metrics with Interleaved Comparisons](/publications/schuth-2015-predicting)
with Anne Schuth, [Katja Hofmann](http://katja-hofmann.de/),
and [Filip Radlinski](http://research.microsoft.com/~filiprad/) was accepted as a full paper
at [SIGIR 2015](http://www.sigir2015.org/).

### Abstract

The gold standard for online retrieval evaluation is AB testing. Rooted in the idea of a controlled experiment, AB tests
compare the performance of an experimental system (treatment) on one sample of the user population, to that of a
baseline system (control) on another sample. Given an online evaluation metric that accurately reflects user
satisfaction, these tests enjoy high validity. However, due to the high variance across users, these comparisons often
have low sensitivity, requiring millions of impressions to detect statistically significant differences between systems.
Interleaving is an alternative online evaluation approach, where each user is presented with a combination of results
from both the control and treatment systems. Compared to AB tests, interleaving has been shown to be substantially more
sensitive. However, interleaving methods have so far focused on user clicks only, and lack support for more
sophisticated user satisfaction metrics as used in AB testing.

In this paper we present the first method for integrating user satisfaction metrics with interleaving. In particular, we
show how interleaved comparison methods can be extended to (1) directly match user signals and parameters of AB metrics,
and (2) how parameterized interleaving credit functions can be automatically calibrated to predict AB comparison
outcomes. We also develop a new method for estimating the relative sensitivity of interleaving and AB metrics, and show
that our interleaving credit functions achieve high agreement with AB metrics without sacrificing sensitivity. Our
results, using 38 large-scale online experiments encompassing over 3 billion clicks in a commercial web search setting,
demonstrate up to a 22% improvement in agreement with AB metrics (constituting over a 50% error reduction), while
maintaining interleaving sensitivity of one to two orders of magnitude above the AB tests. This paves the way towards
more sensitive and accurate online evaluation.

