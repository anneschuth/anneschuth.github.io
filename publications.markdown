---
layout: page
title: Publications
permalink: /publications/
---

{: .intro}
I have published {{ site.publications | size }} peer-reviewed scholarly articles; these include full papers at major information retrieval venues such as ECIR, CIKM, WSDM, and SIGIR with acceptance rates as low as 10%. According to [Google Scholar](https://scholar.google.com/citations?user=Y3ahb_wAAAAJ&hl=en), my articles have received {{ site.data.scholar_stats.total_citations }} citations; my h-index is {{ site.data.scholar_stats.h_index }}.

See also my publication profiles at [google scholar](http://scholar.google.nl/citations?user=Y3ahb_wAAAAJ&hl=en)
and [dblp](http://www.dblp.org/search/index.php#query=author:anne_schuth:).

{% assign publications = site.publications | sort: "date" | reverse %}
{% for pub in publications %}
{% assign currentdate = pub.year %}
{% if currentdate != date %}

## {{currentdate}}

{% assign date = currentdate %}
{% endif %}

{%- comment -%}
Find talks that reference this publication
{%- endcomment -%}
{%- assign related_talks = site.talks | where_exp: "talk", "talk.publication_url == pub.url" -%}
{%- if related_talks.size == 0 -%}
  {%- comment -%}Try alternative matching patterns{%- endcomment -%}
  {%- assign pub_path = pub.url | append: "/" -%}
  {%- assign related_talks = site.talks | where_exp: "talk", "talk.publication_url == pub_path" -%}
{%- endif -%}
{%- if related_talks.size == 0 and pub.key -%}
  {%- comment -%}Try matching by key{%- endcomment -%}
  {%- assign pub_key_path = "/publications/" | append: pub.key -%}
  {%- assign related_talks = site.talks | where_exp: "talk", "talk.publication_url == pub_key_path" -%}
{%- endif -%}
{%- if related_talks.size == 0 -%}
  {%- comment -%}Try matching by filename{%- endcomment -%}
  {%- assign pub_filename = pub.path | split: "/" | last | replace: ".md", "" -%}
  {%- assign pub_filename_path = "/publications/" | append: pub_filename -%}
  {%- assign related_talks = site.talks | where_exp: "talk", "talk.publication_url == pub_filename_path" -%}
{%- endif -%}

{%- comment -%}Get the most recent talk if multiple found{%- endcomment -%}
{%- assign first_talk = related_talks | sort: "date" | reverse | first -%}

![{{pub.shield}}](https://img.shields.io/badge/{{pub.shield}}) {{ pub.author | replace: "Anne Schuth", "**Anne Schuth**" }}. [{{ pub.title }}.]({{ pub.url }}) {% if pub.booktitle %}In {{ pub.booktitle }}, {% endif %}{% if
pub.journal %}In {{ pub.journal }}, {% endif %}{{ pub.year}}.{% if
pub.pdf %}&nbsp;[<i class="fa fa-file-pdf-o"></i>]({{pub.pdf}}){% endif %}{% if
pub.repo %}&nbsp;[<i class="fa fa-github"></i>]({{pub.repo}}){% endif %}{% if
pub.bitbucket %}&nbsp;[<i class="fa fa-bitbucket"></i>]({{pub.bitbucket}}){% endif %}{% if
pub.arxiv %}&nbsp;[<i class="fa fa-archive"></i>](https://arxiv.org/abs/{{pub.arxiv}}){% endif %}{% if
pub.doi %}&nbsp;[<i class="fa fa-link"></i>](https://doi.org/{{pub.doi}}){% endif %}{% if
pub.scholar_url %}&nbsp;[<i class="fa fa-graduation-cap"></i>]({{pub.scholar_url}}){% endif %}{% if
first_talk %}&nbsp;[<i class="fa fa-microphone"></i>]({{first_talk.url}}){% endif %}{% if pub.citations and pub.citations > 0 and pub.scholar_url %}&nbsp;<span style="color:#888;font-size:0.9em;"><i class="fa fa-quote-left"></i>&nbsp;<a href="{{ pub.scholar_url }}" style="color:#888;text-decoration:none;">{{ pub.citations }}</a></span>{% endif %}
{% endfor %}
