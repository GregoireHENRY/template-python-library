#!/usr/bin/env bash

CHECK_MARK="$(tput setaf 2)✔$(tput sgr0)"

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
echo "Install poetry dependencies in a virtual environments.."
poetry install
echo " $CHECK_MARK" && TOTAL_CHECKS=$TOTAL_CHECKS$CHECK_MARK

# Add pre-commit tool
echo -n "Install pre-commit hooks.."
poetry run pre-commit install
echo " $CHECK_MARK" && TOTAL_CHECKS=$TOTAL_CHECKS$CHECK_MARK

# First commit
echo "Write the first commit on a development branch.."
git add .
git branch -M main
git checkout -b dev
git commit -m "🎉 {{cookiecutter.project_name}} first commit"
echo " $CHECK_MARK" && TOTAL_CHECKS=$TOTAL_CHECKS$CHECK_MARK

echo ""
echo "🌟✨ It's done! $TOTAL_CHECKS"
echo ""

# Final setup (to do "a la mano")
echo "Now you can move into your project:
$(tput setaf 3)$ $(tput setaf 2)cd $(tput setaf 6){{cookiecutter.repo_name}}$(tput sgr0)

If you want your repo to be hosted online on your GitHub account, create an online repo named\
 $(tput setaf 6){{cookiecutter.project_name}}$(tput sgr0) and after that set the SSH remote url:
$(tput setaf 3)$ $(tput setaf 2)git remote add origin git@github.com:$(tput setaf 1)USERNAME\
$(tput setaf 2)/$(tput setaf 6){{cookiecutter.project_name}}$(tput setaf 2).git$(tput sgr0)
Then publish your commits on the development branch:
$(tput setaf 3)$ $(tput setaf 2)git push origin dev$(tput sgr0)
You can merge and publish your updates to the main branch when you are ready:
$(tput setaf 3)$ $(tput setaf 2)git checkout main$(tput sgr0)
$(tput setaf 3)$ $(tput setaf 2)git merge dev$(tput sgr0)
$(tput setaf 3)$ $(tput setaf 2)git push origin main$(tput sgr0)
Do not forget to go back to the development branch immediately afterwards:
$(tput setaf 3)$ $(tput setaf 2)git checkout dev$(tput sgr0)"
