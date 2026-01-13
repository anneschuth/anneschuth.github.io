---
title: Software
author: Anne
layout: page
permalink: /software/
---

## Claude-threads

Claude-threads brings Claude Code capabilities directly into team chat platforms like Mattermost and Slack. The bot enables collaborative AI pair programming by streaming Claude's responses live to chat threads, allowing teams to work together on coding tasks in real-time. Each conversation thread maintains its own isolated Claude session with features like interactive approvals through emoji reactions, git integration with worktrees, and support for image analysis. As the tagline suggests, it's "screen-sharing for AI pair programming, but everyone can type."

The source code is [available on GitHub](https://github.com/anneschuth/claude-threads).

## peerpressure

Peerpressure is a social digital detox app that uses peer accountability to help users stay focused and avoid digital distractions. When you join a focus session with friends, they can see when you try to break focus - turning social pressure into your productivity superpower. The app blocks distracting apps in real-time, requires peer approval for emergency unlocks, and tracks focus streaks and session history. By making productivity a collaborative effort, peerpressure helps users break free from digital distractions together.

Learn more at [peerpressure.social](https://peerpressure.social).

## RegelRecht

RegelRecht is an exploration by the Dutch Ministry of the Interior (Bureau Architectuur) into machine-executable
legislation. The project investigates how we can achieve transparent, unambiguous, and consistent execution of laws -
enabling everyone to understand how decisions are made.

This initiative explores whether laws can be written as directly executable code, eliminating the gap between
legislation and implementation. By creating machine-readable legal specifications, RegelRecht aims to:

- Provide one single source of truth for legal rules that all parties use
- Enable full transparency and traceability of government decisions
- Test new legislation before implementation to detect conflicts and inconsistencies
- Reduce interpretation differences across government organizations

The ecosystem includes NRML (Normalized Rule Model Language) as a JSON-based format for machine-executable laws,
execution engines in multiple programming languages, an AI-powered converter for existing analog law, a visual law
editor, and simulation environments for testing legislative impact.

Learn more at [minbzk.github.io/regelrecht](https://minbzk.github.io/regelrecht/) or explore the source code
[on GitHub](https://github.com/MinBZK/poc-machine-law).

## Algorithm Management Toolkit (AMT)

A comprehensive platform for the governance and oversight of algorithmic systems within organizations. Developed for the
Dutch government, AMT provides a structured approach to documenting, testing, and managing both AI and non-AI algorithms
used in public services and decision-making processes.

The toolkit features a bookkeeping system for algorithmic applications, technical validation tools, ethical assessment
frameworks, and transparency reporting capabilities. It helps organizations maintain proper documentation, ensure
regulatory compliance, and implement responsible AI practices. AMT represents an important step toward algorithmic
accountability in governance and public service delivery.

The source code is [available on GitHub](https://github.com/MinBZK/amt).

## Living Labs

The Living Labs for IR Evaluation (LL4IR) is a new evaluation paradigm. I implemented an API for participants (
researchers) and sites (search engines) that take part in this Living Lab (which is also run
as a CLEF lab). The API allows participants (researchers) to evaluate their ranking systems on real users of real
sites (search engines). On the flip site, it allows sites (search engines) to benefit from the knowledge of the research
community.

The LL4IR API can be used by researchers to perform several actions such as obtaining queries, documents and feedback
and to update runs. The API is RESTful, that is, everything is implemented as HTTP request, and we use the request types
GET, PUT and DELETE.

The source code is [available from bitbucket](https://bitbucket.org/living-labs/ll-api).

It has mainly been developed by Anne Schuth and [Krisztian Balog](http://krisztianbalog.com/).

**Related publications:**

- [Extended Overview of the Living Labs for Information Retrieval Evaluation (LL4IR) CLEF Lab 2015](/publications/schuth2015extended.html)
- [OpenSearch: Integrating and Contextualizing Search](/publications/schuth2015opensearch.html)
- [Overview of the CLEF LL4IR 2015 Lab](/publications/schuth2015overview.html)
- [Living Labs for Online Evaluation: From Theory to Practice](/talks/living-labs-for-online-evaluation-from-theory-to-p-2016.html)
- [TREC OpenSearch Track](/talks/trec-opensearch-2015.html)

## Lerot: an Online Learning to Rank Framework

Lerot is a framework, designed to run experiments on online learning to rank methods for information retrieval. It has
mainly been developed by [Katja Hofmann](http://khofm.wordpress.com/) and Anne Schuth.
The source code of Lerot is [available from bitbucket](https://bitbucket.org/ilps/lerot).
A paper describing Lerot is published in the Living Labs Workshop at CIKM'13:

- A. Schuth, K. Hofmann, S. Whiteson, M. de
  Rijke. [Lerot: an Online Learning to Rank Framework](/publications/schuth2013lerot.html)
  In Living Labs for Information Retrieval Evaluation workshop at CIKM'13, 2013
