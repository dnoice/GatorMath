"""
Module Name: gatormath.precision

Description:
    Floating-point precision handling module providing safe comparisons,
    rounding operations, and tolerance-based equality checks to handle
    classic floating-point precision issues.

Module Path: gatormath/precision/__init__.py
Package: gatormath.precision

Author: Dennis 'dnoice' Smaltz
AI Acknowledgement: Claude Code
Created: 2025-11-02
Modified: 2025-11-02
Version: 0.1.0

Submodules:
    - comparison: Safe floating-point comparisons with tolerance
    - rounding: Robust rounding operations (future)

Exports:
    All functions from comparison module for convenience

Notes:
    Addresses the classic issue: 0.1 + 0.2 != 0.3
    Uses configurable epsilon tolerance for comparisons
"""

from gatormath.precision.comparison import compare, is_close, is_zero

__all__ = ["is_close", "is_zero", "compare"]
