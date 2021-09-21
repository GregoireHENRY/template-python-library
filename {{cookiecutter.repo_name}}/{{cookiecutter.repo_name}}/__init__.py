#!/usr/bin/env python3

"""
{{cookiecutter.project_name}}
"""

import logging
import os
from pathlib import Path

from . import config, utils
from .core import run

__all__ = ["run"]

# Project variables.
NAME = "{{cookiecutter.project_name}}"
VERSION = "0.1.0"

# Logging settings.
LOG_LEVEL = logging.DEBUG
LOG_FORMAT = "%(asctime)s %(name)s[%(levelname)s]: %(message)s"
LOG_DATEFMT = "%m/%d/%Y %I:%M:%S %p"

# Runtime variables.
SRC_PATH = Path(os.path.realpath(__file__)).parent
ASSETS_PATH = SRC_PATH / "assets"
CFG_PATH = Path(f"{NAME}.yaml")
LOG_PATH = Path(f"{NAME}.log")

# Start logging.
logging.basicConfig(
    filename=LOG_PATH,
    level=LOG_LEVEL,
    format=LOG_FORMAT,
    datefmt=LOG_DATEFMT,
)
logging.getLogger("matplotlib").setLevel(logging.WARNING)
LOGGER = logging.getLogger(NAME)
LOGGER.info("Logging enabled.")

# Configurable parameters definition.
cfg = config.Cfg()
