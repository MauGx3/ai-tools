---
layout: default
title: Instructions Collection
---

## Instructions Collection

Step-by-step guides and procedures for AI tools and workflows.

## Categories

### ⚙️ Setup Instructions
Installation and configuration guides.

{% assign setup_instructions = site.instructions | where: "type", "setup" %}
{% if setup_instructions.size > 0 %}
<ul>
{% for instruction in setup_instructions %}
  <li><a href="{{ instruction.url | relative_url }}">{{ instruction.title }}</a> - {{ instruction.description | default: "No description available" }}</li>
{% endfor %}
</ul>
{% else %}
<p><em>No setup instructions available yet. <a href="#contributing">Contribute some!</a></em></p>
{% endif %}

### 📖 Usage Instructions
How-to guides for tools and workflows.

{% assign usage_instructions = site.instructions | where: "type", "usage" %}
{% if usage_instructions.size > 0 %}
<ul>
{% for instruction in usage_instructions %}
  <li><a href="{{ instruction.url | relative_url }}">{{ instruction.title }}</a> - {{ instruction.description | default: "No description available" }}</li>
{% endfor %}
</ul>
{% else %}
<p><em>No usage instructions available yet. <a href="#contributing">Contribute some!</a></em></p>
{% endif %}

### ⭐ Best Practices
Recommended approaches and methodologies.

{% assign best_practice_instructions = site.instructions | where: "type", "best-practices" %}
{% if best_practice_instructions.size > 0 %}
<ul>
{% for instruction in best_practice_instructions %}
  <li><a href="{{ instruction.url | relative_url }}">{{ instruction.title }}</a> - {{ instruction.description | default: "No description available" }}</li>
{% endfor %}
</ul>
{% else %}
<p><em>No best practices available yet. <a href="#contributing">Contribute some!</a></em></p>
{% endif %}

## All Instructions

{% assign all_instructions = site.instructions | sort: "title" %}
{% if all_instructions.size > 0 %}
<table>
<thead>
<tr>
<th>Title</th>
<th>Type</th>
<th>Difficulty</th>
<th>Description</th>
</tr>
</thead>
<tbody>
{% for instruction in all_instructions %}
<tr>
<td><a href="{{ instruction.url | relative_url }}">{{ instruction.title }}</a></td>
<td><span class="category-badge">{{ instruction.type | default: "General" }}</span></td>
<td><span class="category-badge">{{ instruction.difficulty | default: "N/A" }}</span></td>
<td>{{ instruction.description | default: "No description available" }}</td>
</tr>
{% endfor %}
</tbody>
</table>
{% else %}
<p><em>No instructions available yet. Start by adding some instructions to the <code>_instructions</code> directory!</em></p>
{% endif %}

## Contributing

To add a new instruction:

1. Create a new markdown file in the `_instructions` directory
2. Use the following front matter template:

```yaml
---
title: "Your Instruction Title"
type: "setup|usage|best-practices"
difficulty: "beginner|intermediate|advanced"
time_required: "Estimated time to complete"
prerequisites: "What you need before starting"
description: "Brief description of what this instruction covers"
---

Your instruction content goes here...

## Prerequisites
- List any requirements

## Steps
1. Step one
2. Step two
3. Step three

## Troubleshooting
Common issues and solutions...
```