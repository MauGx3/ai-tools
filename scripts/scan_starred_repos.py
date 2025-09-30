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
import json
import os
import sys
from datetime import datetime
from typing import Dict, List, Optional
from urllib.parse import urljoin

try:
    import requests
except ImportError:
    print("Error: requests library is required. Install with: pip install requests")
    sys.exit(1)


class StarredRepoScanner:
    """Scanner for GitHub starred repositories"""
    
    BASE_URL = "https://api.github.com"
    
    def __init__(self, token: Optional[str] = None, username: Optional[str] = None):
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
        self, 
        per_page: int = 100, 
        max_pages: Optional[int] = None
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
                print("Error: Authentication required. Set GITHUB_TOKEN environment variable.", file=sys.stderr)
                sys.exit(1)
            elif response.status_code == 404:
                print(f"Error: User '{self.username}' not found.", file=sys.stderr)
                sys.exit(1)
            elif response.status_code != 200:
                print(f"Error: API returned status code {response.status_code}", file=sys.stderr)
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
                print(f"Warning: Only {remaining} API calls remaining", file=sys.stderr)
        
        print(f"Fetched {len(all_repos)} starred repositories", file=sys.stderr)
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
            print(f"Warning: Could not fetch README for {owner}/{repo}: {e}", file=sys.stderr)
        
        return None
    
    def extract_metadata(self, repo: Dict, include_readme: bool = False) -> Dict:
        """
        Extract relevant metadata from repository data
        
        Args:
            repo: Repository data from GitHub API
            include_readme: Whether to fetch and include README content
            
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
            "open_issues": repo.get("open_issues_count", 0),
            "created_at": repo["created_at"],
            "updated_at": repo["updated_at"],
            "pushed_at": repo.get("pushed_at"),
            "homepage": repo.get("homepage"),
            "license": repo.get("license", {}).get("name") if repo.get("license") else None,
            "archived": repo.get("archived", False),
            "fork": repo.get("fork", False),
        }
        
        if include_readme:
            readme = self.fetch_readme(repo["owner"]["login"], repo["name"])
            if readme:
                # Truncate to first 2000 characters to keep manageable for AI
                metadata["readme_preview"] = readme[:2000]
        
        return metadata
    
    def scan(
        self, 
        output_file: Optional[str] = None,
        per_page: int = 100,
        max_pages: Optional[int] = None,
        include_readme: bool = False,
        limit: Optional[int] = None
    ) -> Dict:
        """
        Scan starred repositories and generate output
        
        Args:
            output_file: Path to save JSON output
            per_page: Results per page for API calls
            max_pages: Maximum pages to fetch
            include_readme: Whether to fetch README previews
            limit: Maximum number of repositories to process
            
        Returns:
            Dictionary with scan results
        """
        # Fetch repositories
        repos = self.fetch_starred_repos(per_page=per_page, max_pages=max_pages)
        
        # Apply limit if specified
        if limit:
            repos = repos[:limit]
        
        # Extract metadata
        print(f"Processing {len(repos)} repositories...", file=sys.stderr)
        repositories = []
        
        for i, repo in enumerate(repos, 1):
            if i % 10 == 0:
                print(f"Processed {i}/{len(repos)} repositories...", file=sys.stderr)
            
            metadata = self.extract_metadata(repo, include_readme=include_readme)
            repositories.append(metadata)
        
        # Create output structure
        output = {
            "scan_date": datetime.utcnow().isoformat() + "Z",
            "total_repositories": len(repositories),
            "username": self.username or "authenticated_user",
            "repositories": repositories
        }
        
        # Save to file if specified
        if output_file:
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
        """
    )
    
    parser.add_argument(
        "--output", "-o",
        help="Output JSON file path (default: print to stdout)"
    )
    parser.add_argument(
        "--username", "-u",
        help="GitHub username to scan (defaults to authenticated user)"
    )
    parser.add_argument(
        "--token", "-t",
        help="GitHub personal access token (or set GITHUB_TOKEN env var)"
    )
    parser.add_argument(
        "--per-page",
        type=int,
        default=100,
        help="Results per page (max 100, default: 100)"
    )
    parser.add_argument(
        "--max-pages",
        type=int,
        help="Maximum pages to fetch (default: all)"
    )
    parser.add_argument(
        "--limit", "-l",
        type=int,
        help="Maximum number of repositories to process"
    )
    parser.add_argument(
        "--include-readme",
        action="store_true",
        help="Fetch and include README previews (slower)"
    )
    
    args = parser.parse_args()
    
    # Create scanner
    scanner = StarredRepoScanner(token=args.token, username=args.username)
    
    # Run scan
    results = scanner.scan(
        output_file=args.output,
        per_page=args.per_page,
        max_pages=args.max_pages,
        include_readme=args.include_readme,
        limit=args.limit
    )
    
    # Print to stdout if no output file specified
    if not args.output:
        print(json.dumps(results, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
