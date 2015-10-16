---
layout: base
---

{% for lemma in site.lemmas %}
  <h2>{{ lemma.title }}</h2>
{% endfor %}