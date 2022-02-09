#!/usr/bin/env python

"""
{{cookiecutter.project_name}}
"""

# from .module import function

from pkg_resources import get_distribution

__all__: list[str] = []

__version__ = get_distribution("{{cookiecutter.project_name}}").version
