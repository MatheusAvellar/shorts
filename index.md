---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults
layout: default
title: Avellar's Shorts
lang: "en"
permalink: /
---
<div class="home">
  <h1>Avellar's Shorts</h1>
  <p>
    A personal URL shortener. All short URLs are permanent, and will be archived
    on the <a href="https://web.archive.org/">Wayback Machine</a> for
    future-proofing.
  </p>
  {%- assign len = site.posts | size -%}
  {%- if len < 2 -%}
  <p>There is currently <strong>{{ len }}</strong> registered URL:</p>
  {%- else -%}
  <p>There are currently <strong>{{ len }}</strong> registered URLs:</p>
  {%- endif -%}
  <ul>
  {% for post in site.posts %}
    <li>
      <h2>{{ post.title }}</h2>
      <p>
        <a class="short-link" href="{{ post.url }}">s.avl.la/{{ post.slug }}</a>
      </p>
    </li>
  {% endfor %}
  </ul>
</div>