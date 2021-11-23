---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults
layout: default
title: Home
lang: "en"
permalink: /
---
<div class="home">
  <h1>Shorts</h1>
  <p>
    A personal URL shortener.
  </p>
  <p>
    There are <strong>{{ site.posts | size }}</strong> registered URLs.
  </p>
  <ul>
  {% for post in site.posts %}
    <li>
      <a href="{{ post.url }}">{{ post.title }}</a>
    </li>
  {% endfor %}
  </ul>
</div>