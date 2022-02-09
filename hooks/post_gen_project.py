#!/usr/bin/env python

"""
Finish cookiecutter build.
"""

import subprocess
from pathlib import Path  # noqa:F401
from typing import Optional  # noqa:F401

import sh
from pudb import set_trace as bp  # noqa:F401


def run(COMMAND: str, OUTPUT: bool = False) -> Optional[str]:
    if OUTPUT:
        return subprocess.check_output(COMMAND, shell=True).decode("utf-8").split("\n")[0]
    else:
        subprocess.run(COMMAND, shell=True)


def main() -> None:
    run("poetry update && poetry install")

    run("poetry add pudb click ruamel.yaml")
    run(
        "poetry add --dev pudb flake8 flake8-bugbear mypy black isort pre-commit"
        " pytest pytest-sugar pytest-cov Sphinx pydata-sphinx-theme sphinx-autoapi"
        " twine"
    )

    run("poetry run mypy --install-types --non-interactive")

    sh.git.init(".")
    sh.git.add(".")
    sh.git.branch("-M", "main")

    run("poetry run pre-commit install")
    run("poetry run git commit -m \"feat: initial commit\"")


if __name__ == "__main__":
    main()
