#!/usr/bin/env python3
"""
Starred Repository Scanner

This script fetches starred repositories from GitHub, extracts metadata,
and prepares data for AI-based analysis.

Usage:
    python scan_starred_repos.py --output data/starred-repos.json
    python scan_starred_repos.py --username octocat --limit 50
"""

import argparse
from dotenv import load_dotenv
import json
import os
import sys
from datetime import datetime
from typing import Dict, List, Optional
from urllib.parse import urljoin

# Load environment variables from .env file in the project root
load_dotenv()

try:
    import requests
except ImportError:
    print(
        "Error: requests library is required. Install with: pip install requests"
    )
    sys.exit(1)


class StarredRepoScanner:
    """Scanner for GitHub starred repositories"""

    BASE_URL = "https://api.github.com"

    def __init__(
        self, token: Optional[str] = None, username: Optional[str] = None
    ):
        """
        Initialize scanner

        Args:
            token: GitHub personal access token (optional but recommended)
            username: GitHub username to scan (defaults to authenticated user)
        """
        self.token = token or os.environ.get("GITHUB_TOKEN")
        self.username = username
        self.headers = {}

        if self.token:
            self.headers["Authorization"] = f"token {self.token}"

        self.headers["Accept"] = "application/vnd.github.v3+json"

    def fetch_starred_repos(
        self, per_page: int = 100, max_pages: Optional[int] = None
    ) -> List[Dict]:
        """
        Fetch starred repositories

        Args:
            per_page: Number of results per page (max 100)
            max_pages: Maximum number of pages to fetch (None for all)

        Returns:
            List of repository data dictionaries
        """
        url = f"{self.BASE_URL}/user/starred"
        if self.username:
            url = f"{self.BASE_URL}/users/{self.username}/starred"

        all_repos = []
        page = 1

        while True:
            if max_pages and page > max_pages:
                break

            print(f"Fetching page {page}...", file=sys.stderr)

            params = {"per_page": per_page, "page": page}
            response = requests.get(url, headers=self.headers, params=params)

            if response.status_code == 401:
                print(
                    "Error: Authentication required. Set GITHUB_TOKEN environment variable.",
                    file=sys.stderr,
                )
                sys.exit(1)
            elif response.status_code == 404:
                print(
                    f"Error: User '{self.username}' not found.",
                    file=sys.stderr,
                )
                sys.exit(1)
            elif response.status_code != 200:
                print(
                    f"Error: API returned status code {response.status_code}",
                    file=sys.stderr,
                )
                print(f"Response: {response.text}", file=sys.stderr)
                sys.exit(1)

            repos = response.json()

            if not repos:
                break

            all_repos.extend(repos)
            page += 1

            # Check rate limit
            remaining = response.headers.get("X-RateLimit-Remaining")
            if remaining and int(remaining) < 10:
                print(
                    f"Warning: Only {remaining} API calls remaining",
                    file=sys.stderr,
                )

        print(
            f"Fetched {len(all_repos)} starred repositories", file=sys.stderr
        )
        return all_repos

    def fetch_readme(self, owner: str, repo: str) -> Optional[str]:
        """
        Fetch README content for a repository

        Args:
            owner: Repository owner
            repo: Repository name

        Returns:
            README content as string, or None if not found
        """
        url = f"{self.BASE_URL}/repos/{owner}/{repo}/readme"

        try:
            response = requests.get(url, headers=self.headers)
            if response.status_code == 200:
                data = response.json()
                # README content is base64 encoded
                import base64

                content = base64.b64decode(data["content"]).decode("utf-8")
                return content
        except Exception as e:
            print(
                f"Warning: Could not fetch README for {owner}/{repo}: {e}",
                file=sys.stderr,
            )

        return None

    def fetch_languages(self, owner: str, repo: str) -> Optional[Dict]:
        """
        Fetch language breakdown for a repository

        Args:
            owner: Repository owner
            repo: Repository name

        Returns:
            Dictionary of languages with byte counts, or None if not found
        """
        url = f"{self.BASE_URL}/repos/{owner}/{repo}/languages"

        try:
            response = requests.get(url, headers=self.headers)
            if response.status_code == 200:
                return response.json()
        except Exception as e:
            print(
                f"Warning: Could not fetch languages for {owner}/{repo}: {e}",
                file=sys.stderr,
            )

        return None

    def generate_enhanced_description(
        self, repo: Dict, readme: Optional[str] = None
    ) -> str:
        """
        Generate an enhanced description using repository metadata

        Args:
            repo: Repository data from GitHub API
            readme: Optional README content for context

        Returns:
            Enhanced description string
        """
        base_description = repo.get("description", "")

        # Start with base description
        enhanced_parts = []

        if base_description:
            enhanced_parts.append(base_description)

        # Add context from topics
        topics = repo.get("topics", [])
        if topics and len(topics) > 0:
            topic_str = ", ".join(topics[:5])  # First 5 topics
            enhanced_parts.append(f"Topics: {topic_str}")

        # Add language context
        language = repo.get("language")
        if language:
            enhanced_parts.append(f"Built with {language}")

        # Add activity indicators
        stars = repo.get("stargazers_count", 0)
        if stars > 1000:
            enhanced_parts.append(f"Popular project with {stars:,} stars")
        elif stars > 100:
            enhanced_parts.append(f"Active project with {stars} stars")

        # Extract key phrases from README if available
        if readme:
            # Look for common README sections
            readme_lower = readme.lower()

            # Check for key indicators
            if (
                "cli" in readme_lower
                or "command-line" in readme_lower
                or "command line" in readme_lower
            ):
                enhanced_parts.append("Command-line tool")

            if "framework" in readme_lower:
                enhanced_parts.append("Framework")
            elif "library" in readme_lower:
                enhanced_parts.append("Library")

            if "api" in readme_lower and (
                "rest" in readme_lower or "graphql" in readme_lower
            ):
                enhanced_parts.append("Provides API functionality")

        return (
            " | ".join(enhanced_parts)
            if enhanced_parts
            else "No description available"
        )

    def extract_metadata(
        self,
        repo: Dict,
        include_readme: bool = False,
        include_languages: bool = False,
        enhance_description: bool = False,
    ) -> Dict:
        """
        Extract relevant metadata from repository data

        Args:
            repo: Repository data from GitHub API
            include_readme: Whether to fetch and include README content
            include_languages: Whether to fetch language breakdown
            enhance_description: Whether to generate enhanced description

        Returns:
            Dictionary with extracted metadata
        """
        metadata = {
            "repository": repo["full_name"],
            "owner": repo["owner"]["login"],
            "name": repo["name"],
            "github_url": repo["html_url"],
            "description": repo.get("description", ""),
            "language": repo.get("language"),
            "topics": repo.get("topics", []),
            "stars": repo["stargazers_count"],
            "forks": repo["forks_count"],
            "watchers": repo.get("watchers_count", 0),
            "open_issues": repo.get("open_issues_count", 0),
            "created_at": repo["created_at"],
            "updated_at": repo["updated_at"],
            "pushed_at": repo.get("pushed_at"),
            "homepage": repo.get("homepage"),
            "license": repo.get("license", {}).get("name")
            if repo.get("license")
            else None,
            "archived": repo.get("archived", False),
            "fork": repo.get("fork", False),
            "default_branch": repo.get("default_branch", "main"),
            "has_issues": repo.get("has_issues", False),
            "has_wiki": repo.get("has_wiki", False),
            "has_pages": repo.get("has_pages", False),
        }

        readme_content = None
        if include_readme:
            readme_content = self.fetch_readme(
                repo["owner"]["login"], repo["name"]
            )
            if readme_content:
                # Truncate to first 2000 characters to keep manageable for AI
                metadata["readme_preview"] = readme_content[:2000]

        # Fetch language breakdown
        if include_languages:
            languages = self.fetch_languages(
                repo["owner"]["login"], repo["name"]
            )
            if languages:
                # Calculate percentages
                total_bytes = sum(languages.values())
                language_percentages = {
                    lang: round((bytes_count / total_bytes) * 100, 1)
                    for lang, bytes_count in languages.items()
                }
                metadata["languages"] = language_percentages

        # Generate enhanced description
        if enhance_description:
            metadata["enhanced_description"] = (
                self.generate_enhanced_description(repo, readme_content)
            )

        return metadata

    def scan(
        self,
        output_file: Optional[str] = None,
        per_page: int = 100,
        max_pages: Optional[int] = None,
        include_readme: bool = False,
        include_languages: bool = False,
        enhance_description: bool = False,
        limit: Optional[int] = None,
    ) -> Dict:
        """
        Scan starred repositories and generate output

        Args:
            output_file: Path to save JSON output
                        (default: auto-generated in results/)
            per_page: Results per page for API calls
            max_pages: Maximum pages to fetch
            include_readme: Whether to fetch README previews
            include_languages: Whether to fetch language breakdown
            enhance_description: Whether to generate enhanced descriptions
            limit: Maximum number of repositories to process

        Returns:
            Dictionary with scan results
        """
        # Fetch repositories
        repos = self.fetch_starred_repos(
            per_page=per_page, max_pages=max_pages
        )

        # Apply limit if specified
        if limit:
            repos = repos[:limit]

        # Extract metadata
        print(f"Processing {len(repos)} repositories...", file=sys.stderr)
        repositories = []

        for i, repo in enumerate(repos, 1):
            if i % 10 == 0:
                print(
                    f"Processed {i}/{len(repos)} repositories...",
                    file=sys.stderr,
                )

            metadata = self.extract_metadata(
                repo,
                include_readme=include_readme,
                include_languages=include_languages,
                enhance_description=enhance_description,
            )
            repositories.append(metadata)

        # Create output structure
        from datetime import timezone

        output = {
            "scan_date": datetime.now(timezone.utc).isoformat() + "Z",
            "total_repositories": len(repositories),
            "username": self.username or "authenticated_user",
            "repositories": repositories,
        }

        # Generate default output filename if not specified
        if not output_file:
            from datetime import timezone

            timestamp = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
            username = self.username or "authenticated_user"
            output_file = f"results/starred_repos_{username}_{timestamp}.json"

        # Save to file
        output_dir = os.path.dirname(output_file)
        if output_dir:
            os.makedirs(output_dir, exist_ok=True)
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(output, f, indent=2, ensure_ascii=False)
        print(f"Results saved to {output_file}", file=sys.stderr)

        return output


def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(
        description="Scan GitHub starred repositories and extract metadata",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Scan your own starred repos (requires GITHUB_TOKEN)
  python scan_starred_repos.py --output data/starred-repos.json

  # Scan specific user's starred repos (public)
  python scan_starred_repos.py --username octocat --output octocat-stars.json

  # Limit to first 50 repositories
  python scan_starred_repos.py --limit 50 --output sample.json

  # Include README previews (slower)
  python scan_starred_repos.py --include-readme --limit 10

  # Get AI-powered recommendations for current project
  python scan_starred_repos.py --recommend

  # Get recommendations with custom parameters
  python scan_starred_repos.py --recommend --project-path /path/to/project \\
      --recommend-output recommendations.md
        """,
    )

    parser.add_argument(
        "--output",
        "-o",
        help="Output JSON file path (default: print to stdout)",
    )
    parser.add_argument(
        "--username",
        "-u",
        help="GitHub username to scan (defaults to authenticated user)",
    )
    parser.add_argument(
        "--token",
        "-t",
        help="GitHub personal access token (or set GITHUB_TOKEN env var)",
    )
    parser.add_argument(
        "--per-page",
        type=int,
        default=100,
        help="Results per page (max 100, default: 100)",
    )
    parser.add_argument(
        "--max-pages", type=int, help="Maximum pages to fetch (default: all)"
    )
    parser.add_argument(
        "--limit",
        "-l",
        type=int,
        help="Maximum number of repositories to process",
    )
    parser.add_argument(
        "--include-readme",
        action="store_true",
        help="Fetch and include README previews (slower)",
    )
    parser.add_argument(
        "--include-languages",
        action="store_true",
        help="Fetch language breakdown for each repository",
    )
    parser.add_argument(
        "--enhance-description",
        action="store_true",
        help="Generate enhanced descriptions using metadata analysis",
    )
    parser.add_argument(
        "--recommend",
        action="store_true",
        help="Generate AI-powered repository recommendations",
    )
    parser.add_argument(
        "--project-path",
        default=".",
        help="Path to project for recommendation analysis (default: current)",
    )
    parser.add_argument(
        "--recommend-output",
        help="Output file for recommendations (default: stdout)",
    )
    parser.add_argument(
        "--recommend-format",
        choices=["markdown", "text"],
        default="markdown",
        help="Format for recommendations report",
    )
    parser.add_argument(
        "--recommend-top-n",
        type=int,
        default=10,
        help="Number of recommendations per category (default: 10)",
    )
    parser.add_argument(
        "--recommend-min-score",
        type=float,
        default=30.0,
        help="Minimum recommendation score 0-100 (default: 30.0)",
    )

    args = parser.parse_args()

    # Handle recommendation mode
    if args.recommend:
        # Import recommender module
        try:
            from repo_recommender import RepositoryRecommender
        except ImportError:
            print(
                "Error: repo_recommender module not found. "
                "Make sure repo_recommender.py is in the same directory."
            )
            sys.exit(1)

        # Helper: find latest starred_repos file in results/
        def find_latest_results_file(
            username_hint: Optional[str] = None,
        ) -> Optional[str]:
            results_dir = os.path.join(os.getcwd(), "results")
            if not os.path.isdir(results_dir):
                return None
            candidates = []
            for name in os.listdir(results_dir):
                if name.startswith("starred_repos_") and name.endswith(
                    ".json"
                ):
                    if username_hint and username_hint not in name:
                        # still allow other files if none match username later
                        pass
                    candidates.append(os.path.join(results_dir, name))
            if not candidates:
                return None
            # return newest by modification time
            candidates.sort(key=lambda p: os.path.getmtime(p), reverse=True)
            return candidates[0]

        # Determine starred repos file: prefer explicit output, then latest in results/, else run a quick scan to produce one
        starred_file = None
        if args.output:
            starred_file = args.output
        else:
            # try to find latest results file
            username_hint = None
            # if username provided, use it as hint
            if args.username:
                username_hint = args.username
            starred_file = find_latest_results_file(username_hint)

        # If we still don't have a file, run a scan to produce one
        if not starred_file or not os.path.exists(starred_file):
            print(
                "No existing starred repos file found; running a quick scan to generate one...",
                file=sys.stderr,
            )
            scanner = StarredRepoScanner(
                token=args.token, username=args.username
            )
            # run a short scan (honor other flags)
            scanner.scan(
                output_file=None,
                per_page=args.per_page,
                max_pages=args.max_pages,
                include_readme=args.include_readme,
                include_languages=args.include_languages,
                enhance_description=args.enhance_description,
                limit=args.limit,
            )
            # find the newest file now
            starred_file = find_latest_results_file(args.username)

        if not starred_file or not os.path.exists(starred_file):
            print(
                "Error: Could not locate or create starred repos file."
                " Run the scanner first (without --recommend) or provide --output path.",
                file=sys.stderr,
            )
            sys.exit(1)

        print(f"Using starred repos file: {starred_file}")

        # Create recommender and generate recommendations
        recommender = RepositoryRecommender()
        recommendations = recommender.recommend(
            starred_repos_file=starred_file,
            project_path=args.project_path,
            top_n=args.recommend_top_n,
            min_score=args.recommend_min_score,
        )

        # Generate report
        report = recommender.generate_report(
            recommendations, args.recommend_format
        )

        # Output report to file if requested, otherwise recommender will auto-save
        if args.recommend_output:
            output_path = args.recommend_output
            output_dir = os.path.dirname(output_path)
            if output_dir:
                os.makedirs(output_dir, exist_ok=True)
            with open(output_path, "w", encoding="utf-8") as f:
                f.write(report)
            print(f"\nRecommendations saved to {output_path}")
        else:
            # Let recommender module handle default saving behavior by saving here to results/
            from datetime import datetime, timezone

            timestamp = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
            ext = "md" if args.recommend_format == "markdown" else "txt"
            default_path = os.path.join(
                "results", f"recommendations_{timestamp}.{ext}"
            )
            os.makedirs(os.path.dirname(default_path), exist_ok=True)
            with open(default_path, "w", encoding="utf-8") as f:
                f.write(report)
            print(f"\nRecommendations saved to {default_path}")

        return

    # Create scanner
    scanner = StarredRepoScanner(token=args.token, username=args.username)

    # Run scan
    results = scanner.scan(
        output_file=args.output,
        per_page=args.per_page,
        max_pages=args.max_pages,
        include_readme=args.include_readme,
        include_languages=args.include_languages,
        enhance_description=args.enhance_description,
        limit=args.limit,
    )

    # Print to stdout if no output file specified
    if not args.output:
        print(json.dumps(results, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
