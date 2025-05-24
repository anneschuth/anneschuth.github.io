---
title: Talks
author: Anne
layout: page
permalink: /talks/
---

This is an exhaustive (I think) list of talks I gave and posters I presented since obtaining my master's degree. Please let me know if something (a slide deck or poster, for instance) is missing. Please feel free to use my slides (with a reference).

{% assign talks = site.talks | sort: "date" | reverse %}
{% assign grouped_talks = talks | group_by: "year" %}
{% for year_group in grouped_talks %}

## {{ year_group.name }}

{% assign year_talks = year_group.items | sort: "date" | reverse %}
{% for talk in year_talks %}
{%- assign links = '' -%}
{%- if talk.slides_url -%}
  {%- assign links = links | append: '[<i class="fa fa-file-powerpoint-o"></i>](' | append: talk.slides_url | append: ')' -%}
{%- endif -%}
{%- if talk.video_url -%}
  {%- if links != '' -%}{%- assign links = links | append: '&nbsp;' -%}{%- endif -%}
  {%- assign links = links | append: '[<i class="fa fa-video-camera"></i>](' | append: talk.video_url | append: ')' -%}
{%- endif -%}
{%- if talk.event_url -%}
  {%- if links != '' -%}{%- assign links = links | append: '&nbsp;' -%}{%- endif -%}
  {%- assign links = links | append: '[<i class="fa fa-calendar"></i>](' | append: talk.event_url | append: ')' -%}
{%- endif -%}
{%- if talk.meetup_url -%}
  {%- if links != '' -%}{%- assign links = links | append: '&nbsp;' -%}{%- endif -%}
  {%- assign links = links | append: '[<i class="fa fa-users"></i>](' | append: talk.meetup_url | append: ')' -%}
{%- endif -%}
{%- if talk.website_url -%}
  {%- if links != '' -%}{%- assign links = links | append: '&nbsp;' -%}{%- endif -%}
  {%- assign links = links | append: '[<i class="fa fa-globe"></i>](' | append: talk.website_url | append: ')' -%}
{%- endif -%}
{%- if talk.poster_url -%}
  {%- if links != '' -%}{%- assign links = links | append: '&nbsp;' -%}{%- endif -%}
  {%- assign links = links | append: '[<i class="fa fa-file-image-o"></i>](' | append: talk.poster_url | append: ')' -%}
{%- endif -%}
{%- if talk.publication_url -%}
  {%- if links != '' -%}{%- assign links = links | append: '&nbsp;' -%}{%- endif -%}
  {%- assign links = links | append: '[<i class="fa fa-file-text-o"></i>](' | append: talk.publication_url | append: ')' -%}
{%- endif -%}
{%- if talk.thesis_url -%}
  {%- if links != '' -%}{%- assign links = links | append: '&nbsp;' -%}{%- endif -%}
  {%- assign links = links | append: '[<i class="fa fa-graduation-cap"></i>](' | append: talk.thesis_url | append: ')' -%}
{%- endif -%}

{% if talk.shield %}![{{talk.shield}}](https://img.shields.io/badge/{{talk.shield}}) {% endif %}[{{ talk.title }}]({{ talk.url }}).{% if talk.venue %} _{{ talk.venue }}_{% endif %}{% if talk.location %}. {{ talk.location }}{% endif %}. _{{ talk.date | date: "%B %d" }}_.{% if links != '' %} {{ links }}{% endif %}

{% endfor %}
{% endfor %}
