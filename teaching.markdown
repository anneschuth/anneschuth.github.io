---
id: 7
title: Teaching
author: Anne
layout: page
permalink: /teaching/
---

## Students and Trainees

I (co-)supervised the following students and trainees. Many of them were interns, with some we published a paper. If you are
interested in internships, feel free to reach out!

{% assign sorted_students = site.students | sort: "years" | reverse %}
{% for student in sorted_students %}

### [{{ student.name }}]({{ student.url }}) ({{ student.years }})

{% if student.degree %}**Degree**: {{ student.degree }}{% if student.institution %}, {{ student.institution }}{% endif %}<br>
{% endif %}{% if student.host_company %}**Host company**: {{ student.host_company }}<br>
{% endif %}{% if student.topic %}**Topic**: {{ student.topic }}<br>
{% endif %}{% if student.co_supervisors %}**Co-supervisor{% if student.co_supervisors.size > 1 %}s{% endif %}**: {{ student.co_supervisors | join: ', ' }}<br>
{% endif %}
{% assign student_key = student.path | split: "/" | last | replace: ".md", "" %}
{% assign student_pubs = site.publications | where: "student", student_key %}
{% if student_pubs.size > 0 %}**Publications**:

{% for pub in student_pubs %}- {{ pub.author }}. [{{ pub.title }}]({{ pub.url }}). {% if pub.booktitle %}In {{ pub.booktitle }}, {% endif %}{% if pub.journal %}In {{ pub.journal }}, {% endif %}{{ pub.year }}.
{% endfor %}{% endif %}
{% endfor %}

## Courses and Tutorials

### LiLa 2016: ECIR 2016 Tutorial

**Year: 2016**

- [Living Labs for Online Evaluation: From Theory to Practice](/publications/schuth2016lila)

### Information Retrieval 2 (Curriculum Master Artificial Intelligence)

**Years: 2014-2015**

- Project on "Online Learning to Rank"

**Publications**:

- Anne Schuth and Robert-Jan Bruintjes and Fritjof Büttner and Joost van Doorn and Carla Groenland and Harrie
  Oosterhuis and Cong-Nguyen Tran and Bas Veeling and Jos van der Velde and Roger Wechsler and David Woudenberg and
  Maarten de
  Rijke. [Probabilistic Multileave for Online Retrieval Evaluation](/publications/schuth2015probabilistic.html). In
  Proceedings of SIGIR'15, 2015.

### Information Retrieval 1 (Curriculum Master Artificial Intelligence)

**Years: 2014-2015**

- Lecture on "Online Evaluation" (slides not available)
- Lecture on "Online Learning"
- Projects on "Multileaved Comparison Methods"

### Information Retrieval (Curriculum Master Artificial Intelligence)

**Year: 2013-2014**

- Lecture 7 on "Online Learning to Rank" (slides not available)

### WIP Profile Projects

**Year: 2012-2013**

- slides not available

### Advanced Information Retrieval

**Year: 2011-2012**

### Language Models

**Year: 2009-2010**
