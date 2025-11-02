"""
Metadata:
    Project: GatorMath
    File Name: arithmetic.py
    File Path: gatormath/core/arithmetic.py
    Module: Core Arithmetic Operations
    Created: 2025-11-02
    Modified: 2025-11-02
    Version: 0.2.0
    Author: Dennis 'dnoice' Smaltz
    AI Acknowledgement: Claude Code

Description:
    Safe arithmetic operations with comprehensive error handling, overflow
    detection, and special case management. Provides robust alternatives to
    standard arithmetic operators with detailed error reporting.

Usage:
    >>> from gatormath.core.arithmetic import safe_add, safe_divide, factorial, gcd
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

Contents:
    Basic Arithmetic Functions:
        - safe_add: Addition with overflow checking
        - safe_subtract: Subtraction with overflow checking
        - safe_multiply: Multiplication with overflow checking
        - safe_divide: Division with zero checking
        - safe_power: Exponentiation with overflow checking
        - safe_sqrt: Square root with negative checking
        - safe_mod: Modulo with zero checking

    Integer Functions:
        - factorial: Factorial calculation
        - gcd: Greatest common divisor (Euclidean algorithm)
        - lcm: Least common multiple

    Utility Functions:
        - clamp: Clamp value between bounds
        - sign: Sign of a number (-1, 0, or 1)

    Rounding & Absolute Functions:
        - abs_value: Absolute value with IEEE 754 compliance
        - floor: Round down to nearest integer
        - ceil: Round up to nearest integer
        - trunc: Truncate toward zero
        - round_half_up: Standard rounding (ties away from zero)
        - round_half_even: Banker's rounding (ties to even)
        - round_to_digits: Flexible rounding with method selection

Dependencies:
    - math: Standard library math functions
    - sys: System-specific parameters (float limits)
    - typing: Type hints

Algorithm Complexity:
    - Basic operations (add, sub, mul, div): O(1)
    - factorial: O(n)
    - gcd: O(log(min(a, b)))
    - lcm: O(log(min(a, b)))

References:
    [1] IEEE 754 Standard for Floating-Point Arithmetic
    [2] Python math module documentation

Notes:
    All operations check for overflow and special cases (NaN, infinity)
    Follows IEEE 754 floating-point arithmetic standard
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


# ===== ROUNDING & ABSOLUTE VALUE OPERATIONS =====


def abs_value(value: Number) -> float:
    """
    Compute absolute value of a number.

    Args:
        value (Number): Input value

    Returns:
        float: Absolute value of input (always non-negative)

    Algorithm:
        Returns value if value >= 0, otherwise returns -value

    Complexity:
        Time: O(1)
        Space: O(1)

    Special Cases:
        - abs(NaN) = NaN
        - abs(+inf) = +inf
        - abs(-inf) = +inf
        - abs(+0) = +0
        - abs(-0) = +0

    Examples:
        >>> abs_value(5.0)
        5.0

        >>> abs_value(-3.5)
        3.5

        >>> abs_value(0.0)
        0.0

        >>> abs_value(-0.0)
        0.0

    Notes:
        Named abs_value to avoid collision with built-in abs()
        Handles IEEE 754 special values correctly

    Version: 0.1.0
    """
    if math.isnan(value):
        return float('nan')

    return float(abs(value))


def floor(value: Number) -> float:
    """
    Round value down to nearest integer (toward negative infinity).

    Args:
        value (Number): Value to floor

    Returns:
        float: Largest integer <= value (as float type)

    Algorithm:
        Uses math.floor() which implements IEEE 754 roundToIntegralTowardNegative

    Complexity:
        Time: O(1)
        Space: O(1)

    Special Cases:
        - floor(NaN) = NaN
        - floor(+inf) = +inf
        - floor(-inf) = -inf
        - floor(+0) = +0
        - floor(-0) = -0

    Examples:
        >>> floor(3.7)
        3.0

        >>> floor(3.2)
        3.0

        >>> floor(-3.7)
        -4.0

        >>> floor(-3.2)
        -4.0

        >>> floor(5.0)
        5.0

    See Also:
        - ceil: Round up to nearest integer
        - trunc: Round toward zero

    References:
        [1] IEEE 754-2008 Section 5.9: Round to Integral

    Version: 0.1.0
    """
    if math.isnan(value):
        return float('nan')

    if math.isinf(value):
        return value

    return float(math.floor(value))


def ceil(value: Number) -> float:
    """
    Round value up to nearest integer (toward positive infinity).

    Args:
        value (Number): Value to ceil

    Returns:
        float: Smallest integer >= value (as float type)

    Algorithm:
        Uses math.ceil() which implements IEEE 754 roundToIntegralTowardPositive

    Complexity:
        Time: O(1)
        Space: O(1)

    Special Cases:
        - ceil(NaN) = NaN
        - ceil(+inf) = +inf
        - ceil(-inf) = -inf
        - ceil(+0) = +0
        - ceil(-0) = -0

    Examples:
        >>> ceil(3.2)
        4.0

        >>> ceil(3.7)
        4.0

        >>> ceil(-3.2)
        -3.0

        >>> ceil(-3.7)
        -3.0

        >>> ceil(5.0)
        5.0

    See Also:
        - floor: Round down to nearest integer
        - trunc: Round toward zero

    References:
        [1] IEEE 754-2008 Section 5.9: Round to Integral

    Version: 0.1.0
    """
    if math.isnan(value):
        return float('nan')

    if math.isinf(value):
        return value

    return float(math.ceil(value))


def trunc(value: Number) -> float:
    """
    Truncate value toward zero (remove fractional part).

    Args:
        value (Number): Value to truncate

    Returns:
        float: Integer part of value (as float type)

    Algorithm:
        Uses math.trunc() which implements IEEE 754 roundToIntegralTowardZero
        Equivalent to floor(x) for x >= 0, ceil(x) for x < 0

    Complexity:
        Time: O(1)
        Space: O(1)

    Special Cases:
        - trunc(NaN) = NaN
        - trunc(+inf) = +inf
        - trunc(-inf) = -inf
        - trunc(+0) = +0
        - trunc(-0) = -0

    Examples:
        >>> trunc(3.7)
        3.0

        >>> trunc(3.2)
        3.0

        >>> trunc(-3.7)
        -3.0

        >>> trunc(-3.2)
        -3.0

        >>> trunc(5.0)
        5.0

    See Also:
        - floor: Round down (toward -inf)
        - ceil: Round up (toward +inf)

    Notes:
        Truncation always rounds toward zero, unlike floor which
        always rounds toward negative infinity

    References:
        [1] IEEE 754-2008 Section 5.9: Round to Integral

    Version: 0.1.0
    """
    if math.isnan(value):
        return float('nan')

    if math.isinf(value):
        return value

    return float(math.trunc(value))


def round_half_up(value: Number, decimals: int = 0) -> float:
    """
    Round value using half-up tie-breaking (standard rounding).

    Detailed Description:
        Rounds to nearest value. When exactly halfway between two values
        (e.g., 2.5), rounds away from zero (2.5 -> 3.0, -2.5 -> -3.0).
        This is the most common rounding method taught in schools.

    Args:
        value (Number): Value to round
        decimals (int): Number of decimal places (default: 0)
            - decimals >= 0: Round to that many decimal places
            - decimals < 0: Round to left of decimal (e.g., -1 rounds to tens)

    Returns:
        float: Rounded value

    Algorithm:
        1. Scale value by 10^decimals
        2. Add 0.5 * sign(value)
        3. Truncate to integer
        4. Scale back by 10^(-decimals)

    Complexity:
        Time: O(1)
        Space: O(1)

    Special Cases:
        - Ties round away from zero (0.5 -> 1, -0.5 -> -1)
        - NaN returns NaN
        - Infinity returns infinity

    Examples:
        >>> round_half_up(2.5)
        3.0

        >>> round_half_up(2.4)
        2.0

        >>> round_half_up(-2.5)
        -3.0

        >>> round_half_up(3.14159, 2)
        3.14

        >>> round_half_up(3.14159, 4)
        3.1416

        >>> round_half_up(1234.5, -1)
        1230.0

    See Also:
        - round_half_even: Banker's rounding (ties to even)
        - round_to_digits: Alias with explicit naming

    Notes:
        Python's built-in round() uses half-even rounding, not half-up
        This function provides the traditional "away from zero" behavior

    References:
        [1] IEEE 754-2008 Section 4.3.1: Rounding-direction attributes

    Version: 0.1.0
    """
    if math.isnan(value):
        return float('nan')

    if math.isinf(value):
        return value

    if not isinstance(decimals, int):
        raise ValueError("Decimals must be an integer")

    # Calculate scaling factor
    multiplier = 10 ** decimals

    # Scale, round, and scale back
    scaled = value * multiplier

    # Add 0.5 with the sign of the value for half-up behavior
    if scaled >= 0:
        rounded = math.floor(scaled + 0.5)
    else:
        rounded = math.ceil(scaled - 0.5)

    return float(rounded / multiplier)


def round_half_even(value: Number, decimals: int = 0) -> float:
    """
    Round value using half-even tie-breaking (banker's rounding).

    Detailed Description:
        Rounds to nearest value. When exactly halfway between two values
        (e.g., 2.5), rounds to the nearest even integer (2.5 -> 2.0, 3.5 -> 4.0).
        This method reduces bias in repeated rounding operations and is the
        default in IEEE 754 and Python's built-in round().

    Args:
        value (Number): Value to round
        decimals (int): Number of decimal places (default: 0)
            - decimals >= 0: Round to that many decimal places
            - decimals < 0: Round to left of decimal (e.g., -1 rounds to tens)

    Returns:
        float: Rounded value

    Algorithm:
        Uses Python's built-in round() which implements IEEE 754
        roundTiesToEven (banker's rounding)

    Complexity:
        Time: O(1)
        Space: O(1)

    Special Cases:
        - Ties round to nearest even value (0.5 -> 0, 1.5 -> 2)
        - NaN returns NaN
        - Infinity returns infinity
        - Reduces statistical bias in repeated operations

    Examples:
        >>> round_half_even(0.5)
        0.0

        >>> round_half_even(1.5)
        2.0

        >>> round_half_even(2.5)
        2.0

        >>> round_half_even(3.5)
        4.0

        >>> round_half_even(-0.5)
        0.0

        >>> round_half_even(-1.5)
        -2.0

        >>> round_half_even(3.14159, 2)
        3.14

        >>> round_half_even(2.55, 1)
        2.6

    See Also:
        - round_half_up: Standard rounding (ties away from zero)
        - round_to_digits: Alias for round_half_even

    Notes:
        This is the default rounding in Python 3, IEEE 754, and most
        financial applications. Preferred for statistical work.

    References:
        [1] IEEE 754-2008 Section 4.3.1: roundTiesToEven
        [2] Python round() documentation

    Version: 0.1.0
    """
    if math.isnan(value):
        return float('nan')

    if math.isinf(value):
        return value

    if not isinstance(decimals, int):
        raise ValueError("Decimals must be an integer")

    # Python's round() uses banker's rounding (half-even)
    return float(round(value, decimals))


def round_to_digits(value: Number, decimals: int = 0, method: str = 'half_even') -> float:
    """
    Round value to specified decimal places using chosen method.

    Detailed Description:
        Flexible rounding function that supports multiple rounding strategies.
        Provides a unified interface for all rounding operations with explicit
        method selection.

    Args:
        value (Number): Value to round
        decimals (int): Number of decimal places (default: 0)
            - decimals >= 0: Round to that many decimal places
            - decimals < 0: Round to left of decimal point
        method (str): Rounding method (default: 'half_even')
            - 'half_even': Banker's rounding (ties to even)
            - 'half_up': Standard rounding (ties away from zero)
            - 'floor': Always round down (toward -inf)
            - 'ceil': Always round up (toward +inf)
            - 'trunc': Always round toward zero

    Returns:
        float: Rounded value

    Raises:
        ValueError: If method is not recognized

    Complexity:
        Time: O(1)
        Space: O(1)

    Examples:
        >>> round_to_digits(2.5, method='half_even')
        2.0

        >>> round_to_digits(2.5, method='half_up')
        3.0

        >>> round_to_digits(3.14159, 2, 'half_even')
        3.14

        >>> round_to_digits(3.7, method='floor')
        3.0

        >>> round_to_digits(3.2, method='ceil')
        4.0

        >>> round_to_digits(-3.7, method='trunc')
        -3.0

        >>> round_to_digits(1234.56, -1, 'half_up')
        1230.0

    See Also:
        - round_half_even: Direct banker's rounding
        - round_half_up: Direct standard rounding
        - floor, ceil, trunc: Direct rounding modes

    Notes:
        Provides explicit control over rounding strategy
        Useful when rounding behavior must be documented or configurable

    Version: 0.1.0
    """
    if math.isnan(value):
        return float('nan')

    if math.isinf(value):
        return value

    if not isinstance(decimals, int):
        raise ValueError("Decimals must be an integer")

    # Normalize method name
    method = method.lower().replace('-', '_')

    # Route to appropriate rounding function
    if method == 'half_even':
        return round_half_even(value, decimals)
    elif method == 'half_up':
        return round_half_up(value, decimals)
    elif method == 'floor':
        if decimals == 0:
            return floor(value)
        else:
            multiplier = 10 ** decimals
            return floor(value * multiplier) / multiplier
    elif method == 'ceil':
        if decimals == 0:
            return ceil(value)
        else:
            multiplier = 10 ** decimals
            return ceil(value * multiplier) / multiplier
    elif method == 'trunc':
        if decimals == 0:
            return trunc(value)
        else:
            multiplier = 10 ** decimals
            return trunc(value * multiplier) / multiplier
    else:
        raise ValueError(
            f"Unknown rounding method: '{method}'. "
            f"Valid methods: 'half_even', 'half_up', 'floor', 'ceil', 'trunc'"
        )
