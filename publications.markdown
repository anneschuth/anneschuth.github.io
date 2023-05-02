---
layout: page
title: Publications
permalink: /publications/
---

I have published over 30 peer-reviewed scholarly articles; these include full papers at major information retrieval
venues such as ECIR, CIKM, WSDM, and SIGIR with acceptance rates as low as 10%. According to Google Scholar, my articles
have received over 1.3k citations; my h-index is 20.

See also my publication profiles at [google scholar](http://scholar.google.nl/citations?user=Y3ahb_wAAAAJ&hl=en)
and [dblp](http://www.dblp.org/search/index.php#query=author:anne_schuth:).

{% assign publications = site.publications | sort: "date" | reverse %}
{% for pub in publications %}
{% assign currentdate = pub.year %}
{% if currentdate != date %}

## {{currentdate}}

{% assign date = currentdate %}
{% endif %}
![{{pub.shield}}](https://img.shields.io/badge/{{pub.shield}}) {{ pub.author }}. [{{ pub.title }}.]({{ pub.url }}) {% if pub.booktitle %}In {{ pub.booktitle }}, {% endif %}{% if
pub.journal %}In {{ pub.journal }}, {% endif %}{{ pub.year}}. {% if pub.pdf %} [<i class="fa fa-file-pdf-o"></i>]({{pub.pdf}}){% endif %} {% if pub.repo %} [<i class="fa fa-github"></i>]({{pub.repo}}){% endif %}{% if pub.bitbucket %} [<i class="fa fa-bitbucket"></i>]({{pub.bitbucket}}){% endif %} {% if pub.arxiv %}[<i class="fa fa-archive"></i>](https://arxiv.org/abs/{{pub.arxiv}}){% endif %}

{% endfor %}
