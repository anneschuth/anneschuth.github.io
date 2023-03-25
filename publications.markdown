---
layout: page
title: Publications
permalink: /publications/
---

I have published over 30 peer-reviewed scholarly articles; these include full papers at major information retrieval
venues such as ECIR, CIKM, WSDM, and SIGIR with acceptance rates as low as 10%. According to Google Scholar, my articles
have received over 1.2k citations; my h-index is 20.

See also my publication profiles at [google scholar](http://scholar.google.nl/citations?user=Y3ahb_wAAAAJ&hl=en)
and [dblp](http://www.dblp.org/search/index.php#query=author:anne_schuth:).

{% assign publications = site.publications | sort: "date" | reverse %}
{% for pub in publications %}
{% assign currentdate = pub.year %}
{% if currentdate != date %}

## {{currentdate}}

{% assign date = currentdate %}
{% endif %}
*{{ pub.author }}. [{{ pub.title }}]({{ pub.url }}) {% if pub.booktitle %}In {{ pub.booktitle }}, {% endif %}{% if
pub.journal %}In {{ pub.journal }}, {% endif %}{{ pub.year}}.*
{% endfor %}
