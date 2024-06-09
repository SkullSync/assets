# Author        : Eshan Roy <eshanized@proton.me>
# Author URL    : https://eshanized.github.io

# NOTE: Run at your own risk!

# allows us to spawn new processes, connect to their input/output/error pipes, 
# and obtain their return codes.
import subprocess

# handle pulling changes from the remote repository
def git_pull():
    # catch any errors that occur within the block
    try:
        # executes the git pull origin master command using the subprocess.check_call function
        subprocess.check_call(
            [
                'git', 
                'pull', 
                'origin', 
                'master',
            ]
        )
        print(
            "Pull successful"
        )
    # catches any errors that occur during the execution of the git pull command
    except subprocess.CalledProcessError:
        print(
            "Error pulling from remote repository"
        )

# handles pushing changes to the remote repository
def git_push(commit_message):
    try:
        subprocess.check_call(
            [
                'git', 
                'add', 
                '.'
            ]
        )
        subprocess.check_call(
            [
                'git', 
                'commit', 
                '-m', 
                commit_message,
            ]
        )
        subprocess.check_call(
            [
                'git', 
                'push', 
                'origin', 
                'master',
            ]
        )
        print(
            "Push successful"
        )
    except subprocess.CalledProcessError:
        print(
            "Error pushing to remote repository"
        )

# Execution
git_pull()
# prompts the user to input a commit message, 
# which will be used when committing the changes to the local repository
commit_message = input("Enter commit message: ")
# calls the git_push() function, 
# passing the commit message entered by the user as an argument
git_push(commit_message)
