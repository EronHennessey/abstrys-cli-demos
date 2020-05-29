#!/usr/bin/env python3
# Abstrys CLI demos

from setuptools import setup, find_packages

setup(
    name="abstrys-cli-demos",
    version="0.1",
    author="Eron Hennessey",
    author_email="eron@abstrys.com",
    description="Abstrys CLI demos",
    license="BSD",
    keywords="cli example",
    packages=find_packages(),
    entry_points= {
        "console_scripts": [
            "subcommand_demo=abstrys.subcommand_cli_demo:main"
        ]
    }
)

