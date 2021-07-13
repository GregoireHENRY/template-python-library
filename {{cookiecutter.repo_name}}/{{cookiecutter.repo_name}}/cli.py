#!/usr/bin/env python3

"""
{{cookiecutter.project_name}}
"""


from pathlib import Path
from typing import Any

import click
import envtoml
from dotmap import DotMap
from pudb import set_trace as bp  # noqa: F401

from {{cookiecutter.repo_name}} import core

MANIFEST_FILE = Path("pyproject.toml")
MANIFEST = DotMap(envtoml.load(MANIFEST_FILE.open()))
NAME = MANIFEST.tool.poetry.name
VERSION = MANIFEST.tool.poetry.version
CONTEXT_SETTINGS = dict(help_option_names=["-h", "--help"])


def print_version(ctx: Any, param: Any, value: Any) -> None:
    """Show version."""
    if not value or ctx.resilient_parsing:
        return
    click.echo(VERSION)
    ctx.exit()


@click.group(context_settings=CONTEXT_SETTINGS, invoke_without_command=True)
@click.option(
    "-v",
    "--version",
    is_flag=True,
    callback=print_version,
    expose_value=False,
    is_eager=True,
    help="Show version",
)
def cli() -> None:
    """
    {{cookiecutter.project_name}} description.
    """
    core.start()


def main() -> None:
    cli(prog_name=NAME)


if __name__ == "__main__":
    main()
