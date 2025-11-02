"""
Metadata:
    Project: GatorMath
    File Name: __init__.py
    File Path: gatormath/precision/__init__.py
    Module: Precision Handling Package
    Created: 2025-11-02
    Modified: 2025-11-02
    Version: 0.1.0
    Author: Dennis 'dnoice' Smaltz
    AI Acknowledgement: Claude Code

Description:
    Floating-point precision handling module providing safe comparisons,
    rounding operations, and tolerance-based equality checks to handle
    classic floating-point precision issues.

Usage:
    >>> from gatormath.precision import is_close, is_zero
    >>> is_close(0.1 + 0.2, 0.3)
    True
    >>> is_zero(1e-15)
    True

Contents:
    Submodules:
        - comparison: Safe floating-point comparisons with tolerance
        - rounding: Robust rounding operations (future)

    Exports:
        - is_close: Check if two floats are approximately equal
        - is_zero: Check if a float is approximately zero
        - compare: Three-way comparison with tolerance

Dependencies:
    - gatormath.precision.comparison: Comparison functions

Notes:
    Addresses the classic issue: 0.1 + 0.2 != 0.3
    Uses configurable epsilon tolerance for comparisons
"""

from gatormath.precision.comparison import compare, is_close, is_zero

__all__ = ["is_close", "is_zero", "compare"]
