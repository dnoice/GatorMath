"""
Module Name: core

Description:
    Core mathematical operations with robust implementations.

Module Path: gatormath/core/__init__.py
Package: gatormath.core

Author: GatorMath Development Team
Created: 2025-11-01
Version: 0.1.0
"""

from gatormath.core.arithmetic import (
    EPSILON,
    MAX_FLOAT,
    MAX_SAFE_INTEGER,
    MIN_FLOAT,
    MIN_SAFE_INTEGER,
    clamp,
    factorial,
    gcd,
    lcm,
    safe_add,
    safe_divide,
    safe_mod,
    safe_multiply,
    safe_power,
    safe_sqrt,
    safe_subtract,
    sign,
)


__all__ = [
    "MAX_SAFE_INTEGER",
    "MIN_SAFE_INTEGER",
    "MAX_FLOAT",
    "MIN_FLOAT",
    "EPSILON",
    "safe_add",
    "safe_subtract",
    "safe_multiply",
    "safe_divide",
    "safe_power",
    "safe_sqrt",
    "safe_mod",
    "clamp",
    "sign",
    "factorial",
    "gcd",
    "lcm",
]
