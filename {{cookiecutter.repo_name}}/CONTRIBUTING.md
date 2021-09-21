# Contributing to **{{cookiecutter.project_name}}**

## Contributing to code

### Local development

You will need the source of **{{cookiecutter.project_name}}** to start
contributing on the codebase. You will need to fork the project, clone your
forked repository and place yourself in its directory.

> If you are new to GitHub collaboration, you can refer to the
> [Forking Projects Guide][github fork guide].

Replace the URL to match your forked repository.

```sh
git clone git@github.com:USERNAME/{{cookiecutter.project_name}}.git
cd rust-spice
```

**{{cookiecutter.project_name}}** depends on [poetry][poetry url] for dependency
management and packaging. You need to install the dependencies in the
configured virtual environment and activate it.

**{{cookiecutter.project_name}}** uses [`pre-commit`][pre-commit url] to make
sure that you don't accidentally commit code that does not follow the coding
style. This runs the tests with [pytest][pytest url], checks basic filesystem
and git related guidelines and run python analysis tools. It uses
[flake8][flake8 url] as a static linter, [mypy][mypy url] to check types,
[isort][isort url] to sort the imports and [black][black url] to format the
code.

```sh
pre-commit install
```

to install the hook script to check before commits.

### Merge requests

The main branch (`main`) is the version of the code users get when they install
the library or the executable. The development branch (`dev`) is where the code
gets updated and validated before being merged into the main branch (`main`).

Thus, all merge requests, unless otherwise instructed, need to be accepted into
the development branch (`dev`).

Be sure that your merge request contains tests and documentation that covers the
changed or added code.

*Thank you for your time contributing!!*

[pre-commit url]: https://pre-commit.com
[poetry url]: https://python-poetry.org/docs
[pytest url]: https://docs.pytest.org/en/latest
[flake8 url]: https://flake8.pycqa.org/en/latest
[mypy url]: http://mypy-lang.org
[isort url]: https://github.com/timothycrosley/isort
[black url]: https://github.com/psf/black
[gitlab fork guide]: https://docs.gitlab.com/ee/user/project/repository/forking_workflow.html#creating-a-fork
[github fork guide]: https://guides.github.com/activities/forking
