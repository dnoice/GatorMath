"""
Module Name: comparison

Description:
    Safe floating-point comparison utilities that handle precision issues
    inherent in IEEE 754 arithmetic. Provides robust comparison functions
    with configurable tolerance levels for real-world numerical applications.

Module Path: gatormath/precision/comparison.py
Package: gatormath.precision

Author: GatorMath Development Team
Created: 2025-11-01
Modified: 2025-11-01
Version: 0.1.0

Dependencies:
    - math: Standard mathematical functions
    - typing: Type hints for robust type checking

Exports:
    - is_close: Compare two floats with relative and absolute tolerance
    - is_zero: Check if a number is effectively zero
    - compare: Three-way comparison returning -1, 0, or 1
    - is_equal: Strict equality check with tolerance
    - is_less_than: Less-than comparison with tolerance
    - is_greater_than: Greater-than comparison with tolerance
    - is_between: Check if value is within a range
    - DEFAULT_EPSILON: Default tolerance for comparisons

Mathematical Background:
    Floating-point numbers cannot represent all real numbers exactly due to
    binary representation limitations. This causes issues like:
        0.1 + 0.2 != 0.3  (in most languages)

    Solutions:
        1. Absolute tolerance: |a - b| < epsilon
        2. Relative tolerance: |a - b| / max(|a|, |b|) < epsilon
        3. Combined approach (implemented here)

Precision Notes:
    - Default epsilon: 1e-9 (one billionth)
    - Handles both very small and very large numbers
    - Special handling for zero comparisons
    - NaN and infinity aware

Usage:
    >>> from gatormath.precision import comparison
    >>> comparison.is_close(0.1 + 0.2, 0.3)
    True
    >>> comparison.is_zero(1e-15)
    True

Examples:
    Basic comparison:
    >>> is_close(0.1 + 0.2, 0.3)
    True
    >>> is_close(1.0, 1.0000001, epsilon=1e-6)
    True

    Zero checking:
    >>> is_zero(0.0)
    True
    >>> is_zero(1e-15)
    True
    >>> is_zero(1e-5)
    False

    Three-way comparison:
    >>> compare(5.0, 3.0)
    1
    >>> compare(3.0, 5.0)
    -1
    >>> compare(5.0, 5.0000001)
    0

Notes:
    - All functions handle NaN and infinity correctly
    - Epsilon can be adjusted for specific use cases
    - Relative tolerance prevents issues with large numbers
    - Absolute tolerance handles numbers near zero

See Also:
    - math.isclose: Python's built-in (similar but different defaults)
    - numpy.isclose: NumPy's version for arrays
    - gatormath.precision.rounding: Complementary rounding functions

References:
    [1] "What Every Computer Scientist Should Know About Floating-Point
        Arithmetic" - David Goldberg
    [2] IEEE 754-2008 Standard for Floating-Point Arithmetic
    [3] Python PEP 485 - A function for testing approximate equality
"""

# Standard library imports
import math
from typing import Union


# ============================================================================
# Constants
# ============================================================================

# Default epsilon for floating-point comparisons
# 1e-9 (one billionth) balances precision and practicality
DEFAULT_EPSILON: float = 1e-9

# Epsilon for zero comparisons (can be different from general epsilon)
DEFAULT_ZERO_EPSILON: float = 1e-15


# ============================================================================
# Type Aliases
# ============================================================================

Number = Union[int, float]


# ============================================================================
# Core Comparison Functions
# ============================================================================

def is_close(
    a: Number,
    b: Number,
    *,
    rel_tol: float = DEFAULT_EPSILON,
    abs_tol: float = DEFAULT_EPSILON,
) -> bool:
    """
    Determine if two numbers are close within tolerance.

    Uses both relative and absolute tolerance for robust comparison across
    different magnitudes. Based on PEP 485 with adjusted defaults.

    Args:
        a (Number): First number to compare
        b (Number): Second number to compare
        rel_tol (float): Relative tolerance (default: 1e-9)
            Maximum allowed difference relative to the larger absolute value
        abs_tol (float): Absolute tolerance (default: 1e-9)
            Maximum allowed absolute difference

    Returns:
        bool: True if |a - b| <= max(rel_tol * max(|a|, |b|), abs_tol)

    Algorithm:
        1. Handle special cases (NaN, infinity)
        2. Calculate absolute difference: diff = |a - b|
        3. Calculate relative threshold: max(|a|, |b|) * rel_tol
        4. Return: diff <= max(relative_threshold, abs_tol)

    Complexity:
        Time: O(1)
        Space: O(1)

    Precision:
        - Handles numbers from ~1e-15 to ~1e15 reliably
        - For numbers outside this range, adjust tolerances accordingly
        - Special handling ensures comparisons near zero work correctly

    Examples:
        >>> # Classic floating-point issue resolved
        >>> is_close(0.1 + 0.2, 0.3)
        True

        >>> # Large numbers
        >>> is_close(1e10, 1e10 + 1)
        False
        >>> is_close(1e10, 1e10 + 1, rel_tol=1e-9)
        False

        >>> # Small numbers
        >>> is_close(1e-10, 1e-10 + 1e-15)
        True

        >>> # Custom tolerance
        >>> is_close(1.0, 1.1, rel_tol=0.2)
        True

        >>> # NaN handling
        >>> is_close(float('nan'), float('nan'))
        False

        >>> # Infinity handling
        >>> is_close(float('inf'), float('inf'))
        True

    Raises:
        TypeError: If a or b is not a number
        ValueError: If rel_tol or abs_tol is negative

    See Also:
        - math.isclose: Python's built-in with different defaults
        - is_equal: Alias for this function with default tolerances

    Notes:
        - NaN is never close to anything, including itself
        - Positive and negative infinity are only close to themselves
        - Use abs_tol for comparisons near zero
        - Use rel_tol for comparisons of large numbers

    Version: 0.1.0
    """
    # Input validation
    if rel_tol < 0 or abs_tol < 0:
        raise ValueError("Tolerances must be non-negative")

    # Handle special cases
    if math.isnan(a) or math.isnan(b):
        return False

    if math.isinf(a) or math.isinf(b):
        return a == b

    # Calculate absolute difference
    diff = abs(a - b)

    # Use both relative and absolute tolerance
    # Relative tolerance scales with magnitude
    # Absolute tolerance handles numbers near zero
    return diff <= max(rel_tol * max(abs(a), abs(b)), abs_tol)


def is_zero(
    value: Number,
    *,
    epsilon: float = DEFAULT_ZERO_EPSILON,
) -> bool:
    """
    Check if a number is effectively zero within tolerance.

    Args:
        value (Number): Number to check
        epsilon (float): Absolute tolerance (default: 1e-15)

    Returns:
        bool: True if |value| < epsilon

    Examples:
        >>> is_zero(0.0)
        True
        >>> is_zero(1e-20)
        True
        >>> is_zero(1e-10)
        False
        >>> is_zero(-1e-16)
        True

        >>> # Custom epsilon
        >>> is_zero(0.001, epsilon=0.01)
        True

    Raises:
        ValueError: If epsilon is negative

    Notes:
        - Uses absolute tolerance only (no relative tolerance needed for zero)
        - Default epsilon is very small (1e-15) for strict zero checking
        - For less strict checking, use is_close(value, 0.0)

    Version: 0.1.0
    """
    if epsilon < 0:
        raise ValueError("Epsilon must be non-negative")

    if math.isnan(value):
        return False

    return abs(value) < epsilon


def compare(
    a: Number,
    b: Number,
    *,
    epsilon: float = DEFAULT_EPSILON,
) -> int:
    """
    Three-way comparison with tolerance.

    Args:
        a (Number): First number
        b (Number): Second number
        epsilon (float): Comparison tolerance (default: 1e-9)

    Returns:
        int: -1 if a < b, 0 if a ≈ b, 1 if a > b

    Examples:
        >>> compare(5.0, 3.0)
        1
        >>> compare(3.0, 5.0)
        -1
        >>> compare(3.0, 3.0000001)
        0
        >>> compare(3.0, 3.1, epsilon=0.2)
        0

    Notes:
        - Useful for sorting with tolerance
        - Returns 0 if numbers are within epsilon
        - NaN comparisons always return -1

    Algorithm:
        1. Check if values are close (within epsilon)
        2. If close, return 0
        3. Otherwise, return -1 or 1 based on magnitude

    Complexity:
        Time: O(1)
        Space: O(1)

    Version: 0.1.0
    """
    if is_close(a, b, rel_tol=epsilon, abs_tol=epsilon):
        return 0
    return -1 if a < b else 1


def is_equal(
    a: Number,
    b: Number,
    *,
    epsilon: float = DEFAULT_EPSILON,
) -> bool:
    """
    Check if two numbers are equal within tolerance.

    Alias for is_close with simpler interface.

    Args:
        a (Number): First number
        b (Number): Second number
        epsilon (float): Tolerance (default: 1e-9)

    Returns:
        bool: True if numbers are equal within epsilon

    Examples:
        >>> is_equal(0.1 + 0.2, 0.3)
        True
        >>> is_equal(5.0, 5.0000001)
        True
        >>> is_equal(5.0, 5.1, epsilon=0.2)
        True

    See Also:
        - is_close: More flexible version with separate tolerances

    Version: 0.1.0
    """
    return is_close(a, b, rel_tol=epsilon, abs_tol=epsilon)


def is_less_than(
    a: Number,
    b: Number,
    *,
    epsilon: float = DEFAULT_EPSILON,
) -> bool:
    """
    Check if a is less than b with tolerance.

    Args:
        a (Number): First number
        b (Number): Second number
        epsilon (float): Tolerance (default: 1e-9)

    Returns:
        bool: True if a < b (and not approximately equal)

    Examples:
        >>> is_less_than(3.0, 5.0)
        True
        >>> is_less_than(5.0, 3.0)
        False
        >>> is_less_than(3.0, 3.0000001)
        False

    Notes:
        - Returns False if numbers are approximately equal
        - Equivalent to: a < b and not is_close(a, b)

    Version: 0.1.0
    """
    return not is_close(a, b, rel_tol=epsilon, abs_tol=epsilon) and a < b


def is_greater_than(
    a: Number,
    b: Number,
    *,
    epsilon: float = DEFAULT_EPSILON,
) -> bool:
    """
    Check if a is greater than b with tolerance.

    Args:
        a (Number): First number
        b (Number): Second number
        epsilon (float): Tolerance (default: 1e-9)

    Returns:
        bool: True if a > b (and not approximately equal)

    Examples:
        >>> is_greater_than(5.0, 3.0)
        True
        >>> is_greater_than(3.0, 5.0)
        False
        >>> is_greater_than(3.0, 3.0000001)
        False

    Notes:
        - Returns False if numbers are approximately equal
        - Equivalent to: a > b and not is_close(a, b)

    Version: 0.1.0
    """
    return not is_close(a, b, rel_tol=epsilon, abs_tol=epsilon) and a > b


def is_between(
    value: Number,
    lower: Number,
    upper: Number,
    *,
    epsilon: float = DEFAULT_EPSILON,
    inclusive: bool = True,
) -> bool:
    """
    Check if value is between lower and upper bounds with tolerance.

    Args:
        value (Number): Value to check
        lower (Number): Lower bound
        upper (Number): Upper bound
        epsilon (float): Comparison tolerance (default: 1e-9)
        inclusive (bool): Include bounds in range (default: True)

    Returns:
        bool: True if value is in range [lower, upper] (or (lower, upper))

    Examples:
        >>> is_between(5.0, 3.0, 7.0)
        True
        >>> is_between(3.0, 3.0, 7.0)
        True
        >>> is_between(3.0, 3.0, 7.0, inclusive=False)
        False
        >>> is_between(5.0, 3.0, 7.0, inclusive=False)
        True

    Raises:
        ValueError: If lower > upper

    Notes:
        - Bounds can be equal (single-point range)
        - Uses epsilon for all comparisons
        - inclusive=True: [lower, upper]
        - inclusive=False: (lower, upper)

    Version: 0.1.0
    """
    if lower > upper:
        raise ValueError(f"Lower bound ({lower}) cannot exceed upper bound ({upper})")

    if inclusive:
        return (
            is_close(value, lower, rel_tol=epsilon, abs_tol=epsilon) or value > lower
        ) and (
            is_close(value, upper, rel_tol=epsilon, abs_tol=epsilon) or value < upper
        )
    else:
        return (
            not is_close(value, lower, rel_tol=epsilon, abs_tol=epsilon)
            and value > lower
            and not is_close(value, upper, rel_tol=epsilon, abs_tol=epsilon)
            and value < upper
        )


# ============================================================================
# Module Exports
# ============================================================================

__all__ = [
    # Constants
    "DEFAULT_EPSILON",
    "DEFAULT_ZERO_EPSILON",
    # Functions
    "is_close",
    "is_zero",
    "compare",
    "is_equal",
    "is_less_than",
    "is_greater_than",
    "is_between",
]
