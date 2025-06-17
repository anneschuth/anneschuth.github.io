---
title: "TREC OpenSearch proposal accepted"
date: '2015-10-12T09:08:52+02:00'
author: Anne
layout: post
permalink: /trec-opensearch-proposal-accepted/

---
Our TREC proposal for OpenSearch has been accepted! TREC OpenSearch will be run in the same vein
as CLEF LL4IR and use the same infrastructure.

**Related work:** This builds on our [Living Labs research](/publications/schuth2015opensearch.html) and the [LL4IR CLEF overview](/publications/schuth2015extended.html). See also the [OpenSearch talk](/talks/opensearch-2015.html) and [TREC OpenSearch presentation](/talks/trec-opensearch-2015.html).

> OpenSearch is a new evaluation paradigm for IR. The experimentation platform *is* an existing search engine.
> Researchers have the opportunity to replace components of this search engine and evaluate these components using
> interactions with real, unsuspecting users of this search engine.

Organizers

- Anne Schuth, University of Amsterdam, The Netherlands
- [Krisztian Balog](https://krisztianbalog.com/), University of Stavanger, Norway

Read more on the [TREC OpenSearch website](http://trec-open-search.org/).

## Evaluation Setup

TREC OpenSearch evaluates rankings provided by participants in the context of an actual search engine, by serving
precomputed runs, for a given set of queries, to the users that enter one of these queries in the real-life search
engine.

The track operates as follows. A set Q of queries is taken from the logs of a real, existing, search engine. These
queries are chosen such that they appear frequently enough, making it likely that they will be issued again in the near
future by users of this search engine. This selection of queries is a crucial ingredient of our approach and we
discussed this in more detail in earlier work. Additionally, for each query, the search engine prepares a set of
candidate documents and some historical interaction data for each document. TREC OpenSearch then requires an
infrastructure, an API, that allows the search engine to share queries, documents and interactions with the
participants. Once the search engine uploads the data to the API, it can be downloaded by participants. This way
participants are provided with very much the typical TREC-style collection, consisting of queries and documents and
additionally historical interactions. Queries are strings and documents are represented as JSON documents with all the
fields common in literature search (e.g., author, title, abstract, full text, etc).

Participants are expected to produce their runs, as they normally would, and upload these through the API. When an
unsuspecting, real user then issues a query against the search engine, the search engine will ask the API to provide
them with a run for that query. The API then selects uniformly randomly from among the runs that have already been
upload by participants. This run is then returned to the search engine. The search engine interleaves the run with its
production system and shows this to the user. The user may or may not interact with this ranking. When there is an
interaction, the search engine sends this back to the API. And the API then makes it available to the participant. The
participant can then (or at any moment for that matter) choose to update their ranking.

A subset of queries are designated as test queries, all other queries are considered train queries. For train queries,
the procedure is exactly as described above. The test queries are treated largely the same as the train queries,
however, there are some crucial differences. For test queries, participants never receive individual impressions of
their run nor individual interactions of users with this run. Only aggregations of interleaving outcomes are reported
for test queries. Moreover, during a designated test period, participants can not update the runs for test queries. This
allows TREC OpenSearch to compare stable runs (and their underlying systems) to each other. Moreover, since no
individual feedback is provided for test queries, participants can not optimize their systems for test queries, only for
train queries. We propose this procedure to be able to learn how participants' systems would generalize to unseen
queries.

## Limitations

The above setup has limitations. These include that only a selection of queries is considered (all queries are
reasonably frequent, so no long tail) and there is no contextual information available about the current user (meaning
that personalization is not possible). On the positive side, this approach avoids the privacy concerns and lowers the
barrier to entry: participants prepare their runs offline and partake in an online experiment, without having to build
and maintain a live service.

[![trecopensearch-darker](/assets/trecopensearch-darker.png)](/assets/trecopensearch-darker.png?ssl=1)
