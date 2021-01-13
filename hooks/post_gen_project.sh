#!/usr/bin/env sh

set -e

CHECK_MARK="\e[32m✔\e[0m"

# Pre-run message
echo "
🚧 Cookiecutter's post-generation hook script.

Description
-----------
This script is a hook script executed after the project generation by
cookiecutter.

Notes
-----
This script must exit successfully or the project generation will be aborted.
Test on: Linux (Ubuntu 20).

Prerequesites
-------------
You must have installed these tools:
  - python3
  - pip
  - git

Execution
---------"

# Install poetry
echo -n "Check if poetry is installed.."
if ! hash poetry 2>/dev/null; then
    echo " installing..."
    python3 -m pip install --user poetry
fi
echo " $CHECK_MARK" && TOTAL_CHECKS=$TOTAL_CHECKS$CHECK_MARK

# Initialize repo
echo -n "Initialize the git repo.."
git init . -q
echo " $CHECK_MARK" && TOTAL_CHECKS=$TOTAL_CHECKS$CHECK_MARK

# Add pre-commit tool
echo -n "Add the pre-commit tool.."
poetry run pre-commit install -t pre-commit > /dev/null 2>&1
poetry run pre-commit install -t pre-push > /dev/null 2>&1
echo " $CHECK_MARK" && TOTAL_CHECKS=$TOTAL_CHECKS$CHECK_MARK

# First commit
echo "Write the first commit.."
git add .
git commit -m "🎉 {{cookiecutter.project_name}} start"
echo " $CHECK_MARK" && TOTAL_CHECKS=$TOTAL_CHECKS$CHECK_MARK

# Create main branch
echo -n "Create the main branch.."
git branch -M main
echo " $CHECK_MARK" && TOTAL_CHECKS=$TOTAL_CHECKS$CHECK_MARK

echo ""
echo "🌟✨ It's done! $TOTAL_CHECKS"
echo ""

# Final setup (to do with your bare hands)
echo "Now, create an online repo named {{cookiecutter.project_name}} and set the SSH
remote url. It should look like:
$ git remote add origin git@github.com:USERNAME/{{cookiecutter.project_name}}
Then you can use:
$ git push -u origin main
Do not forget to work on a development branch:
$ git checkout -b dev"
