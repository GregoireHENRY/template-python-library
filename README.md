# Python Project Starter

This repo is a project template, improved from this [blogpost](https://sourcery.ai/blog/python-best-practices/), using [cookiecutter](https://github.com/audreyr/cookiecutter).

## Features

![pytest logo]

- Testing with [pytest](https://docs.pytest.org/en/latest)
- Formatting with [black](https://github.com/psf/black)
- Import sorting with [isort](https://github.com/timothycrosley/isort)
- Static typing with [mypy](http://mypy-lang.org)
- Linting with [flake8](https://flake8.pycqa.org/en/latest)
- Git hooks that run all the above before committing with [pre-commit](https://pre-commit.com/)

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

[pytest logo]: https://docs.pytest.org/en/latest/_static/pytest_logo_curves.svg
{: height="36px"}
