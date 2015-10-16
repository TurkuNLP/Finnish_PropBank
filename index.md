---
layout: base
---

{% for lemma in site.lemmas %}
## [{{lemma.lemma}}](lemmas/{{lemma.lemma}}.html)
{% endfor %}
