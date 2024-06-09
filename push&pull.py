# Author        : Eshan Roy <eshanized@proton.me>
# Author URL    : https://eshanized.github.io

# NOTE: Run at your own risk.

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

# Get the conventional commit message from the user
message = input("Enter a conventional commit message (e.g. 'feat: add a new feature'): ")

# Commit with the conventional message
commit_with_conventional_message(message)

# Pull from GitHub
pull_from_github()

# Push to GitHub
push_to_github()
