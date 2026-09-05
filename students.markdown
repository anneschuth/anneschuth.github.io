---
title: Students
author: Anne
layout: page
permalink: /students/
---

I (co-)supervised the following students and trainees. Many of them were interns, with some we published a paper. If you are
interested in internships, feel free to reach out! For the courses and tutorials I taught, see [Teaching](/teaching/).

{% assign sorted_students = site.students | sort: "years" | reverse %}
{% for student in sorted_students %}

### [{{ student.name }}]({{ student.url }}) ({{ student.years }})

{% if student.degree %}**Degree**: {{ student.degree }}{% if student.institution %}, {{ student.institution }}{% endif %}<br>
{% endif %}{% if student.host_organisation %}**Host organisation**: {{ student.host_organisation }}<br>
{% endif %}{% if student.topic %}**Topic**: {% if student.topic_url %}[{{ student.topic }}]({{ student.topic_url }}){% else %}{{ student.topic }}{% endif %}<br>
{% endif %}{% if student.co_supervisors %}**Co-supervisor{% if student.co_supervisors.size > 1 %}s{% endif %}**: {% for person in student.co_supervisors %}{% assign person_url = site.data.people[person] %}{% if person_url %}[{{ person }}]({{ person_url }}){% else %}{{ person }}{% endif %}{% unless forloop.last %}, {% endunless %}{% endfor %}<br>
{% endif %}
{% assign student_key = student.path | split: "/" | last | replace: ".md", "" %}
{% assign student_pubs = site.publications | where: "student", student_key %}
{% if student_pubs.size > 0 %}**Publications**:

{% for pub in student_pubs %}- {{ pub.author }}. [{{ pub.title }}]({{ pub.url }}). {% if pub.booktitle %}In {{ pub.booktitle }}, {% endif %}{% if pub.journal %}In {{ pub.journal }}, {% endif %}{{ pub.year }}.
{% endfor %}{% endif %}
{% endfor %}
