#!/usr/bin/env python3
# type: ignore [misc]

"""
{{cookiecutter.project_name}} CLI.
"""


from typing import Any

import click
from pudb import set_trace as bp  # noqa: F401

import {{cookiecutter.repo_name}}

CONTEXT_SETTINGS = dict(help_option_names=["-h", "--help"])


def version(ctx: Any, param: Any, value: Any) -> None:
    if not value or ctx.resilient_parsing:
        return
    click.echo({{cookiecutter.repo_name}}.VERSION)
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
@click.option(
    "--generate-config",
    is_flag=True,
    help="Generate a config file `config.yaml` in the current directory.",
)
def cli(ctx: click.Context, generate_config: bool) -> None:
    """{{cookiecutter.project_name}} command-line entry point."""
    # Share default command options.
    ctx.ensure_object(dict)
    # ctx.obj["var"] = var

    if generate_config:
        {{cookiecutter.repo_name}}.config.generate_config()
        ctx.exit()

    {{cookiecutter.repo_name}}.cfg.load_config_file()

    if ctx.invoked_subcommand is None:
        click.echo(ctx.get_help())
        ctx.exit()


@cli.command()
@click.pass_context
def run(
    ctx: click.Context,
) -> None:
    """Run {{cookiecutter.project_name}}."""
    {{cookiecutter.repo_name}}.core.run()


def main() -> None:
    cli(prog_name={{cookiecutter.repo_name}}.NAME)


if __name__ == "__main__":
    main()
