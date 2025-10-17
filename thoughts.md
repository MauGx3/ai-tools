---
layout: default
title: Thoughts Collection
nav_order: 6
description: "Personal reflections, experiments, and ideas"
permalink: /thoughts/
---

# Thoughts Collection

Personal reflections, experiments, and ideas related to AI tools and usage.

## Categories

### 🤔 Reflections
Insights and learnings from AI tool usage.

{% assign reflections = site.thoughts | where: "thought_type", "reflection" %}
{% if reflections.size > 0 %}
<ul>
{% for thought in reflections %}
  <li><a href="{{ thought.url | relative_url }}">{{ thought.title }}</a> - {{ thought.description | default: "No description available" }}</li>
{% endfor %}
</ul>
{% else %}
<p><em>No reflections available yet. <a href="#contributing">Share your insights!</a></em></p>
{% endif %}

### 🧪 Experiments
Testing new approaches and techniques.

{% assign experiments = site.thoughts | where: "thought_type", "experiment" %}
{% if experiments.size > 0 %}
<ul>
{% for thought in experiments %}
  <li><a href="{{ thought.url | relative_url }}">{{ thought.title }}</a> - {{ thought.description | default: "No description available" }}</li>
{% endfor %}
</ul>
{% else %}
<p><em>No experiments available yet. <a href="#contributing">Document your experiments!</a></em></p>
{% endif %}

### 💡 Ideas
Future improvements and potential projects.

{% assign ideas = site.thoughts | where: "thought_type", "idea" %}
{% if ideas.size > 0 %}
<ul>
{% for thought in ideas %}
  <li><a href="{{ thought.url | relative_url }}">{{ thought.title }}</a> - {{ thought.description | default: "No description available" }}</li>
{% endfor %}
</ul>
{% else %}
<p><em>No ideas available yet. <a href="#contributing">Share your ideas!</a></em></p>
{% endif %}

## All Thoughts

{% assign all_thoughts = site.thoughts | sort: "date" | reverse %}
{% if all_thoughts.size > 0 %}
<table>
<thead>
<tr>
<th>Title</th>
<th>Type</th>
<th>Date</th>
<th>Status</th>
<th>Description</th>
</tr>
</thead>
<tbody>
{% for thought in all_thoughts %}
<tr>
<td><a href="{{ thought.url | relative_url }}">{{ thought.title }}</a></td>
<td><span class="category-badge">{{ thought.thought_type | default: "General" }}</span></td>
<td>{{ thought.date | date: "%Y-%m-%d" | default: "N/A" }}</td>
<td><span class="category-badge">{{ thought.status | default: "N/A" }}</span></td>
<td>{{ thought.description | default: "No description available" }}</td>
</tr>
{% endfor %}
</tbody>
</table>
{% else %}
<p><em>No thoughts available yet. Start by adding some thoughts to the <code>_thoughts</code> directory!</em></p>
{% endif %}

## Contributing

To add a new thought:

1. Create a new markdown file in the `_thoughts` directory
2. Use the following front matter template:

```yaml
---
title: "Your Thought Title"
thought_type: "reflection|experiment|idea"
date: 2024-01-01
status: "draft|active|completed|archived"
related_tools: ["tool1", "tool2"]
description: "Brief description of this thought"
---

Your thought content goes here...

## Background
Context and background information...

## Analysis
Your analysis or findings...

## Follow-up Actions
What to do next...
```
