"""
Module Name: cli

Description:
    Command-line interface for GatorMath with Rich theming.

Module Path: gatormath/cli/__init__.py
Package: gatormath.cli

Author: GatorMath Development Team
Created: 2025-11-01
Version: 0.1.0
"""

from gatormath.cli.theme import GATOR_THEME, create_console


__all__ = [
    "GATOR_THEME",
    "create_console",
]
