"""
"""
import os.path
import git

REPO_ROOT = os.path.abspath(os.path.dirname(__file__))
DATA_DIR = os.path.join(REPO_ROOT, 'data')
CURRENT_EXECUTION_VERSION = 4


print("Repo root: " + REPO_ROOT)
print("Data directory: " + DATA_DIR)

repo = git.Repo(REPO_ROOT)
git_driver = repo.git

# Create a new file and commit it to the repo.
new_file = os.path.join(DATA_DIR, "created {number}.txt".format(number=CURRENT_EXECUTION_VERSION))
old_file = os.path.join(DATA_DIR, "created {number}.txt".format(number=CURRENT_EXECUTION_VERSION-1))
with open(new_file, mode='w') as fout:
    contents = "Created file {number}".format(number=CURRENT_EXECUTION_VERSION)
    fout.write(contents)

if os.path.exists(old_file):
    print("Removing file: " + old_file)
    os.remove(old_file)


print("Repo is dirty: " + repr(repo.is_dirty()))
print('Adding new and modified....')
git_driver.add('.')
print('Removing deleted from tree....')
git_driver.add('-A')
print('Committing changes....')
git_driver.commit('-m "Execution {index}"'.format(index=CURRENT_EXECUTION_VERSION))
