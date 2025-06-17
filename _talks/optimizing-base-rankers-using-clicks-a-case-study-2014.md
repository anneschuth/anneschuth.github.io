---
title: 'Optimizing Base Rankers Using Clicks: A Case Study using BM25'
date: '2014-04-14'
year: 2014
layout: talk
key: optimizing-base-rankers-using-clicks-a-case-study-2014
redirect_from: /talks/optimizing-base-rankers-using-clicks-a-case-study--2014.html
shield: conference-orange
venue: ECIR'14
location: Amsterdam, The Netherlands
slides_url: /assets/ecir-2014-bm25.pdf
publication_url: /publications/schuth2014
---

## Summary

This work investigates optimizing the parameters of base ranking functions like BM25 using user click data, rather than just learning linear combinations of fixed features as in traditional learning-to-rank approaches. Using online evaluation methods including Dueling Bandit Gradient Descent and Relative Upper Confidence Bound, the authors demonstrate that optimizing BM25's k1 and b parameters on the Yahoo Learning to Rank dataset improves NDCG@10 from 0.765 to 0.776, nearly matching the performance of more complex learning-to-rank methods (0.780) while being computationally cheaper. The research shows that simple parameter optimization of individual base rankers can yield significant improvements and may be more practical than complex feature combination approaches.
