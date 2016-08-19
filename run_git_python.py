"""
"""
import os.path
import git

REPO_ROOT = os.path.abspath(os.path.dirname(__file__))
DATA_DIR = os.path.join(REPO_ROOT, 'data')
CURRENT_EXECUTION_VERSION = 10
NEW_AND_MODIFIED = '.'
REMOVED = '-A'
COMMIT_MSG='-m "Automated commit {index}. Printing push output."'.format(index=CURRENT_EXECUTION_VERSION)


print("Repo root: " + REPO_ROOT)
print("Data directory: " + DATA_DIR)

repo = git.Repo(REPO_ROOT)
git_driver = repo.git

# Create a new file and commit it to the repo.
new_file = os.path.join(DATA_DIR, "created {number}.txt".format(number=CURRENT_EXECUTION_VERSION))
old_file = os.path.join(DATA_DIR, "created {number}.txt".format(number=CURRENT_EXECUTION_VERSION-1))
modifiable_file = os.path.join(DATA_DIR, "modifiable.txt".format(number=CURRENT_EXECUTION_VERSION-1))
with open(new_file, mode='w') as fout:
    contents = "Created file {number}".format(number=CURRENT_EXECUTION_VERSION)
    fout.write(contents)

with open(modifiable_file, mode='a') as fout:
    contents = "Modified {number} times.\n".format(number=CURRENT_EXECUTION_VERSION)
    fout.write(contents)

if os.path.exists(old_file):
    print("Removing file: " + old_file)
    os.remove(old_file)


print("Repo is dirty: " + repr(repo.is_dirty()))
print('Adding new and modified....')
print(git_driver.add(NEW_AND_MODIFIED))
print('Removing deleted from tree....')
print(git_driver.add(REMOVED))
print('Committing changes....')
print(git_driver.commit(COMMIT_MSG))
print('Pushing changes....')
print(git_driver.push())

