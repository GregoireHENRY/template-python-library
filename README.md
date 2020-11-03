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
python3 -m pip install pipx
python3 -m pipx ensurepath
pipx install pipenv

pipx run cookiecutter gh:GregoireHENRY/python-starter-template

cd <repo_name>
git init
pipenv install --dev
pipenv run pre-commit install -t pre-commit
pipenv run pre-commit install -t pre-push
```
