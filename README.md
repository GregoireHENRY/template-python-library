# Python Project Starter

This repo is a project template, improved from this [blogpost](https://sourcery.ai/blog/python-best-practices/), using [cookiecutter](https://github.com/audreyr/cookiecutter).

## Features

- Testing with [pytest](https://docs.pytest.org/en/latest/)
- Formatting with [black](https://github.com/psf/black)
- Import sorting with [isort](https://github.com/timothycrosley/isort)
- Static typing with [mypy](http://mypy-lang.org/)
- Linting with [pylint](https://www.pylint.org/)
- Git hooks that run all the above with [pre-commit](https://pre-commit.com/)

## Quickstart

```sh
# Install cookiecutter
pip install --user cookiecutter

# Create your project from a template 
cookiecutter gh:GregoireHENRY/python-starter-template

# Install poetry
pip install --user poetry

# Initialize your repo
cd <repo_name>
git init

# pipenv run pre-commit install -t pre-commit
# pipenv run pre-commit install -t pre-push
```
