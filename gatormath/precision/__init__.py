"""
Module Name: precision

Description:
    Floating-point precision handling for robust numerical computing.
    Provides safe comparison operations and rounding utilities that handle
    IEEE 754 floating-point arithmetic edge cases.

Module Path: gatormath/precision/__init__.py
Package: gatormath.precision

Author: GatorMath Development Team
Created: 2025-11-01
Modified: 2025-11-01
Version: 0.1.0

Exports:
    From comparison:
        - is_close: Safe floating-point equality
        - is_zero: Check if effectively zero
        - compare: Three-way comparison
        - is_equal, is_less_than, is_greater_than, is_between

    Constants:
        - DEFAULT_EPSILON: Default tolerance (1e-9)

Usage:
    >>> from gatormath.precision import is_close, is_zero
    >>> is_close(0.1 + 0.2, 0.3)
    True
"""

from gatormath.precision.comparison import (
    DEFAULT_EPSILON,
    DEFAULT_ZERO_EPSILON,
    compare,
    is_between,
    is_close,
    is_equal,
    is_greater_than,
    is_less_than,
    is_zero,
)


__all__ = [
    "DEFAULT_EPSILON",
    "DEFAULT_ZERO_EPSILON",
    "is_close",
    "is_zero",
    "compare",
    "is_equal",
    "is_less_than",
    "is_greater_than",
    "is_between",
]
