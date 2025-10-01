#!/usr/bin/env python3
"""
Repository Recommendation Engine

This module provides AI-powered repository recommendations by analyzing
project context and matching against starred repositories using semantic
understanding and multi-factor scoring.

Usage:
    from repo_recommender import RepositoryRecommender
    recommender = RepositoryRecommender()
    recommendations = recommender.recommend(project_path=".")
"""

import json
import re
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Optional

try:
    import numpy as np
except ImportError:
    import sys

    print(
        "Warning: numpy not installed.\n"
        f"Python executable: {sys.executable}\n"
        f"Install with: {sys.executable} -m pip install numpy"
    )
    np = None

try:
    from sentence_transformers import SentenceTransformer
except ImportError:
    import sys

    print(
        "Warning: sentence-transformers not installed.\n"
        f"Python executable: {sys.executable}\n"
        f"Install with: {sys.executable} -m pip install sentence-transformers"
    )
    SentenceTransformer = None

try:
    from sklearn.metrics.pairwise import cosine_similarity
except ImportError:
    import sys

    print(
        "Warning: scikit-learn not installed.\n"
        f"Python executable: {sys.executable}\n"
        f"Install with: {sys.executable} -m pip install scikit-learn"
    )
    cosine_similarity = None


@dataclass
class RecommendationScore:
    """Scoring breakdown for a repository recommendation"""

    semantic_score: float  # 0-1: Semantic similarity
    tech_stack_score: float  # 0-1: Technology stack match
    topic_score: float  # 0-1: Topic overlap
    popularity_score: float  # 0-1: Normalized popularity
    recency_score: float  # 0-1: Recent activity
    composite_score: float  # 0-100: Weighted total
    reasoning: List[str]  # Human-readable reasons


@dataclass
class RepositoryRecommendation:
    """A recommended repository with scoring details"""

    name: str
    owner: str
    url: str
    description: str
    category: str
    score: RecommendationScore
    metadata: Dict


class ProjectContext:
    """Extracts and represents project context for matching"""

    def __init__(self, project_path: str = "."):
        self.project_path = Path(project_path)
        self.readme_content = ""
        self.languages = []
        self.frameworks = []
        self.topics = []
        self.dependencies = []
        self.description = ""

    def extract(self) -> "ProjectContext":
        """Extract project context from multiple sources"""
        self._extract_readme()
        self._extract_package_info()
        self._detect_languages()
        return self

    def _extract_readme(self):
        """Extract information from README file"""
        readme_patterns = [
            "README.md",
            "README.MD",
            "readme.md",
            "README.rst",
            "README.txt",
            "README",
        ]

        for pattern in readme_patterns:
            readme_path = self.project_path / pattern
            if readme_path.exists():
                try:
                    with open(readme_path, "r", encoding="utf-8") as f:
                        self.readme_content = f.read()
                    self._parse_readme_content()
                    break
                except Exception as e:
                    print(f"Warning: Could not read README: {e}")

    def _parse_readme_content(self):
        """Parse README to extract key information"""
        if not self.readme_content:
            return

        # Extract description (usually first paragraph after title)
        lines = self.readme_content.split("\n")
        desc_lines = []
        skip_title = True

        for line in lines:
            line = line.strip()
            if not line or line.startswith("#"):
                if desc_lines:
                    break
                continue
            if skip_title and line:
                skip_title = False
            if not skip_title and line:
                desc_lines.append(line)
                if len(" ".join(desc_lines)) > 200:
                    break

        self.description = " ".join(desc_lines)

        # Extract technologies mentioned
        tech_keywords = {
            "languages": [
                "python",
                "javascript",
                "typescript",
                "java",
                "go",
                "rust",
                "ruby",
                "php",
                "c++",
                "c#",
                "swift",
                "kotlin",
            ],
            "frameworks": [
                "react",
                "vue",
                "angular",
                "django",
                "flask",
                "express",
                "fastapi",
                "spring",
                "rails",
                "laravel",
                "next.js",
                "nest.js",
            ],
        }

        content_lower = self.readme_content.lower()
        for lang in tech_keywords["languages"]:
            if lang in content_lower:
                self.languages.append(lang)

        for framework in tech_keywords["frameworks"]:
            if framework in content_lower:
                self.frameworks.append(framework)

    def _extract_package_info(self):
        """Extract dependencies from package files"""
        # Python: requirements.txt, setup.py, pyproject.toml
        req_file = self.project_path / "requirements.txt"
        if req_file.exists():
            try:
                with open(req_file, "r", encoding="utf-8") as f:
                    for line in f:
                        line = line.strip()
                        if line and not line.startswith("#"):
                            # Extract package name
                            pkg = re.split(r"[>=<\[]", line)[0].strip()
                            if pkg:
                                self.dependencies.append(pkg)
            except Exception as e:
                print(f"Warning: Could not read requirements.txt: {e}")

        # Node.js: package.json
        pkg_file = self.project_path / "package.json"
        if pkg_file.exists():
            try:
                with open(pkg_file, "r", encoding="utf-8") as f:
                    pkg_data = json.load(f)
                    self.description = self.description or pkg_data.get(
                        "description", ""
                    )

                    # Extract dependencies
                    deps = pkg_data.get("dependencies", {})
                    dev_deps = pkg_data.get("devDependencies", {})
                    self.dependencies.extend(list(deps.keys()))
                    self.dependencies.extend(list(dev_deps.keys()))

                    # Extract keywords as topics
                    keywords = pkg_data.get("keywords", [])
                    self.topics.extend(keywords)
            except Exception as e:
                print(f"Warning: Could not read package.json: {e}")

    def _detect_languages(self):
        """Detect programming languages from file extensions"""
        if self.languages:
            return  # Already detected from README

        lang_extensions = {
            ".py": "python",
            ".js": "javascript",
            ".ts": "typescript",
            ".java": "java",
            ".go": "go",
            ".rs": "rust",
            ".rb": "ruby",
            ".php": "php",
            ".cpp": "c++",
            ".cs": "c#",
            ".swift": "swift",
            ".kt": "kotlin",
        }

        lang_counts = defaultdict(int)
        try:
            for file_path in self.project_path.rglob("*"):
                if file_path.is_file():
                    ext = file_path.suffix.lower()
                    if ext in lang_extensions:
                        lang_counts[lang_extensions[ext]] += 1
        except Exception as e:
            print(f"Warning: Could not scan directory: {e}")

        # Take top 3 languages by file count
        sorted_langs = sorted(
            lang_counts.items(), key=lambda x: x[1], reverse=True
        )
        self.languages = [lang for lang, _ in sorted_langs[:3]]

    def get_text_representation(self) -> str:
        """Get a text representation for semantic embedding"""
        parts = []

        if self.description:
            parts.append(self.description)

        if self.languages:
            parts.append(f"Languages: {', '.join(self.languages)}")

        if self.frameworks:
            parts.append(f"Frameworks: {', '.join(self.frameworks)}")

        if self.topics:
            parts.append(f"Topics: {', '.join(self.topics[:5])}")

        return " | ".join(parts) if parts else "No description available"


class RepositoryRecommender:
    """AI-powered repository recommendation engine"""

    # Scoring weights
    WEIGHTS = {
        "semantic": 0.35,
        "tech_stack": 0.25,
        "topic": 0.20,
        "popularity": 0.10,
        "recency": 0.10,
    }

    # Category thresholds and keywords
    CATEGORIES = {
        "direct_dependency": {
            "keywords": ["library", "package", "module", "sdk", "api-client"],
            "threshold": 0.7,
        },
        "tool_utility": {
            "keywords": [
                "cli",
                "tool",
                "utility",
                "command-line",
                "automation",
            ],
            "threshold": 0.6,
        },
        "reference_implementation": {
            "keywords": [
                "example",
                "sample",
                "template",
                "boilerplate",
                "starter",
            ],
            "threshold": 0.5,
        },
        "learning_resource": {
            "keywords": [
                "tutorial",
                "guide",
                "learning",
                "course",
                "documentation",
                "awesome",
            ],
            "threshold": 0.4,
        },
    }

    def __init__(self, model_name: str = "all-MiniLM-L6-v2"):
        """
        Initialize recommender with ML model

        Args:
            model_name: Sentence transformer model name
                       (default: all-MiniLM-L6-v2 - fast and efficient)
        """
        self.model = None
        self.model_name = model_name

        if SentenceTransformer is not None:
            try:
                print(f"Loading model: {model_name}...")
                self.model = SentenceTransformer(model_name)
                print("Model loaded successfully")
            except Exception as e:
                print(f"Warning: Could not load model: {e}")
                print("Semantic scoring will be disabled")

    def recommend(
        self,
        starred_repos_file: str,
        project_path: str = ".",
        top_n: int = 20,
        min_score: float = 30.0,
    ) -> Dict[str, List[RepositoryRecommendation]]:
        """
        Generate repository recommendations

        Args:
            starred_repos_file: Path to starred repos JSON
            project_path: Path to project for analysis
            top_n: Number of top recommendations per category
            min_score: Minimum composite score (0-100)

        Returns:
            Dictionary mapping categories to recommendations
        """
        # Extract project context
        print("Analyzing project context...")
        context = ProjectContext(project_path).extract()
        print(f"Project: {context.description[:100]}...")
        print(f"Languages: {', '.join(context.languages)}")
        print(f"Frameworks: {', '.join(context.frameworks)}")

        # Load starred repositories
        print(f"\nLoading starred repositories from {starred_repos_file}...")
        with open(starred_repos_file, "r", encoding="utf-8") as f:
            data = json.load(f)
            repos = data.get("repositories", [])
        print(f"Loaded {len(repos)} repositories")

        # Generate embeddings if model available
        project_embedding = None
        repo_embeddings = None

        if self.model is not None:
            print("\nGenerating semantic embeddings...")
            project_text = context.get_text_representation()
            project_embedding = self.model.encode([project_text])[0]

            # Generate embeddings for repositories
            repo_texts = [self._get_repo_text(repo) for repo in repos]
            repo_embeddings = self.model.encode(repo_texts)
            print("Embeddings generated")

        # Score all repositories
        print("\nScoring repositories...")
        recommendations = []
        for i, repo in enumerate(repos):
            score = self._score_repository(
                repo,
                context,
                project_embedding,
                repo_embeddings[i] if repo_embeddings is not None else None,
            )

            if score.composite_score >= min_score:
                category = self._categorize_repository(repo, score)
                recommendations.append(
                    RepositoryRecommendation(
                        name=repo["name"],
                        owner=repo["owner"],
                        url=repo["github_url"],
                        description=repo.get("description", ""),
                        category=category,
                        score=score,
                        metadata=repo,
                    )
                )

        # Group by category and sort
        categorized = defaultdict(list)
        for rec in recommendations:
            categorized[rec.category].append(rec)

        # Sort each category by score and limit to top_n
        for category in categorized:
            categorized[category].sort(
                key=lambda x: x.score.composite_score, reverse=True
            )
            categorized[category] = categorized[category][:top_n]

        print(f"\nGenerated {len(recommendations)} recommendations")
        for category, recs in categorized.items():
            print(f"  {category}: {len(recs)}")

        return dict(categorized)

    def _get_repo_text(self, repo: Dict) -> str:
        """Get text representation of repository for embedding"""
        parts = []

        desc = repo.get("enhanced_description") or repo.get("description", "")
        if desc:
            parts.append(desc)

        if repo.get("language"):
            parts.append(f"Language: {repo['language']}")

        topics = repo.get("topics", [])
        if topics:
            parts.append(f"Topics: {', '.join(topics[:5])}")

        return " | ".join(parts) if parts else "No description"

    def _score_repository(
        self,
        repo: Dict,
        context: ProjectContext,
        project_embedding: Optional[np.ndarray],
        repo_embedding: Optional[np.ndarray],
    ) -> RecommendationScore:
        """Calculate comprehensive score for a repository"""
        reasoning = []

        # 1. Semantic similarity (0-1)
        semantic_score = 0.0
        if (
            project_embedding is not None
            and repo_embedding is not None
            and cosine_similarity is not None
        ):
            semantic_score = float(
                cosine_similarity([project_embedding], [repo_embedding])[0][0]
            )
            if semantic_score > 0.7:
                reasoning.append(
                    f"High semantic similarity ({semantic_score:.2f})"
                )

        # 2. Technology stack matching (0-1)
        tech_score = self._calculate_tech_stack_score(repo, context, reasoning)

        # 3. Topic overlap (0-1)
        topic_score = self._calculate_topic_score(repo, context, reasoning)

        # 4. Popularity score (0-1)
        popularity_score = self._calculate_popularity_score(repo, reasoning)

        # 5. Recency score (0-1)
        recency_score = self._calculate_recency_score(repo, reasoning)

        # Calculate weighted composite score (0-100)
        composite = (
            semantic_score * self.WEIGHTS["semantic"]
            + tech_score * self.WEIGHTS["tech_stack"]
            + topic_score * self.WEIGHTS["topic"]
            + popularity_score * self.WEIGHTS["popularity"]
            + recency_score * self.WEIGHTS["recency"]
        ) * 100

        return RecommendationScore(
            semantic_score=semantic_score,
            tech_stack_score=tech_score,
            topic_score=topic_score,
            popularity_score=popularity_score,
            recency_score=recency_score,
            composite_score=composite,
            reasoning=reasoning,
        )

    def _calculate_tech_stack_score(
        self, repo: Dict, context: ProjectContext, reasoning: List[str]
    ) -> float:
        """Calculate technology stack matching score"""
        score = 0.0
        matches = []

        # Language match
        repo_lang = repo.get("language") or ""
        repo_lang = repo_lang.lower() if repo_lang else ""
        context_langs = [lang.lower() for lang in context.languages]
        if repo_lang and repo_lang in context_langs:
            score += 0.5
            matches.append(f"language: {repo_lang}")

        # Framework mentions in description/topics
        repo_text = (
            f"{repo.get('description', '')} {' '.join(repo.get('topics', []))}"
        ).lower()

        for framework in context.frameworks:
            if framework.lower() in repo_text:
                score += 0.3
                matches.append(f"framework: {framework}")
                break  # Count only once

        # Dependency name matching
        repo_name_lower = repo["name"].lower()
        for dep in context.dependencies:
            dep_lower = dep.lower()
            if dep_lower in repo_name_lower or repo_name_lower in dep_lower:
                score += 0.2
                matches.append(f"dependency: {dep}")
                break

        if matches:
            reasoning.append(f"Tech stack match: {', '.join(matches)}")

        return min(score, 1.0)

    def _calculate_topic_score(
        self, repo: Dict, context: ProjectContext, reasoning: List[str]
    ) -> float:
        """Calculate topic overlap score"""
        repo_topics = set(t.lower() for t in repo.get("topics", []))
        project_topics = set(t.lower() for t in context.topics)

        if not repo_topics or not project_topics:
            return 0.0

        overlap = repo_topics.intersection(project_topics)
        if overlap:
            score = len(overlap) / max(len(repo_topics), len(project_topics))
            reasoning.append(f"Shared topics: {', '.join(overlap)}")
            return score

        return 0.0

    def _calculate_popularity_score(
        self, repo: Dict, reasoning: List[str]
    ) -> float:
        """Calculate normalized popularity score"""
        stars = repo.get("stars", 0)

        # Logarithmic scale: 0 stars -> 0, 10k stars -> ~1.0
        if stars == 0:
            return 0.0

        score = min(np.log10(stars + 1) / 4.0, 1.0) if np else 0.0

        if stars > 5000:
            reasoning.append(f"Highly popular ({stars:,} stars)")
        elif stars > 1000:
            reasoning.append(f"Popular project ({stars:,} stars)")

        return score

    def _calculate_recency_score(
        self, repo: Dict, reasoning: List[str]
    ) -> float:
        """Calculate recency/activity score"""
        from datetime import datetime, timezone

        pushed_at = repo.get("pushed_at")
        if not pushed_at:
            return 0.0

        try:
            # Parse ISO format timestamp
            last_update = datetime.fromisoformat(
                pushed_at.replace("Z", "+00:00")
            )
            now = datetime.now(timezone.utc)
            days_ago = (now - last_update).days

            # Score based on recency: < 30 days -> 1.0, > 365 days -> 0.0
            if days_ago < 30:
                score = 1.0
                reasoning.append("Recently updated (< 1 month)")
            elif days_ago < 90:
                score = 0.8
                reasoning.append("Recently updated (< 3 months)")
            elif days_ago < 180:
                score = 0.6
            elif days_ago < 365:
                score = 0.4
            else:
                score = 0.2

            return score
        except Exception:
            return 0.0

    def _categorize_repository(
        self, repo: Dict, score: RecommendationScore
    ) -> str:
        """Categorize repository based on content and score"""
        desc = repo.get("description", "")
        enhanced = repo.get("enhanced_description", "")
        topics = " ".join(repo.get("topics", []))
        repo_text = f"{desc} {enhanced} {topics}".lower()

        # Check each category
        for category, config in self.CATEGORIES.items():
            for keyword in config["keywords"]:
                if keyword in repo_text:
                    return category

        # Default categorization based on score
        if score.tech_stack_score > 0.7:
            return "direct_dependency"
        elif score.semantic_score > 0.6:
            return "reference_implementation"
        else:
            return "learning_resource"

    def generate_report(
        self,
        recommendations: Dict[str, List[RepositoryRecommendation]],
        output_format: str = "markdown",
    ) -> str:
        """
        Generate human-readable report

        Args:
            recommendations: Categorized recommendations
            output_format: 'markdown' or 'text'

        Returns:
            Formatted report string
        """
        if output_format == "markdown":
            return self._generate_markdown_report(recommendations)
        else:
            return self._generate_text_report(recommendations)

    def _generate_markdown_report(
        self, recommendations: Dict[str, List[RepositoryRecommendation]]
    ) -> str:
        """Generate markdown report"""
        lines = ["# Repository Recommendations\n"]

        category_names = {
            "direct_dependency": "📦 Direct Dependencies",
            "tool_utility": "🔧 Tools & Utilities",
            "reference_implementation": "📚 Reference Implementations",
            "learning_resource": "🎓 Learning Resources",
        }

        for category, recs in sorted(recommendations.items()):
            if not recs:
                continue

            lines.append(f"\n## {category_names.get(category, category)}\n")

            for rec in recs:
                lines.append(f"### [{rec.owner}/{rec.name}]({rec.url})")
                score_line = (
                    f"\n**Score: {rec.score.composite_score:.1f}/100**\n"
                )
                lines.append(score_line)
                lines.append(f"{rec.description}\n")

                # Scoring details
                lines.append("**Scoring Breakdown:**")
                lines.append(
                    f"- Semantic Similarity: {rec.score.semantic_score:.2f}"
                )
                lines.append(
                    f"- Tech Stack Match: {rec.score.tech_stack_score:.2f}"
                )
                lines.append(f"- Topic Overlap: {rec.score.topic_score:.2f}")
                lines.append(f"- Popularity: {rec.score.popularity_score:.2f}")
                lines.append(f"- Recency: {rec.score.recency_score:.2f}\n")

                # Reasoning
                if rec.score.reasoning:
                    lines.append("**Why this recommendation:**")
                    for reason in rec.score.reasoning:
                        lines.append(f"- {reason}")
                    lines.append("")

                # Metadata
                lang = rec.metadata.get("language")
                stars = rec.metadata.get("stars", 0)
                topics = rec.metadata.get("topics", [])

                meta_parts = []
                if lang:
                    meta_parts.append(f"Language: {lang}")
                if stars:
                    meta_parts.append(f"⭐ {stars:,}")
                if topics:
                    meta_parts.append(f"Topics: {', '.join(topics[:5])}")

                if meta_parts:
                    lines.append(" | ".join(meta_parts))

                lines.append("\n---\n")

        return "\n".join(lines)

    def _generate_text_report(
        self, recommendations: Dict[str, List[RepositoryRecommendation]]
    ) -> str:
        """Generate plain text report"""
        lines = ["REPOSITORY RECOMMENDATIONS", "=" * 50, ""]

        for category, recs in sorted(recommendations.items()):
            if not recs:
                continue

            lines.append(f"\n{category.upper().replace('_', ' ')}")
            lines.append("-" * 50)

            for i, rec in enumerate(recs, 1):
                lines.append(f"\n{i}. {rec.owner}/{rec.name}")
                lines.append(f"   Score: {rec.score.composite_score:.1f}/100")
                lines.append(f"   URL: {rec.url}")
                lines.append(f"   {rec.description}")

                if rec.score.reasoning:
                    lines.append("   Reasons:")
                    for reason in rec.score.reasoning:
                        lines.append(f"   - {reason}")

                lines.append("")

        return "\n".join(lines)


def main():
    """CLI interface for testing"""
    import argparse

    parser = argparse.ArgumentParser(
        description="AI-powered repository recommendations"
    )
    parser.add_argument(
        "--starred-repos",
        default="results/starred_repos_authenticated_user_latest.json",
        help="Path to starred repositories JSON file",
    )
    parser.add_argument(
        "--project-path",
        default=".",
        help="Path to project for analysis",
    )
    parser.add_argument(
        "--output",
        "-o",
        help="Output file for report (default: auto-generated in results/)",
    )
    parser.add_argument(
        "--format",
        choices=["markdown", "text"],
        default="markdown",
        help="Output format",
    )
    parser.add_argument(
        "--top-n",
        type=int,
        default=10,
        help="Number of recommendations per category",
    )
    parser.add_argument(
        "--min-score",
        type=float,
        default=30.0,
        help="Minimum score threshold (0-100)",
    )

    args = parser.parse_args()

    # Create recommender
    recommender = RepositoryRecommender()

    # Generate recommendations
    recommendations = recommender.recommend(
        starred_repos_file=args.starred_repos,
        project_path=args.project_path,
        top_n=args.top_n,
        min_score=args.min_score,
    )

    # Generate report
    report = recommender.generate_report(recommendations, args.format)

    # Generate default output filename if not specified
    output_file = args.output
    if not output_file:
        from datetime import datetime, timezone

        timestamp = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
        ext = "md" if args.format == "markdown" else "txt"
        output_file = f"results/recommendations_{timestamp}.{ext}"

    # Save output
    import os

    output_dir = os.path.dirname(output_file)
    if output_dir:
        os.makedirs(output_dir, exist_ok=True)

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(report)
    print(f"\nReport saved to {output_file}")

    # Also print to stdout for immediate viewing
    print("\n" + "=" * 50)
    print(report[:1000] + "..." if len(report) > 1000 else report)


if __name__ == "__main__":
    main()
