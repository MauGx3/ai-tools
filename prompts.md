---
layout: default
title: Prompts
nav_order: 2
has_children: true
description: "Curated AI prompts organized by category"
permalink: /prompts/
---

# Prompts Collection
{: .no_toc }

This section contains curated AI prompts organized by category. Each prompt includes detailed metadata, usage instructions, and examples.
{: .fs-6 .fw-300 }

---

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## Categories

### 🚀 Coding Prompts
{: .text-blue-300}

Prompts for software development, debugging, and code review.

{% assign coding_prompts = site.prompts | where: "category", "coding" %}
{% if coding_prompts.size > 0 %}
{% for prompt in coding_prompts %}
- [{{ prompt.title }}]({{ prompt.url | relative_url }}) - {{ prompt.description | default: "No description available" }}
{% endfor %}
{% else %}
*No coding prompts available yet. [Contribute some!](#contributing)*
{% endif %}

### ✍️ Writing Prompts
{: .text-green-300}

Prompts for content creation, editing, and documentation.

{% assign writing_prompts = site.prompts | where: "category", "writing" %}
{% if writing_prompts.size > 0 %}
{% for prompt in writing_prompts %}
- [{{ prompt.title }}]({{ prompt.url | relative_url }}) - {{ prompt.description | default: "No description available" }}
{% endfor %}
{% else %}
*No writing prompts available yet. [Contribute some!](#contributing)*
{% endif %}

### 📊 Analysis Prompts
{: .text-purple-300}

Prompts for data analysis, research, and evaluation.

{% assign analysis_prompts = site.prompts | where: "category", "analysis" %}
{% if analysis_prompts.size > 0 %}
{% for prompt in analysis_prompts %}
- [{{ prompt.title }}]({{ prompt.url | relative_url }}) - {{ prompt.description | default: "No description available" }}
{% endfor %}
{% else %}
*No analysis prompts available yet. [Contribute some!](#contributing)*
{% endif %}

### 🎨 Creative Prompts
{: .text-yellow-300}

Prompts for brainstorming, ideation, and creative writing.

{% assign creative_prompts = site.prompts | where: "category", "creative" %}
{% if creative_prompts.size > 0 %}
{% for prompt in creative_prompts %}
- [{{ prompt.title }}]({{ prompt.url | relative_url }}) - {{ prompt.description | default: "No description available" }}
{% endfor %}
{% else %}
*No creative prompts available yet. [Contribute some!](#contributing)*
{% endif %}

### ⚡ Productivity Prompts
{: .text-red-300}

Prompts for task management, planning, and optimization.

{% assign productivity_prompts = site.prompts | where: "category", "productivity" %}
{% if productivity_prompts.size > 0 %}
{% for prompt in productivity_prompts %}
- [{{ prompt.title }}]({{ prompt.url | relative_url }}) - {{ prompt.description | default: "No description available" }}
{% endfor %}
{% else %}
*No productivity prompts available yet. [Contribute some!](#contributing)*
{% endif %}

---

## All Prompts

{% assign all_prompts = site.prompts | sort: "title" %}
{% if all_prompts.size > 0 %}

| Title | Category | Description |
|:------|:---------|:------------|
{% for prompt in all_prompts -%}
| [{{ prompt.title }}]({{ prompt.url | relative_url }}) | `{{ prompt.category | default: "General" }}` | {{ prompt.description | default: "No description available" }} |
{% endfor %}

{% else %}
*No prompts available yet. Start by adding some prompts to the `_prompts` directory!*
{% endif %}

---

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
