# Repository Recommendation System

## Overview

The AI-powered repository recommendation system analyzes your project and suggests relevant repositories from your GitHub starred list. It uses semantic understanding, multi-factor scoring, and intelligent categorization to provide meaningful recommendations.

## Features

### Multi-Factor Scoring System

The recommendation engine evaluates repositories using five key factors:

1. **Semantic Similarity (35% weight)**: Uses sentence transformers to understand the conceptual similarity between your project and repositories
2. **Technology Stack Matching (25% weight)**: Compares programming languages, frameworks, and dependencies
3. **Topic Overlap (20% weight)**: Evaluates shared topics and keywords
4. **Popularity (10% weight)**: Considers star count and community engagement
5. **Recency (10% weight)**: Favors actively maintained projects

Each repository receives a composite score from 0-100, with detailed reasoning for recommendations.

### Intelligent Categorization

Recommendations are automatically categorized into:

- **📦 Direct Dependencies**: Libraries and packages that can be directly added to your project
- **🔧 Tools & Utilities**: Command-line tools and automation utilities
- **📚 Reference Implementations**: Similar projects and code examples
- **🎓 Learning Resources**: Tutorials, guides, and educational materials

### Project Context Extraction

The system automatically analyzes your project by:

- Parsing README files for project description and technologies
- Reading `package.json` (Node.js) for dependencies and metadata
- Reading `requirements.txt` (Python) for dependencies
- Detecting programming languages from file extensions
- Extracting frameworks and technologies mentioned

## Installation

### Install Dependencies

```bash
# Install all dependencies
pip install -r scripts/requirements.txt

# Or install individually
pip install sentence-transformers scikit-learn numpy torch
```

**Note**: The first run will download the ML model (~80MB). This is a one-time download.

### Verify Installation

```bash
python3 -c "from sentence_transformers import SentenceTransformer; print('OK')"
```

## Usage

### Basic Usage

```bash
# Analyze current project and get recommendations
python3 scripts/scan_starred_repos.py --recommend
```

### Analyze Specific Project

```bash
# Analyze a different project
python3 scripts/scan_starred_repos.py --recommend --project-path /path/to/project
```

### Customize Output

```bash
# Save recommendations to file
python3 scripts/scan_starred_repos.py --recommend --recommend-output recommendations.md

# Use text format instead of markdown
python3 scripts/scan_starred_repos.py --recommend --recommend-format text

# Get more recommendations per category
python3 scripts/scan_starred_repos.py --recommend --recommend-top-n 20

# Lower the minimum score threshold
python3 scripts/scan_starred_repos.py --recommend --recommend-min-score 20.0
```

### Complete Workflow

```bash
# 1. First, scan and save your starred repositories
python3 scripts/scan_starred_repos.py --enhance-description --output repos/starred-repos.json

# 2. Then generate recommendations for your project
python3 scripts/scan_starred_repos.py --recommend --recommend-output recommendations.md
```

## How It Works

### 1. Project Analysis

The system extracts context from your project:

```
Project: AI Tools collection for prompt engineering and repository analysis
Languages: python, javascript
Frameworks: flask, react
```

### 2. Repository Scoring

Each starred repository is scored across multiple dimensions:

```
Repository: username/awesome-project
- Semantic Similarity: 0.85 (high conceptual match)
- Tech Stack Match: 0.70 (Python + Flask)
- Topic Overlap: 0.60 (shared: ai, tools)
- Popularity: 0.75 (5,000 stars)
- Recency: 0.90 (updated last week)

Composite Score: 76.5/100
```

### 3. Categorization

Repositories are categorized based on:
- Keywords in descriptions and topics
- Repository characteristics (library vs tool)
- Score patterns (high tech match → dependency)

### 4. Report Generation

Results are presented with:
- Ranked recommendations per category
- Detailed scoring breakdown
- Human-readable reasoning
- Relevant metadata (stars, language, topics)

## Output Example

```markdown
# Repository Recommendations

## 📦 Direct Dependencies

### username/awesome-library
**Score: 85.2/100**

A powerful Python library for data processing and analysis.

**Scoring Breakdown:**
- Semantic Similarity: 0.87
- Tech Stack Match: 0.90
- Topic Overlap: 0.70
- Popularity: 0.80
- Recency: 0.85

**Why this recommendation:**
- High semantic similarity (0.87)
- Tech stack match: language: python
- Shared topics: data, analysis
- Highly popular (12,500 stars)
- Recently updated (< 1 month)

Language: Python | ⭐ 12,500 | Topics: data, analysis, python, library
```

## Configuration

### Scoring Weights

You can modify scoring weights in `repo_recommender.py`:

```python
WEIGHTS = {
    "semantic": 0.35,      # Adjust importance of semantic similarity
    "tech_stack": 0.25,    # Adjust tech stack matching weight
    "topic": 0.20,         # Adjust topic overlap weight
    "popularity": 0.10,    # Adjust popularity factor
    "recency": 0.10,       # Adjust recency importance
}
```

### Category Thresholds

Adjust categorization rules:

```python
CATEGORIES = {
    "direct_dependency": {
        "keywords": ["library", "package", "module"],
        "threshold": 0.7,  # Minimum score for this category
    },
    # ...
}
```

### ML Model Selection

Choose a different sentence transformer model:

```python
# Faster but less accurate
recommender = RepositoryRecommender(model_name="all-MiniLM-L6-v2")

# More accurate but slower
recommender = RepositoryRecommender(model_name="all-mpnet-base-v2")
```

## Performance

- **Model Loading**: 2-5 seconds (first time only)
- **Embedding Generation**: ~0.5 seconds per 100 repositories
- **Total Analysis**: < 2 minutes for 500+ repositories

## Troubleshooting

### Model Download Issues

If the model fails to download:

```bash
# Manually download model
python3 -c "from sentence_transformers import SentenceTransformer; SentenceTransformer('all-MiniLM-L6-v2')"
```

### Memory Issues

For large repository lists (1000+), consider:

```bash
# Process in batches
python3 scripts/scan_starred_repos.py --recommend --recommend-top-n 5 --recommend-min-score 50
```

### No Recommendations

If you get no recommendations:
1. Lower the minimum score: `--recommend-min-score 20`
2. Ensure your project has a README with description
3. Check that starred-repos.json exists and has data

## Extensibility

### Adding New Scoring Factors

```python
def _calculate_custom_score(self, repo, context, reasoning):
    # Add your custom scoring logic
    score = 0.0
    # ...
    return score
```

### Custom Context Extraction

```python
class ProjectContext:
    def _extract_custom_source(self):
        # Add support for new project file types
        # e.g., Cargo.toml, go.mod, etc.
        pass
```

### Hybrid ML Approach

The architecture supports adding API-based models:

```python
class RepositoryRecommender:
    def _get_embedding_api(self, text):
        # Call OpenAI, Cohere, or other embedding APIs
        # Fall back to local model if API fails
        pass
```

## Future Enhancements

- [ ] Support for more project file types (Cargo.toml, go.mod, etc.)
- [ ] Hybrid local + cloud ML models
- [ ] Dependency graph analysis
- [ ] GitHub API integration for real-time data
- [ ] Interactive CLI with filtering
- [ ] Web UI for visualization
- [ ] Export to various formats (JSON, CSV, HTML)
- [ ] Integration with project management tools

## Contributing

Contributions welcome! Areas of interest:
- Additional scoring factors
- Better categorization logic
- Support for more programming languages
- Performance optimizations
- UI/UX improvements

## License

Same as parent project.
