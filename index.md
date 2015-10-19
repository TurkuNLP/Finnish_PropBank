---
layout: base
---

<table id="lemmatable" class="display">
<thead>
<tr>
<th>Lemma</th>
</tr>
</thead>
<tbody>
{% for lemma in site.lemmas %}
<tr><td><a href="lemmas/{{lemma.lemma}}.html">{{lemma.lemma}}</a></td></tr>
{% endfor %}
</tbody>
</table>

<script type="text/javascript">
$(document).ready( function () {
    $('#lemmatable').DataTable();
} );
</script>