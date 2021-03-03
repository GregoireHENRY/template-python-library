# Python Project Starter

This repo is a project template, improved from this [blogpost](https://sourcery.ai/blog/python-best-practices/), using [cookiecutter](https://github.com/audreyr/cookiecutter).

## Features

<p align="center">
    <img src="https://docs.pytest.org/en/latest/_static/pytest_logo_curves.svg" height="50px" padding="0px">
    <img src="https://black.readthedocs.io/en/stable/_static/logo2.png" height="50px" padding="4px 20px 6px">
    <img src="https://pycqa.github.io/isort/art/logo.png" height="50px" padding="4px 10px 14px">
    <img src="https://camo.githubusercontent.com/20e0f72b4f84dc5b42aceb95eb8eaa6c574746c0057e9e2525dd6cb4797d565f/687474703a2f2f6d7970792d6c616e672e6f72672f7374617469632f6d7970795f6c696768742e737667" height="50px" padding="6px 30px 12px">
    <img src="rsc/img/flake8.png" height="50px" padding="8px 0px 16px">
    <img src="https://pre-commit.com/logo.svg" height="50px" padding="4px 34px 10px">
    <img src="https://python-poetry.org/images/logo-origami.svg" height="50px" padding="6px 16px 10px">
</p>

- Testing with [pytest](https://docs.pytest.org/en/latest)
- Formatting with [black](https://github.com/psf/black)
- Import sorting with [isort](https://github.com/timothycrosley/isort)
- Static typing with [mypy](http://mypy-lang.org)
- Linting with [flake8](https://flake8.pycqa.org/en/latest)
- Git hooks that run all the above before committing with [pre-commit](https://pre-commit.com/)
- Virtual environment dependencies & PyPI publish [poetry](https://python-poetry.org/)

## Quickstart

```bash
# Get yourself cookiecutter
pip install --user cookiecutter

# Create your project from a template 
cookiecutter gh:GregoireHENRY/python-starter-template

# Or from local template
cookiecutter python-starter-template/
```

Voilà! ✨
You can see an example [here](https://github.com/GregoireHENRY/test-python-starter).
