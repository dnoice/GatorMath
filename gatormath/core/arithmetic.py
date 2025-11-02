"""
Module Name: arithmetic

Description:
    Safe arithmetic operations with comprehensive error handling, overflow
    detection, and special case management. Provides robust alternatives to
    standard arithmetic operators with detailed error reporting.

Module Path: gatormath/core/arithmetic.py
Package: gatormath.core

Author: GatorMath Development Team
Created: 2025-11-02
Modified: 2025-11-02
Version: 0.1.0

Dependencies:
    - math: Standard library math functions
    - sys: System-specific parameters (float limits)
    - typing: Type hints

Exports:
    - safe_add: Addition with overflow checking
    - safe_subtract: Subtraction with overflow checking
    - safe_multiply: Multiplication with overflow checking
    - safe_divide: Division with zero checking
    - safe_power: Exponentiation with overflow checking
    - safe_sqrt: Square root with negative checking
    - safe_mod: Modulo with zero checking
    - factorial: Factorial calculation
    - gcd: Greatest common divisor
    - lcm: Least common multiple
    - clamp: Clamp value between bounds
    - sign: Sign of a number

Examples:
    >>> safe_add(1.0, 2.0)
    3.0

    >>> safe_divide(10.0, 0.0)
    Traceback (most recent call last):
        ...
    ZeroDivisionError: Division by zero

    >>> factorial(5)
    120

    >>> gcd(48, 18)
    6

Algorithm Complexity:
    - Basic operations (add, sub, mul, div): O(1)
    - factorial: O(n)
    - gcd: O(log(min(a, b)))
    - lcm: O(log(min(a, b)))

Notes:
    All operations check for overflow and special cases (NaN, infinity)
    Follows IEEE 754 floating-point arithmetic standard

References:
    [1] IEEE 754 Standard for Floating-Point Arithmetic
    [2] Python math module documentation
"""

import math
import sys
from typing import Union

# Type alias for numeric types
Number = Union[int, float]

# Constants
FLOAT_MAX = sys.float_info.max
FLOAT_MIN = sys.float_info.min
EPSILON = sys.float_info.epsilon


def safe_add(a: Number, b: Number) -> float:
    """
    Safely add two numbers with overflow detection.

    Args:
        a (Number): First operand
        b (Number): Second operand

    Returns:
        float: Sum of a and b

    Raises:
        OverflowError: If result exceeds float range
        ValueError: If either operand is NaN

    Complexity:
        Time: O(1)
        Space: O(1)

    Examples:
        >>> safe_add(1.0, 2.0)
        3.0

        >>> safe_add(0.1, 0.2)
        0.30000000000000004

    Version: 0.1.0
    """
    if math.isnan(a) or math.isnan(b):
        raise ValueError("Cannot add NaN values")

    result = float(a) + float(b)

    if math.isinf(result):
        raise OverflowError(f"Addition overflow: {a} + {b}")

    return result


def safe_subtract(a: Number, b: Number) -> float:
    """
    Safely subtract two numbers with overflow detection.

    Args:
        a (Number): Minuend
        b (Number): Subtrahend

    Returns:
        float: Difference of a and b

    Raises:
        OverflowError: If result exceeds float range
        ValueError: If either operand is NaN

    Complexity:
        Time: O(1)
        Space: O(1)

    Examples:
        >>> safe_subtract(5.0, 3.0)
        2.0

    Version: 0.1.0
    """
    if math.isnan(a) or math.isnan(b):
        raise ValueError("Cannot subtract NaN values")

    result = float(a) - float(b)

    if math.isinf(result):
        raise OverflowError(f"Subtraction overflow: {a} - {b}")

    return result


def safe_multiply(a: Number, b: Number) -> float:
    """
    Safely multiply two numbers with overflow detection.

    Args:
        a (Number): First factor
        b (Number): Second factor

    Returns:
        float: Product of a and b

    Raises:
        OverflowError: If result exceeds float range
        ValueError: If either operand is NaN

    Complexity:
        Time: O(1)
        Space: O(1)

    Examples:
        >>> safe_multiply(3.0, 4.0)
        12.0

    Version: 0.1.0
    """
    if math.isnan(a) or math.isnan(b):
        raise ValueError("Cannot multiply NaN values")

    result = float(a) * float(b)

    if math.isinf(result):
        raise OverflowError(f"Multiplication overflow: {a} * {b}")

    return result


def safe_divide(a: Number, b: Number) -> float:
    """
    Safely divide two numbers with zero and overflow checking.

    Args:
        a (Number): Numerator
        b (Number): Denominator

    Returns:
        float: Quotient of a and b

    Raises:
        ZeroDivisionError: If denominator is zero
        OverflowError: If result exceeds float range
        ValueError: If either operand is NaN

    Precision:
        Subject to floating-point division precision limits

    Complexity:
        Time: O(1)
        Space: O(1)

    Examples:
        >>> safe_divide(10.0, 2.0)
        5.0

        >>> safe_divide(10.0, 0.0)
        Traceback (most recent call last):
            ...
        ZeroDivisionError: Division by zero

    Version: 0.1.0
    """
    if math.isnan(a) or math.isnan(b):
        raise ValueError("Cannot divide NaN values")

    if b == 0:
        raise ZeroDivisionError("Division by zero")

    result = float(a) / float(b)

    if math.isinf(result):
        raise OverflowError(f"Division overflow: {a} / {b}")

    return result


def safe_power(base: Number, exponent: Number) -> float:
    """
    Safely raise base to exponent with overflow checking.

    Args:
        base (Number): Base value
        exponent (Number): Exponent value

    Returns:
        float: base raised to exponent

    Raises:
        ValueError: If base is negative and exponent is fractional
        OverflowError: If result exceeds float range

    Complexity:
        Time: O(1)
        Space: O(1)

    Examples:
        >>> safe_power(2.0, 3.0)
        8.0

        >>> safe_power(4.0, 0.5)
        2.0

    Version: 0.1.0
    """
    if math.isnan(base) or math.isnan(exponent):
        raise ValueError("Cannot compute power with NaN values")

    try:
        result = float(base) ** float(exponent)
    except ValueError as e:
        raise ValueError(f"Invalid power operation: {base}^{exponent}") from e

    if math.isinf(result):
        raise OverflowError(f"Power overflow: {base}^{exponent}")

    if math.isnan(result):
        raise ValueError(f"Power resulted in NaN: {base}^{exponent}")

    return result


def safe_sqrt(value: Number) -> float:
    """
    Safely compute square root with negative checking.

    Args:
        value (Number): Value to compute square root of

    Returns:
        float: Square root of value

    Raises:
        ValueError: If value is negative

    Algorithm:
        Uses math.sqrt() for computation

    Complexity:
        Time: O(1)
        Space: O(1)

    Examples:
        >>> safe_sqrt(16.0)
        4.0

        >>> safe_sqrt(-1.0)
        Traceback (most recent call last):
            ...
        ValueError: Cannot compute square root of negative number: -1.0

    Version: 0.1.0
    """
    if math.isnan(value):
        raise ValueError("Cannot compute square root of NaN")

    if value < 0:
        raise ValueError(f"Cannot compute square root of negative number: {value}")

    return math.sqrt(float(value))


def safe_mod(a: Number, b: Number) -> float:
    """
    Safely compute modulo with zero checking.

    Args:
        a (Number): Dividend
        b (Number): Divisor

    Returns:
        float: Remainder of a divided by b

    Raises:
        ZeroDivisionError: If divisor is zero
        ValueError: If either operand is NaN

    Complexity:
        Time: O(1)
        Space: O(1)

    Examples:
        >>> safe_mod(10.0, 3.0)
        1.0

        >>> safe_mod(10.0, 0.0)
        Traceback (most recent call last):
            ...
        ZeroDivisionError: Modulo by zero

    Version: 0.1.0
    """
    if math.isnan(a) or math.isnan(b):
        raise ValueError("Cannot compute modulo with NaN values")

    if b == 0:
        raise ZeroDivisionError("Modulo by zero")

    return float(a) % float(b)


def factorial(n: int) -> int:
    """
    Calculate factorial of non-negative integer.

    Args:
        n (int): Non-negative integer
            - Range: n >= 0
            - Constraint: Must be integer

    Returns:
        int: Factorial of n (n!)

    Raises:
        ValueError: If n is negative or not an integer

    Algorithm:
        Uses math.factorial() for computation

    Complexity:
        Time: O(n)
        Space: O(1)

    Examples:
        >>> factorial(5)
        120

        >>> factorial(0)
        1

        >>> factorial(-1)
        Traceback (most recent call last):
            ...
        ValueError: Factorial undefined for negative numbers

    Version: 0.1.0
    """
    if not isinstance(n, int):
        raise ValueError("Factorial requires integer argument")

    if n < 0:
        raise ValueError("Factorial undefined for negative numbers")

    return math.factorial(n)


def gcd(a: int, b: int) -> int:
    """
    Calculate greatest common divisor using Euclidean algorithm.

    Args:
        a (int): First integer
        b (int): Second integer

    Returns:
        int: Greatest common divisor of a and b

    Algorithm:
        Euclidean algorithm: gcd(a,b) = gcd(b, a mod b)

    Complexity:
        Time: O(log(min(a, b)))
        Space: O(1)

    Examples:
        >>> gcd(48, 18)
        6

        >>> gcd(17, 5)
        1

    Version: 0.1.0
    """
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("GCD requires integer arguments")

    return math.gcd(a, b)


def lcm(a: int, b: int) -> int:
    """
    Calculate least common multiple.

    Args:
        a (int): First integer
        b (int): Second integer

    Returns:
        int: Least common multiple of a and b

    Algorithm:
        lcm(a,b) = abs(a*b) / gcd(a,b)

    Complexity:
        Time: O(log(min(a, b)))
        Space: O(1)

    Examples:
        >>> lcm(12, 18)
        36

        >>> lcm(5, 7)
        35

    Version: 0.1.0
    """
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("LCM requires integer arguments")

    return math.lcm(a, b)


def clamp(value: Number, min_val: Number, max_val: Number) -> float:
    """
    Clamp value between minimum and maximum bounds.

    Args:
        value (Number): Value to clamp
        min_val (Number): Minimum bound
        max_val (Number): Maximum bound

    Returns:
        float: Clamped value

    Raises:
        ValueError: If min_val > max_val

    Complexity:
        Time: O(1)
        Space: O(1)

    Examples:
        >>> clamp(5.0, 0.0, 10.0)
        5.0

        >>> clamp(-5.0, 0.0, 10.0)
        0.0

        >>> clamp(15.0, 0.0, 10.0)
        10.0

    Version: 0.1.0
    """
    if min_val > max_val:
        raise ValueError(f"min_val ({min_val}) cannot be greater than max_val ({max_val})")

    return max(min_val, min(value, max_val))


def sign(value: Number) -> int:
    """
    Return sign of a number.

    Args:
        value (Number): Value to check

    Returns:
        int: -1 if negative, 0 if zero, 1 if positive

    Complexity:
        Time: O(1)
        Space: O(1)

    Examples:
        >>> sign(5.0)
        1

        >>> sign(-3.0)
        -1

        >>> sign(0.0)
        0

    Version: 0.1.0
    """
    if value > 0:
        return 1
    elif value < 0:
        return -1
    else:
        return 0
