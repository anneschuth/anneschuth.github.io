---
title: Software
author: Anne
layout: page
permalink: /software/
---

## PoC Machine Law

A proof-of-concept project developed for the Dutch Ministry of the Interior that explores the transformation of legal
texts into executable code. This innovative system converts complex legislation into machine-readable specifications
that can be processed directly by computer systems. By formalizing legal rules as code, the project aims to improve
transparency, reduce interpretation errors, and enable automated compliance checking.

The implementation supports multiple domains like social security, taxation, and administrative law, with a built-in
engine to execute, validate, and test legal specifications. The technology helps bridge the gap between legal experts
and software developers by providing a common language for expressing legal requirements.

The source code is [available on GitHub](https://github.com/MinBZK/poc-machine-law).

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
Several of my publications relate to Living Labs.

## Lerot: an Online Learning to Rank Framework

Lerot is a framework, designed to run experiments on online learning to rank methods for information retrieval. It has
mainly been developed by [Katja Hofmann](http://khofm.wordpress.com/) and Anne Schuth.  
The source code of Lerot is [available from bitbucket](https://bitbucket.org/ilps/lerot).  
A paper describing Lerot is published in the Living Labs Workshop at CIKM'13:

- A. Schuth, K. Hofmann, S. Whiteson, M. de
  Rijke. [Lerot: an Online Learning to Rank Framework](/publications/schuth-lerot-2013)
  In Living Labs for Information Retrieval Evaluation workshop at CIKM'13, 2013 
