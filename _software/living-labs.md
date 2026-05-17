---
title: Living Labs
slug: living-labs
order: 5
repo: https://github.com/living-labs/ll-api
summary: RESTful API for the Living Labs for IR Evaluation (LL4IR / CLEF lab) letting researchers evaluate rankers on real users of real search engines.
---
The Living Labs for IR Evaluation (LL4IR) is a new evaluation paradigm. I implemented an API for participants (
researchers) and sites (search engines) that take part in this Living Lab (which is also run
as a CLEF lab). The API allows participants (researchers) to evaluate their ranking systems on real users of real
sites (search engines). On the flip site, it allows sites (search engines) to benefit from the knowledge of the research
community.

The LL4IR API can be used by researchers to perform several actions such as obtaining queries, documents and feedback
and to update runs. The API is RESTful, that is, everything is implemented as HTTP request, and we use the request types
GET, PUT and DELETE.

The source code is [available on GitHub](https://github.com/living-labs/ll-api).

It has mainly been developed by Anne Schuth and [Krisztian Balog](http://krisztianbalog.com/).

**Related publications:**

- [Extended Overview of the Living Labs for Information Retrieval Evaluation (LL4IR) CLEF Lab 2015](/publications/schuth2015extended.html)
- [OpenSearch: Integrating and Contextualizing Search](/publications/schuth2015opensearch.html)
- [Overview of the CLEF LL4IR 2015 Lab](/publications/schuth2015overview.html)
- [Living Labs for Online Evaluation: From Theory to Practice](/talks/living-labs-for-online-evaluation-from-theory-to-p-2016.html)
- [TREC OpenSearch Track](/talks/trec-opensearch-2015.html)
