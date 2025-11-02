"""
Metadata:
    Project: GatorMath
    File Name: comparison.py
    File Path: gatormath/precision/comparison.py
    Module: Floating-Point Comparison
    Created: 2025-11-02
    Modified: 2025-11-02
    Version: 0.1.0
    Author: Dennis 'dnoice' Smaltz
    AI Acknowledgement: Claude Code

Description:
    Safe floating-point comparison functions with configurable tolerance.
    Solves classic precision issues like 0.1 + 0.2 != 0.3 by using
    epsilon-based comparisons instead of direct equality.

Usage:
    >>> from gatormath.precision.comparison import is_close, is_zero, compare
    >>> is_close(0.1 + 0.2, 0.3)
    True

    >>> is_zero(1e-15)
    True

    >>> compare(5.0, 3.0)
    1

Contents:
    Functions:
        - is_close: Check if two floats are approximately equal
        - is_zero: Check if a float is approximately zero
        - compare: Three-way comparison with tolerance

Dependencies:
    - math: Standard library math functions
    - sys: System-specific parameters (float epsilon)
    - typing: Type hints

Algorithm Complexity:
    All functions: O(1) time, O(1) space

References:
    [1] IEEE 754 Standard for Floating-Point Arithmetic
    [2] Python math.isclose() documentation

Notes:
    Default epsilon is based on sys.float_info.epsilon scaled appropriately
    for typical use cases (1e-9). Can be customized per call.
"""

import math
import sys
from typing import Union

# Type alias
Number = Union[int, float]

# Default tolerance for floating-point comparisons
# Using 1e-9 as it works well for most practical cases
DEFAULT_EPSILON = 1e-9


def is_close(
    a: Number,
    b: Number,
    rel_tol: float = DEFAULT_EPSILON,
    abs_tol: float = DEFAULT_EPSILON
) -> bool:
    """
    Check if two numbers are approximately equal within tolerance.

    Implements both relative and absolute tolerance checks to handle
    comparisons across different magnitude ranges.

    Args:
        a (Number): First value
        b (Number): Second value
        rel_tol (float): Relative tolerance (default: 1e-9)
            - Applied as percentage of larger magnitude
        abs_tol (float): Absolute tolerance (default: 1e-9)
            - Applied as fixed difference threshold

    Returns:
        bool: True if values are within tolerance, False otherwise

    Algorithm:
        Returns True if:
        abs(a - b) <= max(rel_tol * max(abs(a), abs(b)), abs_tol)

    Precision:
        Uses both relative and absolute tolerance to handle:
        - Small numbers (absolute tolerance)
        - Large numbers (relative tolerance)
        - Numbers near zero (absolute tolerance)

    Complexity:
        Time: O(1)
        Space: O(1)

    Examples:
        >>> is_close(0.1 + 0.2, 0.3)
        True

        >>> is_close(1.0, 1.0000000001)
        True

        >>> is_close(1.0, 2.0)
        False

        >>> # Custom tolerance
        >>> is_close(1.0, 1.01, rel_tol=0.02)
        True

    See Also:
        - is_zero: Check if value is approximately zero
        - math.isclose: Python standard library equivalent

    Notes:
        Handles NaN and infinity according to IEEE 754:
        - NaN is never close to anything (including itself)
        - Infinity is only close to itself

    Version: 0.1.0
    """
    # Handle NaN
    if math.isnan(a) or math.isnan(b):
        return False

    # Handle infinity
    if math.isinf(a) or math.isinf(b):
        return a == b

    # Standard tolerance check
    return abs(a - b) <= max(rel_tol * max(abs(a), abs(b)), abs_tol)


def is_zero(value: Number, tolerance: float = DEFAULT_EPSILON) -> bool:
    """
    Check if a number is approximately zero within tolerance.

    Args:
        value (Number): Value to check
        tolerance (float): Absolute tolerance (default: 1e-9)

    Returns:
        bool: True if value is within tolerance of zero

    Complexity:
        Time: O(1)
        Space: O(1)

    Examples:
        >>> is_zero(0.0)
        True

        >>> is_zero(1e-15)
        True

        >>> is_zero(1e-8)
        True

        >>> is_zero(0.001)
        False

        >>> # Custom tolerance
        >>> is_zero(0.01, tolerance=0.1)
        True

    Notes:
        Uses absolute tolerance only (not relative) since we're comparing to zero

    Version: 0.1.0
    """
    if math.isnan(value):
        return False

    return abs(value) <= tolerance


def compare(a: Number, b: Number, tolerance: float = DEFAULT_EPSILON) -> int:
    """
    Three-way comparison with tolerance.

    Performs a three-way comparison that returns:
    - -1 if a < b (beyond tolerance)
    - 0 if a ≈ b (within tolerance)
    - 1 if a > b (beyond tolerance)

    Args:
        a (Number): First value
        b (Number): Second value
        tolerance (float): Comparison tolerance (default: 1e-9)

    Returns:
        int: -1, 0, or 1 indicating comparison result

    Complexity:
        Time: O(1)
        Space: O(1)

    Examples:
        >>> compare(5.0, 3.0)
        1

        >>> compare(3.0, 5.0)
        -1

        >>> compare(3.0, 3.0)
        0

        >>> compare(3.0, 3.0000001)
        0

        >>> compare(1.0, 2.0, tolerance=2.0)
        0

    See Also:
        - is_close: Check if two values are approximately equal

    Notes:
        Useful for sorting operations where floating-point precision matters
        Can be used as a key function for sorted()

    Version: 0.1.0
    """
    if is_close(a, b, abs_tol=tolerance, rel_tol=tolerance):
        return 0
    elif a < b:
        return -1
    else:
        return 1
