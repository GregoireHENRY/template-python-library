#!/usr/bin/env sh

set -e

CHECK_MARK="\e[32m✔\e[0m"

# Pre-run message
echo "
🚧  $(tput bold)Cookiecutter$(tput sgr0)'s post-generation hook script.

$(tput smul)Description$(tput rmul)
This script is a hook script executed after the project generation by
cookiecutter.

$(tput smul)Notes$(tput rmul)
This script must exit successfully or the project generation will be aborted.
Test on: Linux (Ubuntu 20).

$(tput smul)Prerequisites$(tput rmul)
You must have installed these tools:
  - python3
  - pip
  - git

$(tput smul)Execution$(tput rmul)"

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

# Install poetry dependencies
echo "Install poetry dependencies.."
poetry install
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
echo "Now, create an online repo named $(tput setaf 6){{cookiecutter.project_name}}$(tput sgr0) and set the SSH remote url.
But first, move to your repo:
$(tput setaf 3)$ $(tput setaf 2)cd $(tput setaf 6){{cookiecutter.repo_name}}$(tput sgr0)
The command to add the your url, after having created the repo online, is:
$(tput setaf 3)$ $(tput setaf 2)git remote add origin git@github.com:$(tput setaf 1)USERNAME$(tput setaf 2)/$(tput setaf 6){{cookiecutter.project_name}}$(tput setaf 2).git$(tput sgr0)
Then you can use:
$(tput setaf 3)$ $(tput setaf 2)git push -u origin main$(tput sgr0)
Do not forget to work on a development branch:
$(tput setaf 3)$ $(tput setaf 2)git checkout -b dev$(tput sgr0)$(tput bel)"
