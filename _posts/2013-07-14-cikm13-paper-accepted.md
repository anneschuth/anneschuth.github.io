---
title: "CIKM'13 paper accepted"
date: '2013-07-14T18:46:25+02:00'
author: Anne
layout: post
lang: en
permalink: /cikm13-paper-accepted/
categories:
    - Paper
    - Publication
tags:
    - '2013'
    - cikm
    - conference
---

Our paper [Evaluating Aggregated Search Using Interleaving](/publications/chuklin2013evaluating)
with [Aleksandr Chuklin](http://ch.linkedin.com/in/chuklin), [Katja Hofmann](http://khofm.wordpress.com/), [Pavel Serdyukov](http://ru.linkedin.com/in/pavelserdyukov)
and [Maarten de Rijke](http://staff.science.uva.nl/~mdr/) was accepted for publication as full paper
in [CIKM'13](http://www.cikm2013.org/). I will present the paper on Tuesday afternoon.

### Abstract

A result page of a modern web search engine is often much more complicated than a simple list of “ten blue links”. In
particular, a search engine may combine results from different sources (e.g., Web, News, and Images), and display these
as grouped results to provide a better user experience. Such a system is called an aggregated or federated search
system.

Because search engines evolve over time, their results need to be constantly evaluated. One of the most efficient and
widely used evaluation methods, interleaving, however cannot be directly applied to aggregated search systems, as it
ignores the need to group results originating from the same source (vertical results).

We propose an interleaving algorithm that allows comparisons of search engine result pages containing grouped vertical
documents. We compare our algorithm to existing interleaving algorithms and other evaluation methods (such as
A/B-testing), both on real-life click log data and in simulation experiments. We find that our algorithm allows us to
perform unbiased and accurate interleaved comparisons that are comparable to conventional evaluation techniques. We also
show that our interleaving algorithm produces a ranking that does not substantially alter the user experience, while
being sensitive to changes in both vertical result block and the non-vertical document rankings. All this makes our
proposed interleaving algorithm an essential tool for comparing IR systems with complex aggregated pages.
