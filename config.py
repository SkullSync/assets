import git

repo = git.Repo()

name = input("Please provide your name (e.g., Eshan Roy): ")
email = input("Please provide your email address (e.g., eshanized@proton.me): ")

with repo.config_writer() as cw:
    cw.set_value("user", "name", name)
    cw.set_value("user", "email", email)

print("Git configuration setup successfully!")