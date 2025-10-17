---
layout: default
title: Modes Collection
nav_order: 4
description: "AI interaction modes and configurations"
permalink: /modes/
---

# Modes Collection

AI interaction modes and configurations for different use cases.

## Categories

### 💻 Development Modes
Coding and software development configurations.

{% assign development_modes = site.modes | where: "mode_type", "development" %}
{% if development_modes.size > 0 %}
<ul>
{% for mode in development_modes %}
  <li><a href="{{ mode.url | relative_url }}">{{ mode.title }}</a> - {{ mode.description | default: "No description available" }}</li>
{% endfor %}
</ul>
{% else %}
<p><em>No development modes available yet. <a href="#contributing">Contribute some!</a></em></p>
{% endif %}

### 🔍 Research Modes
Information gathering and analysis configurations.

{% assign research_modes = site.modes | where: "mode_type", "research" %}
{% if research_modes.size > 0 %}
<ul>
{% for mode in research_modes %}
  <li><a href="{{ mode.url | relative_url }}">{{ mode.title }}</a> - {{ mode.description | default: "No description available" }}</li>
{% endfor %}
</ul>
{% else %}
<p><em>No research modes available yet. <a href="#contributing">Contribute some!</a></em></p>
{% endif %}

### 📝 Documentation Modes
Technical writing and documentation configurations.

{% assign documentation_modes = site.modes | where: "mode_type", "documentation" %}
{% if documentation_modes.size > 0 %}
<ul>
{% for mode in documentation_modes %}
  <li><a href="{{ mode.url | relative_url }}">{{ mode.title }}</a> - {{ mode.description | default: "No description available" }}</li>
{% endfor %}
</ul>
{% else %}
<p><em>No documentation modes available yet. <a href="#contributing">Contribute some!</a></em></p>
{% endif %}

### 🛠️ Troubleshooting Modes
Problem-solving and debugging configurations.

{% assign troubleshooting_modes = site.modes | where: "mode_type", "troubleshooting" %}
{% if troubleshooting_modes.size > 0 %}
<ul>
{% for mode in troubleshooting_modes %}
  <li><a href="{{ mode.url | relative_url }}">{{ mode.title }}</a> - {{ mode.description | default: "No description available" }}</li>
{% endfor %}
</ul>
{% else %}
<p><em>No troubleshooting modes available yet. <a href="#contributing">Contribute some!</a></em></p>
{% endif %}

## All Modes

{% assign all_modes = site.modes | sort: "title" %}
{% if all_modes.size > 0 %}
<table>
<thead>
<tr>
<th>Title</th>
<th>Type</th>
<th>AI Model</th>
<th>Description</th>
</tr>
</thead>
<tbody>
{% for mode in all_modes %}
<tr>
<td><a href="{{ mode.url | relative_url }}">{{ mode.title }}</a></td>
<td><span class="category-badge">{{ mode.mode_type | default: "General" }}</span></td>
<td>{{ mode.ai_model | default: "Any" }}</td>
<td>{{ mode.description | default: "No description available" }}</td>
</tr>
{% endfor %}
</tbody>
</table>
{% else %}
<p><em>No modes available yet. Start by adding some modes to the <code>_modes</code> directory!</em></p>
{% endif %}

## Contributing

To add a new mode:

1. Create a new markdown file in the `_modes` directory
2. Use the following front matter template:

```yaml
---
title: "Your Mode Title"
mode_type: "development|research|documentation|troubleshooting"
ai_model: "Recommended AI model (e.g., GPT-4, Claude, etc.)"
context_length: "Recommended context length"
best_for: "What this mode is best suited for"
description: "Brief description of this mode"
---

Your mode description and instructions go here...

## Configuration
Specific settings and parameters...

## Example Usage
How to use this mode effectively...
```
