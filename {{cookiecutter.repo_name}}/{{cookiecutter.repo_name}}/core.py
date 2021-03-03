#!/usr/bin/env python3

"""
{{cookiecutter.project_name}}
"""

from pudb import set_trace as bp  # noqa: F401


def start() -> None:
    """{{cookiecutter.project_name}}"""


def demo(name: str, demo: str) -> str:
    """Description."""
    return f"{name}: {demo}"


def power(value: float) -> float:
    """Compute power."""
    return value ** 2
