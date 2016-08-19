"""
"""
import os.path
import git

REPO_ROOT = os.path.abspath(os.path.dirname(__file__))
DATA_DIR = os.path.join(REPO_ROOT, 'data')
CURRENT_EXECUTION_VERSION = 14
NEW_AND_MODIFIED = '.'
REMOVED = '-A'
COMMIT_MSG='-m "Automated commit {index}. Printing push output."'.format(index=CURRENT_EXECUTION_VERSION)
VERSION_TAG = 'v1.0.{build}'.format(build=CURRENT_EXECUTION_VERSION)


print("Repo root: " + REPO_ROOT)
print("Data directory: " + DATA_DIR)

repo = git.Repo(REPO_ROOT)
git_driver = repo.git

# Making some changes that we can commit.
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

# Adding new and modified, and deleting removed files from the repo.
print('Adding new and modified....')
git_driver.add(NEW_AND_MODIFIED)
print('Removing deleted from tree....')
git_driver.add(REMOVED)
print(git_driver.status())
print('Committing changes....')
print(git_driver.commit(COMMIT_MSG))

# Let's tag this version if the tag doesn't exist and push it preventing override.
if VERSION_TAG not in repo.tags:
    print('Tagging repository with: {tag}....'.format(tag=VERSION_TAG))
    repo.create_tag(VERSION_TAG, message='Annotated tag {version}'.format(version=VERSION_TAG))
    print('Pushing changes....')
    git_driver.push('--follow-tags')



