---
id: 379
title: "ACM TOIS paper 'A comparative analysis of interleaving methods for aggregated search' online"
date: '2015-02-06T12:12:59+01:00'
author: Anne
layout: post
permalink: /acm-tois-paper-comparative-analysis-interleaving-methods-aggregated-search-online/
categories:
    - Uncategorized
---

Our ACM Transactions on Information Systems paper called [“A comparative analysis of interleaving methods for aggregated search”](/assets/2015/02/tois2015-interleaving-for-aggregated-search.pdf) by [Aleksandr Chuklin](https://www.linkedin.com/in/chuklin), Anne Schuth, [Ke Zhou](http://www.dcs.gla.ac.uk/~zhouke/) and [Maarten de Rijke](https://staff.fnwi.uva.nl/m.derijke/) is available now.

A result page of a modern search engine often goes beyond a simple list of “ten blue links.’ Many specific user needs (e.g., News, Image, Video) are addressed by so-called aggregated or vertical search solutions: specially presented documents, often retrieved from specific sources, that stand out from the regular organic web search results. When it comes to evaluating ranking systems, such complex result layouts raise their own challenges. This is especially true for so-called interleaving methods that have arisen as an important type of online evaluation: by mixing results from two different result pages interleaving can easily break the desired web layout in which vertical documents are grouped together, and hence hurt the user experience.

We conduct an analysis of different interleaving methods as applied to aggregated search engine result pages. Apart from conventional interleaving methods, we propose two vertical-aware methods: one derived from the widely used Team-Draft Interleaving method by adjusting it in such a way that it respects vertical document groupings, and another based on the recently introduced Optimized Interleaving framework. We show that our proposed methods are better at preserving the user experience than existing interleaving methods while still performing well as a tool for comparing ranking systems. For evaluating our proposed vertical-aware interleaving methods we use real world click data as well as simulated clicks and simulated ranking systems.