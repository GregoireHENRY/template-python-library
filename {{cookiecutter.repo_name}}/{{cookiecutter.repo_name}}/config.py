#!/usr/bin/env python3

"""
Configurate parameters.
"""

from pathlib import Path
from typing import Any, Dict, Optional

import yaml
from dotmap import DotMap
from pudb import set_trace as bp  # noqa: F401

import {{cookiecutter.repo_name}}


class Cfg:
    """Structure representation of the configurable parameters."""

    # Configurable parameters default values.
    __DEFAULT_VARIABLE = Path("./default")

    # Variable
    __variable = __DEFAULT_VARIABLE

    def __init__(self) -> None:
        pass

    def load_config_file(self) -> None:
        """Load the config file."""
        PATH = {{cookiecutter.repo_name}}.CFG_PATH
        if PATH.is_file():
            CFG_FILE = {{cookiecutter.repo_name}}.utils.read_yaml(PATH)
            self.__parse_config_file(CFG_FILE)

    def __parse_config_file(self, CFG_FILE: DotMap) -> None:
        """Check that the config file is correct."""
        # Create the config.
        if CFG_FILE["variable"] not in (None, DotMap()):
            self.variable = Path(CFG_FILE["variable"])

    def to_dict(self, DEFAULT_ARE_NONE: bool = False) -> Dict[str, Optional[Any]]:
        """Convert config to hashmap."""
        if DEFAULT_ARE_NONE:
            return dict(
                variable=None,
            )
        else:
            return dict(
                variable=str(self.variable),
            )

    @property
    def variable(self) -> Path:
        """Get variable."""
        return self.__variable

    @variable.setter
    def variable(self, PATH: Path) -> None:
        """Set variable."""
        self.__variable = PATH


def generate_config() -> None:
    """Generate a config file `config.yaml` in the current directory."""
    PATH = {{cookiecutter.repo_name}}.CFG_PATH

    # Create empty config.
    CFG = dict(to_process=None, results=None)

    # Change all None to empty.
    {{cookiecutter.repo_name}}.utils.yaml_add_representer_none()

    # Check whether config should be saved.
    save = True
    if {{cookiecutter.repo_name}}.CFG_PATH.is_file():
        save = {{cookiecutter.repo_name}}.utils.form_yes_or_no(f"Overwrite {PATH}?")

    # Save as a new config file.
    if save:
        with PATH.open("w") as fp:
            yaml.dump(CFG, fp)
