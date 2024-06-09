import os
import subprocess

def commit_with_conventional_message(message):
    # Check if the commit message is conventional
    if not is_conventional(message):
        print("Error: Commit message is not conventional")
        return

    # Add all changes
    subprocess.run(["git", "add", "."])

    # Commit with the conventional message
    subprocess.run(["git", "commit", "-m", message])

def push_to_github():
    # Push to GitHub
    subprocess.run(["git", "push", "origin", "master"])

def pull_from_github():
    # Pull from GitHub
    subprocess.run(["git", "pull", "origin", "master"])

def is_conventional(message):
    # Check if the commit message is conventional
    conventional_types = ["build", "chore", "ci", "docs", "feat", "fix", "perf", "refactor", "revert", "style", "test"]
    for type in conventional_types:
        if message.startswith(f"{type}:"):
            return True
    return False

# Example usage
commit_with_conventional_message("feat: add a new feature")
push_to_github()
pull_from_github()