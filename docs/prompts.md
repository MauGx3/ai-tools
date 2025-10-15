---
layout: default
title: Prompts Collection
---

## Prompts Collection

This section contains curated AI prompts organized by category. Each prompt includes detailed metadata, usage instructions, and examples.

## Categories

### 🚀 Coding Prompts
Prompts for software development, debugging, and code review.

{% assign coding_prompts = site.prompts | where: "category", "coding" %}
{% if coding_prompts.size > 0 %}
<ul>
{% for prompt in coding_prompts %}
  <li><a href="{{ prompt.url | relative_url }}">{{ prompt.title }}</a> - {{ prompt.description | default: "No description available" }}</li>
{% endfor %}
</ul>
{% else %}
<p><em>No coding prompts available yet. <a href="#contributing">Contribute some!</a></em></p>
{% endif %}

### ✍️ Writing Prompts
Prompts for content creation, editing, and documentation.

{% assign writing_prompts = site.prompts | where: "category", "writing" %}
{% if writing_prompts.size > 0 %}
<ul>
{% for prompt in writing_prompts %}
  <li><a href="{{ prompt.url | relative_url }}">{{ prompt.title }}</a> - {{ prompt.description | default: "No description available" }}</li>
{% endfor %}
</ul>
{% else %}
<p><em>No writing prompts available yet. <a href="#contributing">Contribute some!</a></em></p>
{% endif %}

### 📊 Analysis Prompts
Prompts for data analysis, research, and evaluation.

{% assign analysis_prompts = site.prompts | where: "category", "analysis" %}
{% if analysis_prompts.size > 0 %}
<ul>
{% for prompt in analysis_prompts %}
  <li><a href="{{ prompt.url | relative_url }}">{{ prompt.title }}</a> - {{ prompt.description | default: "No description available" }}</li>
{% endfor %}
</ul>
{% else %}
<p><em>No analysis prompts available yet. <a href="#contributing">Contribute some!</a></em></p>
{% endif %}

### 🎨 Creative Prompts
Prompts for brainstorming, ideation, and creative writing.

{% assign creative_prompts = site.prompts | where: "category", "creative" %}
{% if creative_prompts.size > 0 %}
<ul>
{% for prompt in creative_prompts %}
  <li><a href="{{ prompt.url | relative_url }}">{{ prompt.title }}</a> - {{ prompt.description | default: "No description available" }}</li>
{% endfor %}
</ul>
{% else %}
<p><em>No creative prompts available yet. <a href="#contributing">Contribute some!</a></em></p>
{% endif %}

### ⚡ Productivity Prompts
Prompts for task management, planning, and optimization.

{% assign productivity_prompts = site.prompts | where: "category", "productivity" %}
{% if productivity_prompts.size > 0 %}
<ul>
{% for prompt in productivity_prompts %}
  <li><a href="{{ prompt.url | relative_url }}">{{ prompt.title }}</a> - {{ prompt.description | default: "No description available" }}</li>
{% endfor %}
</ul>
{% else %}
<p><em>No productivity prompts available yet. <a href="#contributing">Contribute some!</a></em></p>
{% endif %}

## All Prompts

{% assign all_prompts = site.prompts | sort: "title" %}
{% if all_prompts.size > 0 %}
<table>
<thead>
<tr>
<th>Title</th>
<th>Category</th>
<th>Description</th>
</tr>
</thead>
<tbody>
{% for prompt in all_prompts %}
<tr>
<td><a href="{{ prompt.url | relative_url }}">{{ prompt.title }}</a></td>
<td><span class="category-badge">{{ prompt.category | default: "General" }}</span></td>
<td>{{ prompt.description | default: "No description available" }}</td>
</tr>
{% endfor %}
</tbody>
</table>
{% else %}
<p><em>No prompts available yet. Start by adding some prompts to the <code>_prompts</code> directory!</em></p>
{% endif %}

## Contributing

To add a new prompt:

1. Create a new markdown file in the `_prompts` directory
2. Use the following front matter template:

```yaml
---
title: "Your Prompt Title"
category: "coding|writing|analysis|creative|productivity"
description: "Brief description of what this prompt does"
tags: ["tag1", "tag2"]
use_case: "When to use this prompt"
---

Your prompt content goes here...
```

3. Include examples and variations if applicable
