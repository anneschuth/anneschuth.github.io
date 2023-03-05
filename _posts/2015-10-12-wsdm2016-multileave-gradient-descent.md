---
id: 511
title: 'WSDM2016 paper on &#8220;Multileave Gradient Descent for Fast Online Learning to Rank&#8221; accepted'
date: '2015-10-12T21:43:50+02:00'
author: Anne
layout: post
guid: 'http://www.anneschuth.nl/?p=511'
permalink: /wsdm2016-multileave-gradient-descent/
jetpack-post-views:
    - '173'
jetpack-post-views-Day:
    - '1'
jetpack-post-views-Week:
    - '1'
jetpack-post-views-Month:
    - '1'
jetpack-post-views-Year:
    - '2'
categories:
    - Uncategorized
---

Our paper “[Multileave Gradient Descent for Fast Online Learning to Rank](https://www.anneschuth.nl/wp-content/uploads/wsdm2016-multileave-gradient-descent.pdf)” with Anne Schuth, Harrie Oosterhuis, [Shimon Whiteson](https://www.cs.ox.ac.uk/people/shimon.whiteson/), and [Maarten de Rijke](https://staff.fnwi.uva.nl/m.derijke/) was accepted at [WSDM2016](http://www.wsdm-conference.org/2016/).

We will present a [one page abstract at DIR](https://www.anneschuth.nl/wp-content/uploads/dir2015-multileave-gradient-descent.pdf).  
  
Modern search systems are based on dozens or even hundreds of ranking features. The *dueling bandit gradient descent* (DBGD) algorithm has been shown to effectively learn combinations of these features solely from user interactions. DBGD explores the search space by comparing a possibly improved ranker to the current production ranker. To this end, it uses interleaved comparison methods, which can infer with high sensitivity a preference between two rankings based only on interaction data. A limiting factor is that it can compare only to a single exploratory ranker.

We propose an online learning to rank algorithm called *multileave gradient descent* (MGD) that extends DBGD to learn from so-called multileaved comparison methods that can compare a set of rankings instead of merely a pair. We show experimentally that MGD allows for better selection of candidates than DBGD without the need for more comparisons involving users. An important implication of our results is that orders of magnitude less user interaction data is required to find good rankers when multileaved comparisons are used within online learning to rank. Hence, fewer users need to be exposed to possibly inferior rankers and our method allows search engines to adapt more quickly to changes in user preferences.