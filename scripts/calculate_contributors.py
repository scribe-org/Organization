# SPDX-License-Identifier: GPL-3.0-or-later
"""
Calculate Top Contributors for Scribe Community Spotlight
Fetches commit data from GitHub for Scribe projects over the past 30 days
  (25th of last month to 25th of current month), calculates top contributors,
  and formats a message for the Matrix channel.
Run via GitHub Actions workflow. Requires GITHUB_TOKEN environment variable.
"""

import requests
from datetime import datetime
from collections import defaultdict
import os

ORG = "scribe-org"   
TOP_N = 5  

def get_date_range():
    """
    Calculate the date range: 25th of last month to 25th of current month.
    """
    today = datetime.today()
    start_month = today.month - 1 if today.month > 1 else 12
    start_year = today.year if today.month > 1 else today.year - 1
    start_date = datetime(start_year, start_month, 25)
    end_date = datetime(today.year, today.month, 25)
    return start_date, end_date

def get_repos():
    """
    Fetch all repository names for the organization.
    """
    repos = []
    page = 1
    headers = {"Authorization": f"token {os.getenv('GITHUB_TOKEN')}"}
    
    while True:
        url = f"https://api.github.com/orgs/{ORG}/repos?per_page=100&page={page}"
        r = requests.get(url, headers=headers)
        if r.status_code != 200:
            print(f"Error fetching repos: {r.status_code} {r.text}")
            break
        data = r.json()
        if not data:
            break
        repos += [repo["name"] for repo in data]
        page += 1
    return repos

def get_commits(repo, start_date, end_date):
    """
    Fetch commits for a repository within the date range.
    """
    commits = []
    page = 1
    headers = {"Authorization": f"token {os.getenv('GITHUB_TOKEN')}"}
    
    while True:
        url = (f"https://api.github.com/repos/{ORG}/{repo}/commits?"
               f"since={start_date.isoformat()}Z&until={end_date.isoformat()}Z&per_page=100&page={page}")
        r = requests.get(url, headers=headers)
        if r.status_code != 200:
            print(f"Error fetching commits for {repo}: {r.status_code}")
            break
        data = r.json()
        if not isinstance(data, list) or not data:
            break
        commits += data
        page += 1
    return commits

def main():
    """
    Calculate top contributors and format the Community Spotlight message.
    """
    # Initialize contributor tracking.
    contribution_count = defaultdict(int)
    
    # Get date range and repositories.
    start_date, end_date = get_date_range()
    repos = get_repos()

    # Count commits per author.
    for repo in repos:
        commits = get_commits(repo, start_date, end_date)
        for commit in commits:
            author = commit.get("author")
            if author and author.get("login"):
                contribution_count[author["login"]] += 1

    # Sort contributors by commit count.
    top_contributors = sorted(contribution_count.items(), key=lambda x: x[1], reverse=True)

    # Build the message.
    message = (
        "👥 **Community Spotlight Reminder** 🙌\n\n"
        "Here are the top GitHub contributors to all **Scribe** projects from "
        f"**{start_date.strftime('%B %d')}** to **{end_date.strftime('%B %d')}**:\n\n"
    )
    for user, count in top_contributors[:TOP_N]:
        message += f"- [{user}](https://github.com/{user}) ({count} commits)\n"

    message += (
        "\n💬 Please reply in the thread with who you think should be spotlighted this month!\n"
        "We'll reach out to them for a short message and LinkedIn tag before posting. 💙\n"
    )

    # Write message to file for reference.
    with open("message.txt", "w") as f:
        f.write(message)

    # Set GitHub Actions output.
    with open(os.getenv("GITHUB_OUTPUT"), "a") as f:
        f.write(f"message<<EOF\n{message}\nEOF\n")

    # Log summary for debugging.
    with open(os.getenv("GITHUB_STEP_SUMMARY"), "a") as f:
        f.write("**Community Spotlight Summary** 🟢\n")
        f.write(f"Date Range: {start_date.strftime('%Y-%m-%d')} to {end_date.strftime('%Y-%m-%d')}\n")
        f.write(f"Repositories Scanned: {len(repos)}\n")
        f.write("Top Contributors:\n")
        for user, count in top_contributors[:TOP_N]:
            f.write(f"- {user}: {count} commits\n")
        f.write("\nMessage prepared for Matrix channel.\n")

if __name__ == "__main__":
    main()
 