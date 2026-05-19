---
title: Software
author: Anne
layout: page
permalink: /software/
---

{% assign projects = site.software | sort: "order" %}
{% for project in projects %}

## {{ project.title }} {#{{ project.slug }}}

{{ project.content }}
{% if project.publications and project.publications.size > 0 %}
{%- assign resolved_pubs = '' | split: '' -%}
{%- for key in project.publications -%}
  {%- assign pub = site.publications | where: "key", key | first -%}
  {%- unless pub -%}
    {%- assign pub_filename = key | append: ".md" -%}
    {%- for p in site.publications -%}
      {%- assign p_filename = p.path | split: "/" | last -%}
      {%- if p_filename == pub_filename -%}{%- assign pub = p -%}{%- break -%}{%- endif -%}
    {%- endfor -%}
  {%- endunless -%}
  {%- if pub -%}{%- assign resolved_pubs = resolved_pubs | push: pub -%}{%- endif -%}
{%- endfor -%}
{% if resolved_pubs.size > 0 %}
**Related publications:**

{% assign sorted_pubs = resolved_pubs | sort: "date" | reverse %}
{% for pub in sorted_pubs %}- [{{ pub.title }}]({{ pub.url }}). _{{ pub.author | replace: "Anne Schuth", "**Anne Schuth**" }}._{% if pub.booktitle %} In {{ pub.booktitle }},{% endif %}{% if pub.journal %} In {{ pub.journal }},{% endif %} {{ pub.year }}.
{% endfor %}
{%- assign related_talks = '' | split: '' -%}
{%- for talk in site.talks -%}
  {%- if talk.publication_url -%}
    {%- assign talk_pub_key = talk.publication_url | replace: '/publications/', '' | replace: '.html', '' | replace: '/', '' -%}
    {%- for pub in resolved_pubs -%}
      {%- assign pub_key = pub.url | replace: '/publications/', '' | replace: '.html', '' | replace: '/', '' -%}
      {%- if talk_pub_key == pub_key -%}{%- assign related_talks = related_talks | push: talk -%}{%- break -%}{%- endif -%}
    {%- endfor -%}
  {%- endif -%}
{%- endfor -%}
{% if related_talks.size > 0 %}
**Related talks:**

{% assign sorted_talks = related_talks | sort: "date" | reverse %}
{% for talk in sorted_talks %}- [{{ talk.title }}]({{ talk.url }}).{% if talk.venue %} _{{ talk.venue }}_.{% endif %}{% if talk.location %} {{ talk.location }}.{% endif %} _{{ talk.date | date: "%b %-d, %Y" }}_.
{% endfor %}
{% endif %}
{% endif %}
{% endif %}
{% endfor %}
