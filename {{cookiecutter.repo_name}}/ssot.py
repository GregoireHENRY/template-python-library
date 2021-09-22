#!/usr/bin/env python3

"""
Update single sources of truth (name, version) in all listed files according to
their respective rules.
"""

import re
import sys
from pathlib import Path
from typing import Optional  # noqa: F401

from pudb import set_trace as bp  # noqa: F401

from {{cookiecutter.repo_name}} import NAME, VERSION

# Define for each file the pattern to match and the value to replace.
REGEX_VERSION = {
    Path("pyproject.toml"): [
        (r'(version\ =\ )("[\d.]+")', rf'\g<1>"{VERSION}"'),
        (r'(name\ =\ )(".+")', rf'\g<1>"{NAME}"'),
    ],
    Path("README.md"): [
        (r"(\[version badge\]\:\ .+\/version)(-[\d.]+-)", rf"\g<1>-{VERSION}-"),
    ],
}


def main() -> None:
    # Loop over the files to change.
    for PATH, OPERATIONS in REGEX_VERSION.items():
        # Read contents of file.
        TEXT = PATH.read_text()

        for (PATTERN, REPLACEMENT) in OPERATIONS:
            # Check that we have exactly one match.
            RESULT = re.findall(PATTERN, TEXT)
            if not len(RESULT):
                print(f"no match for the pattern {PATTERN} of {PATH.name}")
                sys.exit(1)
            elif len(RESULT) > 1:
                print(f"more than one match for the pattern {PATTERN} of {PATH.name}")
                sys.exit(1)
            # Apply match replacement.
            else:
                TEXT = re.sub(PATTERN, REPLACEMENT, TEXT)

        # Save TEXT into file.
        with PATH.open("w") as F:
            F.write(TEXT)


if __name__ == "__main__":
    main()
