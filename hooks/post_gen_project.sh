#!/usr/bin/env sh

#
# DISCLAIMER: this script is intended for Linux (tested on Ubuntu 20)

set -e

CHECK_MARK="\e[32m✔\e[0m"

read -r -d '' PRE_RUN_MESSAGE <<- EOM
    🚧 Cookiecutter's post-generation hook script.

    ## Description
    ==============

    This script is a hook script executed after the project generation by
    cookiecutter.

    ## Notes
    ========

    This script must exit successfully or the project generation will be aborted.

    Test on: Linux (Ubuntu 20).

    ## Prerequesites
    ================

    You must have installed these tools:
      - python3
      - pip
      - git

    ## EXECUTION
    ============

EOM

# Pre-run message
echo $PRE_RUN_MESSAGE

# Install poetry
echo -n "Check if poetry is installed.."
if ! hash poetry 2>/dev/null; then
    echo " installing..."
    python3 -m pip install --user poetry
fi
echo " $CHECK_MARK" && TOTAL_CHECKS=$TOTAL_CHECKS$CHECK_MARK

# Initialize repo
echo -n "Initialize the git repo.."
git init .
echo " $CHECK_MARK" && TOTAL_CHECKS=$TOTAL_CHECKS$CHECK_MARK

# Add pre-commit tool
echo -n "Add the pre-commit tool.."
poetry run pre-commit install -t pre-commit
poetry run pre-commit install -t pre-push
echo " $CHECK_MARK" && TOTAL_CHECKS=$TOTAL_CHECKS$CHECK_MARK

# First commit
echo -n "First commit.."
git add --all
git commit -m "🎉 {{cookiecutter.project_name}} start"
echo " $CHECK_MARK" && TOTAL_CHECKS=$TOTAL_CHECKS$CHECK_MARK

# Create main branch
echo -n "First commit.."
git branch -M main
echo " $CHECK_MARK" && TOTAL_CHECKS=$TOTAL_CHECKS$CHECK_MARK

echo "🌟✨ It's done! $TOTAL_CHECKS"

# Final setup (to do with your bare hands)
echo "Now, create a repo online named {{cookiecutter.project_name}} and set the SSH remote url. It should look like:"
echo "$ git remote add origin git@github.com:USERNAME/{{cookiecutter.project_name}}"
echo "Then you can use:"
echo "$ git push -u origin main"
echo "Do not forget to work on a development branch:"
echo "$ git checkout -b dev"
