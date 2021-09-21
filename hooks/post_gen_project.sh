#!/usr/bin/env bash

CHECK_MARK="$(tput setaf 2)✔$(tput sgr0)"

echo "
🚧 $(tput bold)Cookiecutter$(tput sgr0)'s post-generation hook script.

$(tput smul)Prerequisites$(tput rmul)
You must have installed poetry with pipx and Python3.9.

$(tput smul)Execution$(tput rmul)"
# Install poetry dependencies in a virtual environments.
poetry env use 3.9
poetry update
poetry install

# Initialize the git repo.
git init .
git add .

# Install & initialize pre-commit hooks.
poetry run pre-commit install
poetry run pre-commit >&/dev/null

# Write the first commit.
git add .
git commit -m "🎉 {{cookiecutter.project_name}} initial commit"
git branch -M main

echo ""
echo "🌟✨ {{cookiecutter.project_name}} created!"
echo ""
