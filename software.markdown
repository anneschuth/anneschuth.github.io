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
{% endfor %}
