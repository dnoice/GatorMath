"""
Module Name: gatormath.core

Description:
    Core mathematical operations module providing safe, robust arithmetic,
    algebraic, calculus, and statistical functions with overflow detection
    and precision handling.

Module Path: gatormath/core/__init__.py
Package: gatormath.core

Author: GatorMath Development Team
Created: 2025-11-02
Modified: 2025-11-02
Version: 0.1.0

Submodules:
    - arithmetic: Safe arithmetic operations with overflow detection
    - algebra: Algebraic operations (future)
    - calculus: Calculus operations (future)
    - statistics: Statistical functions (future)

Exports:
    All functions from arithmetic module for convenience

Notes:
    This module forms the foundation of all mathematical operations in GatorMath
"""

from gatormath.core import arithmetic

__all__ = ["arithmetic"]
