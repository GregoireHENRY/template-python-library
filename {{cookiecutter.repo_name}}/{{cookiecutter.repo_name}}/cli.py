#!/usr/bin/env python

"""
{{cookiecutter.project_name}} command line interface.
"""

from pathlib import Path  # noqa:F401
from typing import Any  # noqa:F401

import click
from pudb import set_trace as bp  # noqa:F401

import {{cookiecutter.project_name}}  # noqa:F401

CONTEXT_SETTINGS = dict(help_option_names=["-h", "--help"])


def version(ctx: Any, param: Any, value: Any) -> None:
    if not value or ctx.resilient_parsing:
        return
    click.echo({{cookiecutter.project_name}}.__version__)
    ctx.exit()


@click.group(context_settings=CONTEXT_SETTINGS, invoke_without_command=True)
@click.pass_context
@click.option(
    "-v",
    "--version",
    is_flag=True,
    callback=version,
    expose_value=False,
    is_eager=True,
    help="Show version.",
)
def cli(ctx: click.Context) -> None:
    """{{cookiecutter.project_name}} command line interface."""
    # Share default command options.
    # ctx.obj["var"] = var
    ctx.ensure_object(dict)

    if ctx.invoked_subcommand is None:
        click.echo(ctx.get_help())
        ctx.exit()


def main() -> None:
    cli(prog_name=Path().parent)


if __name__ == "__main__":
    main()
