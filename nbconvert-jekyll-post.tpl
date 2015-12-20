{# Based on: http://mcwitt.github.io/2015/04/29/jekyll_blogging_with_ipython3/ #}
{%- extends 'markdown.tpl' -%}
{%- block header -%}
---
layout: post
title: "{{resources['metadata']['title']}}"
date: {{resources['metadata']['date']}}
categories: notebooks
---
{% endblock header %}

{% block any_cell scoped %}
{{ super () }}
{% endblock any_cell %}

{%- block input -%}
{{ '{% highlight python %}' }}
{{ cell.source }}
{{ '{% endhighlight %}' }}
{%- endblock input -%}