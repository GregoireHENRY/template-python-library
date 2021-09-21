# Template for Python Libraries

> Template using [`cookiecutter`][cookiecutter url] for Python libraries to be
> upload on [pypi][pypi url].

## Features

+ tests with [`pytest`][pytest url]
+ fixers for code with [`black`][black url] and imports with [`isort`][isort url]
+ linting with [`flake8`][flake8 url]
+ type checking with [`mypy`][mypy url]
+ git commit checking with [`pre-commit`][pre-commit url]
+ dependency management & packaging with [`poetry`][poetry url]

## Quickstart

```sh
pipx install cookiecutter
```

to install `cookiecutter` using [`pipx`][pipx url]. The template uses
[Python3.9][python url], so check your `pipx` versions.

```sh
cookiecutter gh:GregoireHENRY/template-python-library
```

to create your project from this template.

[python badge]: https://img.shields.io/badge/python-^3.9-blue
[python url]: https://www.python.org/
[pypi url]: https://pypi.org
[pipx url]: https://github.com/pypa/pipx
[cookiecutter url]: https://github.com/audreyr/cookiecutter
[pre-commit url]: https://pre-commit.com
[poetry url]: https://python-poetry.org/docs
[flake8 url]: https://flake8.pycqa.org/en/latest
[isort url]: https://github.com/timothycrosley/isort
[mypy url]: http://mypy-lang.org
[black url]: https://github.com/psf/black
[pytest url]: https://docs.pytest.org/en/latest
