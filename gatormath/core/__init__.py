"""
Metadata:
    Project: GatorMath
    File Name: __init__.py
    File Path: gatormath/core/__init__.py
    Module: Core Mathematical Operations Package
    Created: 2025-11-02
    Modified: 2025-11-02
    Version: 0.1.0
    Author: Dennis 'dnoice' Smaltz
    AI Acknowledgement: Claude Code

Description:
    Core mathematical operations module providing safe, robust arithmetic,
    algebraic, calculus, and statistical functions with overflow detection
    and precision handling.

Usage:
    >>> from gatormath.core import arithmetic
    >>> arithmetic.safe_add(1.0, 2.0)
    3.0

Contents:
    Submodules:
        - arithmetic: Safe arithmetic operations with overflow detection
        - algebra: Algebraic operations (future)
        - calculus: Calculus operations (future)
        - statistics: Statistical functions (future)

    Exports:
        - arithmetic: Arithmetic operations module

Dependencies:
    - gatormath.core.arithmetic: Core arithmetic functions

Notes:
    This module forms the foundation of all mathematical operations in GatorMath
"""

from gatormath.core import arithmetic

__all__ = ["arithmetic"]
