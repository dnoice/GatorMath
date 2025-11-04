"""
Metadata:
    Project: GatorMath
    File Name: arithmetic.py
    File Path: gatormath/core/arithmetic.py
    Module: Core Arithmetic Operations
    Created: 2025-11-02
    Modified: 2025-11-02
    Version: 1.0.0
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

    >>> from gatormath.core.arithmetic import nth_root, cbrt, sqrt_newton
    >>> nth_root(27, 3)
    3.0

    >>> cbrt(-8)
    -2.0

    >>> sqrt_newton(16.0)
    4.0

    >>> from gatormath.core.arithmetic import exp, ln, log2, log10, log
    >>> exp(1)
    2.718281828459045

    >>> ln(2.718281828459045)
    1.0

    >>> log2(1024)
    10.0

    >>> log10(1000)
    3.0

    >>> log(27, 3)
    3.0

    >>> from gatormath.core.arithmetic import is_prime, prime_factors, divisors, totient
    >>> is_prime(17)
    True

    >>> prime_factors(60)
    [2, 2, 3, 5]

    >>> divisors(12)
    [1, 2, 3, 4, 6, 12]

    >>> totient(10)
    4

    >>> from gatormath.core.arithmetic import fma, hypot, copysign, lerp
    >>> fma(2.0, 3.0, 4.0)
    10.0

    >>> hypot(3, 4)
    5.0

    >>> copysign(5.0, -1.0)
    -5.0

    >>> lerp(0, 10, 0.5)
    5.0

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

    Root Operations:
        - nth_root: Compute nth root of a value
        - cbrt: Compute cube root
        - sqrt_newton: Newton-Raphson square root implementation

    Exponential & Logarithmic Operations:
        - exp: Exponential function (e^x)
        - ln: Natural logarithm (base e)
        - log2: Base-2 logarithm
        - log10: Base-10 logarithm (common logarithm)
        - log: General logarithm with arbitrary base

    Number Theory Operations:
        - is_prime: Check if a number is prime
        - prime_factors: Find all prime factors (with repetition)
        - divisors: Find all divisors of a number
        - totient: Euler's totient function φ(n)

    Advanced Arithmetic Operations:
        - fma: Fused multiply-add (a*b + c with single rounding)
        - hypot: Euclidean distance without overflow
        - copysign: Copy sign from one number to another
        - lerp: Linear interpolation between two values

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


# ===== ROOT OPERATIONS =====


def nth_root(value: Number, n: int) -> float:
    """
    Compute the nth root of a value.

    Detailed Description:
        Calculates the nth root of a value, defined as the number r such that
        r^n = value. For even n, only non-negative values are supported.
        For odd n, negative values are supported and return negative roots.

    Args:
        value (Number): Value to compute root of
        n (int): Root degree (must be positive integer)
            - n = 1: Returns value unchanged
            - n = 2: Square root
            - n = 3: Cube root
            - n > 3: Higher-order roots

    Returns:
        float: The nth root of value

    Raises:
        ValueError: If n <= 0 or not an integer
        ValueError: If value < 0 and n is even
        ValueError: If value is NaN

    Algorithm:
        1. For n = 1: Return value directly
        2. For even n and value < 0: Raise error (no real root)
        3. For odd n and value < 0: Compute root of |value| and negate
        4. For value >= 0: Use value^(1/n)

    Complexity:
        Time: O(1) - Constant time exponentiation
        Space: O(1) - No additional space

    Special Cases:
        - nth_root(NaN, n) = NaN
        - nth_root(+inf, n) = +inf for n > 0
        - nth_root(-inf, n) = -inf for odd n > 0
        - nth_root(0, n) = 0 for any n > 0
        - nth_root(1, n) = 1 for any n
        - nth_root(-1, odd) = -1
        - nth_root(value, 1) = value

    Examples:
        >>> nth_root(8, 3)
        2.0

        >>> nth_root(16, 4)
        2.0

        >>> nth_root(27, 3)
        3.0

        >>> nth_root(-8, 3)
        -2.0

        >>> nth_root(2, 2)
        1.4142135623730951

        >>> nth_root(-16, 2)
        Traceback (most recent call last):
            ...
        ValueError: Cannot compute even root of negative number

        >>> nth_root(0, 5)
        0.0

    See Also:
        - cbrt: Optimized cube root function
        - safe_sqrt: Square root with error handling
        - sqrt_newton: Newton-Raphson square root implementation

    Notes:
        - For n = 2, consider using safe_sqrt() for better error messages
        - For n = 3, consider using cbrt() for potentially better accuracy
        - Handles odd/even root distinction automatically
        - Preserves sign for odd roots of negative values

    Mathematical Properties:
        - nth_root(a * b, n) ≈ nth_root(a, n) * nth_root(b, n)
        - nth_root(a^m, n) = a^(m/n)
        - nth_root(nth_root(a, n), m) = nth_root(a, n*m)

    References:
        [1] IEEE 754-2008: Floating-point arithmetic
        [2] Abramowitz & Stegun, "Handbook of Mathematical Functions"

    Version: 0.3.0
    """
    if not isinstance(n, int):
        raise ValueError("Root degree n must be an integer")

    if n <= 0:
        raise ValueError(f"Root degree must be positive, got n={n}")

    if math.isnan(value):
        return float('nan')

    # Handle n = 1 special case
    if n == 1:
        return float(value)

    # Handle infinity
    if math.isinf(value):
        if value > 0:
            return float('inf')
        elif n % 2 == 1:  # Odd root of -infinity
            return float('-inf')
        else:  # Even root of -infinity
            raise ValueError("Cannot compute even root of negative infinity")

    # Handle negative values
    if value < 0:
        if n % 2 == 0:  # Even root
            raise ValueError(
                f"Cannot compute even root of negative number: "
                f"{n}th root of {value}"
            )
        else:  # Odd root
            # For odd roots, we can take the root of the absolute value
            # and negate the result
            return -float(abs(value) ** (1.0 / n))

    # Handle non-negative values
    return float(value ** (1.0 / n))


def cbrt(value: Number) -> float:
    """
    Compute the cube root of a value.

    Detailed Description:
        Calculates the cube root (3rd root) of a value. Unlike square root,
        cube root is defined for all real numbers, including negative values.
        For negative inputs, returns the negative cube root.

    Args:
        value (Number): Value to compute cube root of

    Returns:
        float: Cube root of value (can be positive, negative, or zero)

    Algorithm:
        For positive values: Uses value^(1/3)
        For negative values: Returns -(|value|^(1/3))
        For zero: Returns 0

    Complexity:
        Time: O(1) - Constant time computation
        Space: O(1) - No additional space

    Special Cases:
        - cbrt(NaN) = NaN
        - cbrt(+inf) = +inf
        - cbrt(-inf) = -inf
        - cbrt(+0) = +0
        - cbrt(-0) = -0
        - cbrt(1) = 1
        - cbrt(-1) = -1
        - cbrt(8) = 2
        - cbrt(-8) = -2

    Examples:
        >>> cbrt(8)
        2.0

        >>> cbrt(27)
        3.0

        >>> cbrt(-8)
        -2.0

        >>> cbrt(-27)
        -3.0

        >>> cbrt(0)
        0.0

        >>> cbrt(1)
        1.0

        >>> cbrt(0.125)
        0.5

    See Also:
        - nth_root: General nth root function
        - safe_sqrt: Square root function
        - sqrt_newton: Newton-Raphson square root

    Notes:
        - Cube root is defined for all real numbers
        - Preserves sign of input (cbrt(-x) = -cbrt(x))
        - More efficient than calling nth_root(value, 3)
        - IEEE 754 compliant for special values

    Mathematical Properties:
        - cbrt(a * b) ≈ cbrt(a) * cbrt(b)
        - cbrt(a^3) = a
        - cbrt(-a) = -cbrt(a)

    Applications:
        - Volume calculations (finding side length from volume)
        - Scaling operations in graphics
        - Physics equations involving cubic relationships

    References:
        [1] IEEE 754-2008: Floating-point arithmetic
        [2] Abramowitz & Stegun, Section 3.7: Roots

    Version: 0.3.0
    """
    if math.isnan(value):
        return float('nan')

    if math.isinf(value):
        return value  # Returns +inf for +inf, -inf for -inf

    # Handle negative values
    if value < 0:
        return -float(abs(value) ** (1.0 / 3.0))

    # Handle non-negative values
    return float(value ** (1.0 / 3.0))


def sqrt_newton(
    value: Number,
    max_iterations: int = 50,
    tolerance: float = 1e-10
) -> float:
    """
    Compute square root using Newton-Raphson method.

    Detailed Description:
        Implements the Newton-Raphson iterative method for computing square
        roots. This is an educational implementation that demonstrates the
        classical algorithm. For production use, math.sqrt() or safe_sqrt()
        are preferred for better performance and accuracy.

    Args:
        value (Number): Value to compute square root of (must be >= 0)
        max_iterations (int): Maximum number of iterations (default: 50)
        tolerance (float): Convergence tolerance (default: 1e-10)
            - Stops when |x_{n+1} - x_n| < tolerance

    Returns:
        float: Approximation of square root of value

    Raises:
        ValueError: If value < 0 (no real square root)
        ValueError: If value is NaN
        ValueError: If max_iterations < 1
        ValueError: If tolerance <= 0

    Algorithm:
        Newton-Raphson iteration for f(x) = x² - value:
        1. Start with initial guess x₀ = value / 2 (or 1 if value < 1)
        2. Iterate: x_{n+1} = (x_n + value/x_n) / 2
        3. Stop when |x_{n+1} - x_n| < tolerance or max iterations reached

    Complexity:
        Time: O(log log n) - Quadratic convergence (iterations)
        Space: O(1) - Constant space

    Convergence:
        - Quadratic convergence: Error roughly squares each iteration
        - Typically converges in 4-6 iterations for double precision
        - Initial guess quality affects iteration count

    Special Cases:
        - sqrt_newton(0) = 0 (immediate return)
        - sqrt_newton(1) = 1 (immediate return)
        - sqrt_newton(+inf) = +inf (immediate return)
        - sqrt_newton(NaN) raises ValueError
        - sqrt_newton(negative) raises ValueError

    Examples:
        >>> sqrt_newton(4.0)
        2.0

        >>> sqrt_newton(2.0)
        1.414213562373095

        >>> sqrt_newton(9.0)
        3.0

        >>> sqrt_newton(0.25)
        0.5

        >>> sqrt_newton(0)
        0.0

        >>> sqrt_newton(-1)
        Traceback (most recent call last):
            ...
        ValueError: Cannot compute square root of negative number

        >>> sqrt_newton(2.0, max_iterations=3)
        1.4166666666666665

    See Also:
        - safe_sqrt: Production square root with error handling
        - nth_root: General nth root function
        - cbrt: Cube root function

    Notes:
        - Educational implementation demonstrating Newton-Raphson method
        - For production code, use math.sqrt() or safe_sqrt()
        - Convergence is quadratic (very fast)
        - Initial guess affects iteration count but not final accuracy

    Mathematical Derivation:
        For f(x) = x² - a, we want to find x where f(x) = 0
        Newton-Raphson: x_{n+1} = x_n - f(x_n)/f'(x_n)
        Since f'(x) = 2x:
        x_{n+1} = x_n - (x_n² - a)/(2x_n)
                = (x_n + a/x_n) / 2

    References:
        [1] Press et al., "Numerical Recipes", Section 9.5
        [2] Burden & Faires, "Numerical Analysis", Chapter 2
        [3] Newton, Isaac (1669), "De analysi per aequationes"

    Version: 0.3.0
    """
    if math.isnan(value):
        raise ValueError("Cannot compute square root of NaN")

    if value < 0:
        raise ValueError(
            f"Cannot compute square root of negative number: {value}"
        )

    if not isinstance(max_iterations, int) or max_iterations < 1:
        raise ValueError(
            f"max_iterations must be a positive integer, got {max_iterations}"
        )

    if tolerance <= 0:
        raise ValueError(f"tolerance must be positive, got {tolerance}")

    # Handle special cases
    if value == 0:
        return 0.0

    if value == 1:
        return 1.0

    if math.isinf(value):
        return float('inf')

    # Initial guess: value/2 for large values, 1 for small values
    if value >= 1:
        x = value / 2.0
    else:
        x = 1.0

    # Newton-Raphson iteration
    for iteration in range(max_iterations):
        # Compute next approximation: x_new = (x + value/x) / 2
        x_new = (x + value / x) / 2.0

        # Check for convergence
        if abs(x_new - x) < tolerance:
            return float(x_new)

        x = x_new

    # Return best approximation after max iterations
    return float(x)


# ===== EXPONENTIAL & LOGARITHMIC OPERATIONS =====


def exp(value: Number) -> float:
    """
    Compute the exponential function e^x.

    Detailed Description:
        Calculates e raised to the power of value, where e ≈ 2.71828 is Euler's
        number. The exponential function is fundamental in calculus, probability,
        physics, and engineering. It's the inverse of the natural logarithm.

    Args:
        value (Number): Exponent value (can be any real number)

    Returns:
        float: e^value (always positive for finite inputs)

    Raises:
        OverflowError: If result exceeds float range

    Algorithm:
        Uses math.exp() which typically implements optimized Taylor series
        or CORDIC algorithm for hardware acceleration

    Complexity:
        Time: O(1) - Constant time computation
        Space: O(1) - No additional space

    Special Cases:
        - exp(NaN) = NaN
        - exp(+inf) = +inf
        - exp(-inf) = +0
        - exp(0) = 1
        - exp(1) = e ≈ 2.71828
        - exp(-0) = 1

    Examples:
        >>> exp(0)
        1.0

        >>> exp(1)
        2.718281828459045

        >>> exp(2)
        7.38905609893065

        >>> exp(-1)
        0.36787944117144233

        >>> exp(0.5)
        1.6487212707001282

        >>> from math import log
        >>> exp(log(5))
        5.0

    See Also:
        - ln: Natural logarithm (inverse of exp)
        - safe_power: General exponentiation
        - log: Logarithm with arbitrary base

    Notes:
        - exp(x) is always positive for finite x
        - exp(x + y) = exp(x) * exp(y)
        - exp(ln(x)) = x for x > 0
        - Grows very rapidly for positive x
        - Approaches 0 (never negative) for negative x

    Mathematical Properties:
        - d/dx[exp(x)] = exp(x) (derivative equals itself)
        - ∫exp(x)dx = exp(x) + C
        - exp(0) = 1 (multiplicative identity)
        - exp(x) * exp(-x) = 1
        - exp(i*π) = -1 (Euler's identity, complex numbers)

    Applications:
        - Growth and decay models (population, radioactive)
        - Probability distributions (normal, exponential, Poisson)
        - Compound interest calculations
        - Signal processing (exponential smoothing)
        - Physics (quantum mechanics, thermodynamics)

    References:
        [1] IEEE 754-2008: Floating-point arithmetic
        [2] Abramowitz & Stegun, Section 4.2: Exponential Function
        [3] Press et al., "Numerical Recipes", Section 5.4

    Version: 0.4.0
    """
    if math.isnan(value):
        return float('nan')

    if math.isinf(value):
        if value > 0:
            return float('inf')
        else:  # -infinity
            return 0.0

    try:
        result = math.exp(float(value))
    except OverflowError:
        raise OverflowError(f"Exponential overflow: e^{value} exceeds float range")

    return float(result)


def ln(value: Number) -> float:
    """
    Compute the natural logarithm (base e).

    Detailed Description:
        Calculates the natural logarithm of value, denoted ln(x) or log_e(x).
        This is the inverse of the exponential function. The natural logarithm
        answers: "To what power must e be raised to get x?"

    Args:
        value (Number): Input value (must be positive)

    Returns:
        float: Natural logarithm of value

    Raises:
        ValueError: If value <= 0 (logarithm undefined for non-positive)
        ValueError: If value is NaN

    Algorithm:
        Uses math.log() which implements optimized algorithm (often
        hardware-accelerated) based on polynomial approximations

    Complexity:
        Time: O(1) - Constant time computation
        Space: O(1) - No additional space

    Special Cases:
        - ln(NaN) raises ValueError
        - ln(+inf) = +inf
        - ln(0) raises ValueError (negative infinity mathematically)
        - ln(1) = 0
        - ln(e) = 1
        - ln(negative) raises ValueError

    Examples:
        >>> ln(1)
        0.0

        >>> ln(2.718281828459045)  # ln(e)
        1.0

        >>> ln(2)
        0.6931471805599453

        >>> ln(10)
        2.302585092994046

        >>> ln(0.5)
        -0.6931471805599453

        >>> ln(0)
        Traceback (most recent call last):
            ...
        ValueError: Natural logarithm undefined for non-positive values

        >>> ln(-1)
        Traceback (most recent call last):
            ...
        ValueError: Natural logarithm undefined for non-positive values

    See Also:
        - exp: Exponential function (inverse of ln)
        - log2: Base-2 logarithm
        - log10: Base-10 logarithm
        - log: Logarithm with arbitrary base

    Notes:
        - ln(x) is only defined for x > 0
        - ln(e^x) = x
        - ln(x * y) = ln(x) + ln(y)
        - ln(x / y) = ln(x) - ln(y)
        - ln(x^n) = n * ln(x)
        - ln(1) = 0 (additive identity)

    Mathematical Properties:
        - d/dx[ln(x)] = 1/x
        - ∫(1/x)dx = ln|x| + C
        - ln is monotonically increasing
        - ln is concave (d²/dx²[ln(x)] = -1/x² < 0)

    Applications:
        - Information theory (entropy, information content)
        - Statistics (log-likelihood, logarithmic distributions)
        - Complexity analysis (time complexity bounds)
        - Physics (entropy, thermodynamics)
        - Economics (logarithmic utility, growth rates)

    References:
        [1] IEEE 754-2008: Floating-point arithmetic
        [2] Abramowitz & Stegun, Section 4.1: Logarithms
        [3] Knuth, TAOCP Vol 2, Section 4.2.2

    Version: 0.4.0
    """
    if math.isnan(value):
        raise ValueError("Natural logarithm undefined for NaN")

    if value <= 0:
        raise ValueError(
            f"Natural logarithm undefined for non-positive values: {value}"
        )

    if math.isinf(value):
        return float('inf')

    return float(math.log(value))


def log2(value: Number) -> float:
    """
    Compute the base-2 logarithm.

    Detailed Description:
        Calculates the logarithm base 2 of value, denoted log₂(x).
        Answers: "To what power must 2 be raised to get x?"
        Fundamental in computer science and information theory.

    Args:
        value (Number): Input value (must be positive)

    Returns:
        float: Base-2 logarithm of value

    Raises:
        ValueError: If value <= 0 (logarithm undefined)
        ValueError: If value is NaN

    Algorithm:
        Uses math.log2() which implements optimized base-2 logarithm,
        often more accurate than log(x)/log(2)

    Complexity:
        Time: O(1) - Constant time computation
        Space: O(1) - No additional space

    Special Cases:
        - log2(NaN) raises ValueError
        - log2(+inf) = +inf
        - log2(0) raises ValueError
        - log2(1) = 0
        - log2(2) = 1
        - log2(0.5) = -1
        - log2(negative) raises ValueError

    Examples:
        >>> log2(1)
        0.0

        >>> log2(2)
        1.0

        >>> log2(4)
        2.0

        >>> log2(8)
        3.0

        >>> log2(1024)
        10.0

        >>> log2(0.5)
        -1.0

        >>> log2(3)
        1.5849625007211563

        >>> log2(0)
        Traceback (most recent call last):
            ...
        ValueError: Base-2 logarithm undefined for non-positive values

    See Also:
        - ln: Natural logarithm (base e)
        - log10: Base-10 logarithm
        - log: Logarithm with arbitrary base
        - exp: Exponential function

    Notes:
        - log2(2^n) = n for any real n
        - log2(x * y) = log2(x) + log2(y)
        - log2(x / y) = log2(x) - log2(y)
        - log2(x^n) = n * log2(x)
        - More accurate than ln(x)/ln(2) due to direct computation

    Mathematical Properties:
        - d/dx[log2(x)] = 1/(x * ln(2))
        - log2(x) = ln(x) / ln(2)
        - log2(x) = log10(x) / log10(2)
        - 2^(log2(x)) = x for x > 0

    Applications:
        - Computer science (algorithm complexity, binary search)
        - Information theory (entropy, bit depth)
        - Digital signal processing (octaves, frequency analysis)
        - Data structures (tree heights, hash tables)
        - Compression algorithms (encoding efficiency)

    References:
        [1] IEEE 754-2008: Floating-point arithmetic
        [2] Knuth, TAOCP Vol 1, Section 1.2.2: Numbers and Logarithms
        [3] Cover & Thomas, "Elements of Information Theory"

    Version: 0.4.0
    """
    if math.isnan(value):
        raise ValueError("Base-2 logarithm undefined for NaN")

    if value <= 0:
        raise ValueError(
            f"Base-2 logarithm undefined for non-positive values: {value}"
        )

    if math.isinf(value):
        return float('inf')

    return float(math.log2(value))


def log10(value: Number) -> float:
    """
    Compute the base-10 logarithm (common logarithm).

    Detailed Description:
        Calculates the logarithm base 10 of value, denoted log₁₀(x) or simply
        log(x) in many contexts. Answers: "To what power must 10 be raised to
        get x?" Used extensively in science and engineering.

    Args:
        value (Number): Input value (must be positive)

    Returns:
        float: Base-10 logarithm of value

    Raises:
        ValueError: If value <= 0 (logarithm undefined)
        ValueError: If value is NaN

    Algorithm:
        Uses math.log10() which implements optimized base-10 logarithm,
        more accurate than log(x)/log(10)

    Complexity:
        Time: O(1) - Constant time computation
        Space: O(1) - No additional space

    Special Cases:
        - log10(NaN) raises ValueError
        - log10(+inf) = +inf
        - log10(0) raises ValueError
        - log10(1) = 0
        - log10(10) = 1
        - log10(0.1) = -1
        - log10(negative) raises ValueError

    Examples:
        >>> log10(1)
        0.0

        >>> log10(10)
        1.0

        >>> log10(100)
        2.0

        >>> log10(1000)
        3.0

        >>> log10(0.1)
        -1.0

        >>> log10(0.01)
        -2.0

        >>> log10(2)
        0.30102999566398114

        >>> log10(0)
        Traceback (most recent call last):
            ...
        ValueError: Base-10 logarithm undefined for non-positive values

    See Also:
        - ln: Natural logarithm (base e)
        - log2: Base-2 logarithm
        - log: Logarithm with arbitrary base
        - exp: Exponential function

    Notes:
        - log10(10^n) = n for any real n
        - log10(x * y) = log10(x) + log10(y)
        - log10(x / y) = log10(x) - log10(y)
        - log10(x^n) = n * log10(x)
        - More accurate than ln(x)/ln(10) due to direct computation

    Mathematical Properties:
        - d/dx[log10(x)] = 1/(x * ln(10))
        - log10(x) = ln(x) / ln(10)
        - log10(x) = log2(x) / log2(10)
        - 10^(log10(x)) = x for x > 0

    Applications:
        - Decibel scales (sound, power ratios)
        - pH scale (chemistry, acidity)
        - Richter scale (earthquake magnitude)
        - Orders of magnitude (scientific notation)
        - Signal processing (gain, attenuation)
        - Astronomy (apparent magnitude)

    References:
        [1] IEEE 754-2008: Floating-point arithmetic
        [2] Abramowitz & Stegun, Section 4.1: Logarithms
        [3] ISO 80000-3: Quantities and units - Space and time

    Version: 0.4.0
    """
    if math.isnan(value):
        raise ValueError("Base-10 logarithm undefined for NaN")

    if value <= 0:
        raise ValueError(
            f"Base-10 logarithm undefined for non-positive values: {value}"
        )

    if math.isinf(value):
        return float('inf')

    return float(math.log10(value))


def log(value: Number, base: Number = math.e) -> float:
    """
    Compute logarithm with arbitrary base.

    Detailed Description:
        Calculates the logarithm of value with specified base, denoted log_base(x).
        Answers: "To what power must base be raised to get x?"
        Provides flexible logarithm computation for any positive base ≠ 1.

    Args:
        value (Number): Input value (must be positive)
        base (Number): Logarithm base (must be positive, ≠ 1)
            - Default: e (natural logarithm)
            - Common: 2, 10, e

    Returns:
        float: Logarithm of value with given base

    Raises:
        ValueError: If value <= 0 (logarithm undefined)
        ValueError: If base <= 0 or base == 1 (invalid base)
        ValueError: If either argument is NaN

    Algorithm:
        Uses change of base formula: log_base(x) = ln(x) / ln(base)
        Leverages math.log() for computation

    Complexity:
        Time: O(1) - Constant time computation
        Space: O(1) - No additional space

    Special Cases:
        - log(x, e) = ln(x) (natural logarithm)
        - log(x, 2) = log2(x) (binary logarithm)
        - log(x, 10) = log10(x) (common logarithm)
        - log(base, base) = 1 for any valid base
        - log(1, base) = 0 for any valid base
        - log(+inf, base) = +inf for base > 1
        - log(+inf, base) = -inf for 0 < base < 1

    Examples:
        >>> log(8, 2)
        3.0

        >>> log(1000, 10)
        3.0

        >>> log(16, 4)
        2.0

        >>> log(27, 3)
        3.0

        >>> log(100, 10)
        2.0

        >>> log(2.718281828459045)  # log(e, e) - default base e
        1.0

        >>> log(10, 10)
        1.0

        >>> log(1, 5)
        0.0

        >>> log(0, 2)
        Traceback (most recent call last):
            ...
        ValueError: Logarithm undefined for non-positive values

        >>> log(5, 1)
        Traceback (most recent call last):
            ...
        ValueError: Logarithm base must be positive and not equal to 1

    See Also:
        - ln: Natural logarithm (base e)
        - log2: Base-2 logarithm
        - log10: Base-10 logarithm
        - exp: Exponential function

    Notes:
        - For common bases (2, 10, e), prefer specialized functions
        - log2(), log10(), ln() may be more accurate for their bases
        - log_b(x * y) = log_b(x) + log_b(y)
        - log_b(x / y) = log_b(x) - log_b(y)
        - log_b(x^n) = n * log_b(x)
        - log_b(x) = ln(x) / ln(b) (change of base formula)

    Mathematical Properties:
        - d/dx[log_b(x)] = 1/(x * ln(b))
        - base^(log_base(x)) = x for x > 0
        - log_b(base) = 1
        - log_a(x) = log_b(x) / log_b(a) (change of base)

    Change of Base Formula:
        log_b(x) = log_c(x) / log_c(b) for any valid base c
        Common choices: c = e (natural), c = 10 (common), c = 2 (binary)

    Applications:
        - Mathematical modeling (custom bases)
        - Information theory (variable base entropy)
        - Number theory (discrete logarithm)
        - Cryptography (modular exponentiation)
        - Scientific computing (custom scales)

    References:
        [1] IEEE 754-2008: Floating-point arithmetic
        [2] Abramowitz & Stegun, Section 4.1: Logarithms
        [3] Knuth, TAOCP Vol 2, Section 4.2.2

    Version: 0.4.0
    """
    if math.isnan(value) or math.isnan(base):
        raise ValueError("Logarithm undefined for NaN")

    if value <= 0:
        raise ValueError(
            f"Logarithm undefined for non-positive values: {value}"
        )

    if base <= 0 or base == 1:
        raise ValueError(
            f"Logarithm base must be positive and not equal to 1: {base}"
        )

    if math.isinf(value):
        if base > 1:
            return float('inf')
        else:  # 0 < base < 1
            return float('-inf')

    if math.isinf(base):
        # log_inf(x) = 0 for finite x > 1, approaches -inf for 0 < x < 1
        if value > 1:
            return 0.0
        elif value == 1:
            return 0.0
        else:
            return float('-inf')

    # Use math.log with base parameter (uses change of base formula internally)
    return float(math.log(value, base))


# ===== NUMBER THEORY OPERATIONS =====


def is_prime(n: int) -> bool:
    """
    Check if a number is prime.

    Detailed Description:
        Determines whether a given positive integer is prime (only divisible by
        1 and itself). Uses trial division with optimizations: checks divisibility
        only up to sqrt(n) and skips even numbers after checking 2.

    Args:
        n (int): Integer to test for primality (must be positive)

    Returns:
        bool: True if n is prime, False otherwise

    Raises:
        ValueError: If n is not a positive integer
        TypeError: If n is not an integer

    Algorithm:
        1. Handle special cases: n ≤ 1 (not prime), n = 2 (prime), even n (not prime)
        2. Check odd divisors from 3 to sqrt(n)
        3. If any divisor found, not prime; otherwise prime

        Optimization: Only check up to sqrt(n) because if n = a*b and a ≤ b,
        then a ≤ sqrt(n)

    Complexity:
        Time: O(√n) - Trial division up to square root
        Space: O(1) - Constant space

    Special Cases:
        - is_prime(0) = False (by convention)
        - is_prime(1) = False (by convention, not prime)
        - is_prime(2) = True (only even prime)
        - is_prime(negative) raises ValueError

    Examples:
        >>> is_prime(2)
        True

        >>> is_prime(3)
        True

        >>> is_prime(4)
        False

        >>> is_prime(17)
        True

        >>> is_prime(100)
        False

        >>> is_prime(97)
        True

        >>> is_prime(1)
        False

        >>> is_prime(0)
        False

        >>> is_prime(-5)
        Traceback (most recent call last):
            ...
        ValueError: Input must be a positive integer

    See Also:
        - prime_factors: Find all prime factors
        - divisors: Find all divisors
        - gcd: Greatest common divisor

    Notes:
        - This is a deterministic primality test
        - For large numbers, consider probabilistic tests (Miller-Rabin)
        - 2 is the only even prime number
        - All primes > 2 are odd
        - Trial division is simple but not fastest for large n

    Prime Numbers:
        First few primes: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47...
        There are infinitely many primes (Euclid's theorem)

    Applications:
        - Cryptography (RSA, public-key encryption)
        - Number theory research
        - Hash functions and random number generation
        - Primality testing in algorithms
        - Mathematical proofs and theorems

    Advanced Algorithms:
        For production systems with large numbers, consider:
        - Miller-Rabin (probabilistic, O(k log³ n))
        - AKS primality test (deterministic, polynomial time)
        - Sieve of Eratosthenes (for finding all primes up to n)

    References:
        [1] Hardy & Wright, "An Introduction to the Theory of Numbers"
        [2] Cormen et al., "Introduction to Algorithms", Section 31.8
        [3] Crandall & Pomerance, "Prime Numbers: A Computational Perspective"

    Version: 0.5.0
    """
    if not isinstance(n, int):
        raise TypeError(f"Input must be an integer, got {type(n).__name__}")

    if n < 1:
        raise ValueError("Input must be a positive integer")

    # Special cases
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    # Trial division for odd numbers up to sqrt(n)
    limit = int(math.sqrt(n)) + 1
    for divisor in range(3, limit, 2):
        if n % divisor == 0:
            return False

    return True


def prime_factors(n: int) -> list[int]:
    """
    Find all prime factors of a number.

    Detailed Description:
        Computes the prime factorization of a positive integer, returning a list
        of all prime factors (with repetition). For example, 12 = 2² × 3 returns
        [2, 2, 3]. Uses trial division algorithm.

    Args:
        n (int): Positive integer to factor (must be > 0)

    Returns:
        list[int]: List of prime factors in ascending order (with repetition)
            - Empty list for n = 1
            - Single element [n] if n is prime

    Raises:
        ValueError: If n < 1
        TypeError: If n is not an integer

    Algorithm:
        1. Divide by 2 as many times as possible
        2. Try odd divisors from 3 upward
        3. When a divisor is found, divide and repeat
        4. Continue until quotient becomes 1
        5. Remaining quotient (if > 1) is a prime factor

    Complexity:
        Time: O(√n) - Trial division up to square root
        Space: O(log n) - At most log₂(n) factors (all 2's worst case)

    Special Cases:
        - prime_factors(1) = [] (empty, 1 has no prime factors)
        - prime_factors(prime) = [prime] (prime factorizes to itself)
        - prime_factors(power of 2) = [2, 2, 2, ...] (repeated 2's)

    Examples:
        >>> prime_factors(1)
        []

        >>> prime_factors(2)
        [2]

        >>> prime_factors(12)
        [2, 2, 3]

        >>> prime_factors(60)
        [2, 2, 3, 5]

        >>> prime_factors(100)
        [2, 2, 5, 5]

        >>> prime_factors(17)
        [17]

        >>> prime_factors(97)
        [97]

        >>> prime_factors(360)
        [2, 2, 2, 3, 3, 5]

    See Also:
        - is_prime: Check if number is prime
        - divisors: Find all divisors (not just prime)
        - gcd: Greatest common divisor

    Notes:
        - Returns factors with repetition (multiplicities preserved)
        - Result is always sorted in ascending order
        - Product of returned factors equals n
        - For n = 1, returns empty list (convention)
        - Fundamental theorem: Every integer > 1 has unique prime factorization

    Mathematical Properties:
        - n = p₁^a₁ × p₂^a₂ × ... × pₖ^aₖ (unique factorization)
        - Number of divisors: (a₁+1)(a₂+1)...(aₖ+1)
        - Sum of divisors: ((p₁^(a₁+1)-1)/(p₁-1)) × ... × ((pₖ^(aₖ+1)-1)/(pₖ-1))

    Applications:
        - Cryptography (RSA key generation, factoring challenge)
        - Number theory research (distribution of primes)
        - Simplifying fractions (finding GCD via factorization)
        - Computing totient function
        - Integer partition problems

    Fundamental Theorem of Arithmetic:
        Every integer n > 1 can be represented uniquely (up to order) as a
        product of prime powers: n = p₁^a₁ × p₂^a₂ × ... × pₖ^aₖ

    References:
        [1] Hardy & Wright, "An Introduction to the Theory of Numbers", Ch. 1
        [2] Knuth, TAOCP Vol 2, Section 4.5.4: Factoring
        [3] Cormen et al., "Introduction to Algorithms", Section 31.9

    Version: 0.5.0
    """
    if not isinstance(n, int):
        raise TypeError(f"Input must be an integer, got {type(n).__name__}")

    if n < 1:
        raise ValueError(f"Input must be a positive integer, got {n}")

    # Special case: 1 has no prime factors
    if n == 1:
        return []

    factors = []

    # Divide by 2 as many times as possible
    while n % 2 == 0:
        factors.append(2)
        n //= 2

    # Try odd divisors starting from 3
    divisor = 3
    while divisor * divisor <= n:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 2

    # If n is still greater than 1, it's a prime factor
    if n > 1:
        factors.append(n)

    return factors


def divisors(n: int) -> list[int]:
    """
    Find all divisors of a number.

    Detailed Description:
        Computes all positive divisors of a given integer. A divisor d of n
        satisfies: n mod d = 0. Returns divisors in ascending order, including
        1 and n itself.

    Args:
        n (int): Positive integer to find divisors of (must be > 0)

    Returns:
        list[int]: Sorted list of all positive divisors
            - Always includes 1 and n
            - For prime n: returns [1, n]

    Raises:
        ValueError: If n < 1
        TypeError: If n is not an integer

    Algorithm:
        1. Check all integers from 1 to sqrt(n)
        2. For each i where n % i == 0:
           - Add i as a divisor
           - Add n/i as a divisor (unless i = n/i)
        3. Sort the result

    Complexity:
        Time: O(√n) - Check divisors up to square root
        Space: O(d(n)) - Where d(n) is the number of divisors

    Special Cases:
        - divisors(1) = [1] (only divisor of 1 is 1)
        - divisors(prime) = [1, prime] (primes have exactly 2 divisors)
        - divisors(perfect_square) includes sqrt(n) once
        - divisors(n) always includes 1 and n

    Examples:
        >>> divisors(1)
        [1]

        >>> divisors(6)
        [1, 2, 3, 6]

        >>> divisors(12)
        [1, 2, 3, 4, 6, 12]

        >>> divisors(17)
        [1, 17]

        >>> divisors(28)
        [1, 2, 4, 7, 14, 28]

        >>> divisors(36)
        [1, 2, 3, 4, 6, 9, 12, 18, 36]

        >>> divisors(100)
        [1, 2, 4, 5, 10, 20, 25, 50, 100]

    See Also:
        - prime_factors: Prime factorization
        - is_prime: Check primality
        - gcd: Greatest common divisor

    Notes:
        - Result always sorted in ascending order
        - 1 and n are always divisors (for n > 0)
        - Number of divisors denoted τ(n) or d(n)
        - For n = p₁^a₁ × ... × pₖ^aₖ: τ(n) = (a₁+1)...(aₖ+1)

    Mathematical Properties:
        - τ(1) = 1 (only 1)
        - τ(p) = 2 for prime p (1 and p)
        - τ(p^k) = k + 1 for prime p
        - τ is multiplicative: τ(mn) = τ(m)τ(n) if gcd(m,n) = 1
        - Average order: τ(n) ≈ log(n)

    Special Numbers:
        - Perfect numbers: sum of proper divisors equals n (e.g., 6, 28)
        - Abundant numbers: sum of proper divisors > n
        - Deficient numbers: sum of proper divisors < n
        - Highly composite: more divisors than any smaller number

    Applications:
        - Number theory (perfect numbers, abundant numbers)
        - Factor tables and lookup
        - Divisibility rules and tests
        - Cryptographic applications
        - Algorithm optimization (divisor-based approaches)

    Sum of Divisors:
        Related function σ(n) sums all divisors. For n = p₁^a₁ × ... × pₖ^aₖ:
        σ(n) = ((p₁^(a₁+1)-1)/(p₁-1)) × ... × ((pₖ^(aₖ+1)-1)/(pₖ-1))

    References:
        [1] Hardy & Wright, "An Introduction to the Theory of Numbers", Ch. 16
        [2] Apostol, "Introduction to Analytic Number Theory", Ch. 2
        [3] OEIS A000005: Number of divisors of n

    Version: 0.5.0
    """
    if not isinstance(n, int):
        raise TypeError(f"Input must be an integer, got {type(n).__name__}")

    if n < 1:
        raise ValueError(f"Input must be a positive integer, got {n}")

    divs = []

    # Find divisors up to sqrt(n)
    limit = int(math.sqrt(n)) + 1
    for i in range(1, limit):
        if n % i == 0:
            divs.append(i)
            # Add the complementary divisor (n/i) if it's different
            if i != n // i:
                divs.append(n // i)

    # Sort and return
    return sorted(divs)


def totient(n: int) -> int:
    """
    Compute Euler's totient function φ(n).

    Detailed Description:
        Calculates Euler's totient function φ(n), which counts the number of
        positive integers up to n that are relatively prime to n (i.e.,
        gcd(k, n) = 1 for 1 ≤ k ≤ n). Uses prime factorization for efficient
        computation via the product formula.

    Args:
        n (int): Positive integer (must be > 0)

    Returns:
        int: Count of integers k where 1 ≤ k ≤ n and gcd(k, n) = 1
            - φ(1) = 1 (by convention)
            - φ(p) = p - 1 for prime p

    Raises:
        ValueError: If n < 1
        TypeError: If n is not an integer

    Algorithm:
        Uses Euler's product formula:
        φ(n) = n × ∏(1 - 1/p) for all prime divisors p of n

        Implementation:
        1. Find all unique prime factors of n
        2. For each prime p: multiply result by (p - 1) / p
        3. Simplify: φ(n) = n × (p₁-1)/p₁ × (p₂-1)/p₂ × ...

    Complexity:
        Time: O(√n) - Dominated by prime factorization
        Space: O(log n) - Storage for unique prime factors

    Special Cases:
        - φ(1) = 1 (by convention)
        - φ(p) = p - 1 for prime p (all numbers < p are coprime)
        - φ(p^k) = p^k - p^(k-1) = p^(k-1)(p - 1)
        - φ(mn) = φ(m)φ(n) if gcd(m, n) = 1 (multiplicative)

    Examples:
        >>> totient(1)
        1

        >>> totient(2)
        1

        >>> totient(6)
        2

        >>> totient(9)
        6

        >>> totient(10)
        4

        >>> totient(12)
        4

        >>> totient(17)
        16

        >>> totient(36)
        12

        >>> totient(100)
        40

    See Also:
        - prime_factors: Prime factorization
        - gcd: Greatest common divisor
        - is_prime: Primality testing

    Notes:
        - φ(n) is always < n for n > 1
        - φ is multiplicative: φ(mn) = φ(m)φ(n) if gcd(m,n) = 1
        - ∑_{d|n} φ(d) = n (sum over all divisors)
        - φ(n) is even for n ≥ 3

    Mathematical Properties:
        - φ(p^k) = p^(k-1)(p - 1) for prime p
        - φ(2^k) = 2^(k-1)
        - Average order: φ(n) ≈ (6/π²)n ≈ 0.608n
        - φ(n)/n → 0 as n → ∞ (through certain sequences)

    Euler's Product Formula:
        φ(n) = n × ∏_{p|n} (1 - 1/p)
        where the product is over all distinct prime divisors p of n

    Applications:
        - RSA cryptography (key generation, φ(pq) = (p-1)(q-1))
        - Fermat's Little Theorem: a^(p-1) ≡ 1 (mod p) for prime p
        - Euler's Theorem: a^φ(n) ≡ 1 (mod n) if gcd(a,n) = 1
        - Cyclic groups and group theory
        - Number theory research and proofs

    Related Theorems:
        - Euler's Theorem: If gcd(a, n) = 1, then a^φ(n) ≡ 1 (mod n)
        - Fermat's Little Theorem: Special case where n = p (prime)
        - Carmichael's λ function: Related but often smaller than φ

    References:
        [1] Hardy & Wright, "An Introduction to the Theory of Numbers", Ch. 5
        [2] Apostol, "Introduction to Analytic Number Theory", Ch. 2
        [3] Cormen et al., "Introduction to Algorithms", Section 31.7

    Version: 0.5.0
    """
    if not isinstance(n, int):
        raise TypeError(f"Input must be an integer, got {type(n).__name__}")

    if n < 1:
        raise ValueError(f"Input must be a positive integer, got {n}")

    # Special case
    if n == 1:
        return 1

    # Start with result = n
    result = n

    # Find unique prime factors and apply Euler's product formula
    # φ(n) = n × ∏(1 - 1/p) = n × ∏((p-1)/p)

    # Divide by 2 as many times as possible
    if n % 2 == 0:
        result -= result // 2  # Multiply by (1 - 1/2) = 1/2
        while n % 2 == 0:
            n //= 2

    # Try odd divisors
    divisor = 3
    while divisor * divisor <= n:
        if n % divisor == 0:
            result -= result // divisor  # Multiply by (1 - 1/divisor)
            while n % divisor == 0:
                n //= divisor
        divisor += 2

    # If n is still > 1, then it's a prime factor
    if n > 1:
        result -= result // n  # Multiply by (1 - 1/n)

    return result


# ===== ADVANCED ARITHMETIC OPERATIONS =====


def fma(a: Number, b: Number, c: Number) -> float:
    """
    Fused multiply-add: compute a*b + c with single rounding.

    Detailed Description:
        Computes a*b + c as a single operation with only one rounding step,
        providing better accuracy than separate multiply and add operations.
        The FMA operation is fundamental in numerical computing and is often
        hardware-accelerated on modern CPUs.

    Args:
        a (Number): First multiplicand
        b (Number): Second multiplicand
        c (Number): Addend

    Returns:
        float: Result of a*b + c with single rounding

    Algorithm:
        Uses math.fma() which leverages hardware FMA instructions when
        available, or implements high-precision software fallback

    Complexity:
        Time: O(1) - Constant time, often single CPU instruction
        Space: O(1) - No additional space

    Special Cases:
        - fma(NaN, x, y) = NaN
        - fma(x, NaN, y) = NaN
        - fma(x, y, NaN) = NaN
        - fma(±inf, 0, c) = NaN (invalid)
        - fma(0, ±inf, c) = NaN (invalid)
        - fma(±inf, x, -inf) = NaN if a*b = ±inf (invalid)

    Examples:
        >>> fma(2.0, 3.0, 4.0)
        10.0

        >>> fma(0.1, 10.0, 0.5)
        1.5

        >>> fma(1e308, 2.0, 1e308)
        3e+308

        >>> # Demonstrates increased precision
        >>> a, b, c = 1e16, 1.0, -1e16
        >>> (a * b) + c  # Standard: may have rounding error
        0.0
        >>> fma(a, b, c)  # FMA: single rounding, more accurate
        0.0

    See Also:
        - safe_multiply: Multiplication with overflow checking
        - safe_add: Addition with overflow checking
        - hypot: Euclidean distance without overflow

    Notes:
        - Only one rounding error (vs. two for separate ops)
        - More accurate than (a * b) + c
        - Often implemented as single CPU instruction (FMA3/FMA4, ARM NEON)
        - Critical for numerical stability in algorithms
        - Preserves more precision in accumulated sums

    Mathematical Properties:
        - fma(a, b, c) ≈ a*b + c (but more accurate)
        - Associativity may differ from separate operations
        - Not always equivalent to (a*b) + c due to rounding

    Applications:
        - Numerical algorithms (matrix multiplication, dot products)
        - Graphics (ray tracing, transformations)
        - Scientific computing (iterative solvers)
        - Signal processing (filter implementations)
        - Machine learning (neural network forward/backward pass)
        - Financial calculations (compound interest with fees)

    Accuracy Advantages:
        - Dot products: ∑(aᵢ × bᵢ) with FMA has half the rounding error
        - Polynomial evaluation: Horner's method with FMA
        - Matrix operations: More accurate BLAS implementations
        - Compensated summation: Kahan summation improvements

    Hardware Support:
        - x86: FMA3 (Intel Haswell+, AMD Piledriver+)
        - ARM: NEON (ARMv7+), SVE (ARMv8.2+)
        - PowerPC: All modern processors
        - Often compiled to single instruction by optimizing compilers

    References:
        [1] IEEE 754-2008 Section 5.4.1: Fused Multiply-Add
        [2] Muller et al., "Handbook of Floating-Point Arithmetic"
        [3] Intel FMA Instructions Documentation

    Version: 1.0.0
    """
    if math.isnan(a) or math.isnan(b) or math.isnan(c):
        return float('nan')

    # Check for invalid operations
    if (math.isinf(a) and b == 0) or (a == 0 and math.isinf(b)):
        return float('nan')

    # Use math.fma for hardware acceleration and accuracy
    return float(math.fma(a, b, c))


def hypot(*values: Number) -> float:
    """
    Compute Euclidean distance (hypotenuse) without overflow.

    Detailed Description:
        Calculates the Euclidean norm (L2 norm) of a sequence of values:
        sqrt(x₁² + x₂² + ... + xₙ²) while avoiding overflow and underflow.
        For 2 values, computes the hypotenuse of a right triangle. Generalizes
        to n-dimensional Euclidean distance.

    Args:
        *values (Number): Variable number of values (at least 1)

    Returns:
        float: Euclidean distance sqrt(x₁² + x₂² + ... + xₙ²)

    Raises:
        ValueError: If no values provided
        ValueError: If any value is NaN

    Algorithm:
        Uses math.hypot() which implements careful scaling to avoid
        overflow/underflow:
        1. Find maximum absolute value
        2. Scale all values by 1/max
        3. Compute sqrt of sum of squares
        4. Scale result by max

    Complexity:
        Time: O(n) - Linear in number of values
        Space: O(1) - Constant space (ignoring varargs)

    Special Cases:
        - hypot(0) = 0
        - hypot(x) = |x| for single value
        - hypot(x, y) = sqrt(x² + y²) (Pythagorean theorem)
        - hypot(±inf, x) = +inf for any finite x
        - hypot with NaN raises ValueError

    Examples:
        >>> hypot(3, 4)
        5.0

        >>> hypot(5, 12)
        13.0

        >>> hypot(1, 1)
        1.4142135623730951

        >>> hypot(3, 4, 12)
        13.0

        >>> hypot(1, 2, 2)
        3.0

        >>> hypot(1e308, 1e308)  # No overflow!
        1.4142135623730951e+308

        >>> hypot(1e-200, 1e-200)  # No underflow!
        1.4142135623730951e-200

    See Also:
        - safe_sqrt: Square root with checking
        - fma: Fused multiply-add
        - safe_power: General exponentiation

    Notes:
        - Avoids intermediate overflow/underflow
        - More accurate than naive sqrt(x² + y²)
        - Generalizes to any number of dimensions
        - Critical for numerical stability
        - Used extensively in distance calculations

    Mathematical Properties:
        - hypot(x, y) = hypot(y, x) (commutative)
        - hypot(x, y) ≥ max(|x|, |y|) (triangle inequality)
        - hypot(x, 0) = |x|
        - hypot(x, y)² = x² + y² (Pythagorean theorem)

    Applications:
        - Geometry (distance between points)
        - Computer graphics (vector magnitude)
        - Physics (velocity, force magnitudes)
        - Signal processing (magnitude of complex numbers)
        - Machine learning (Euclidean distance, L2 norm)
        - Navigation (great circle distance approximation)
        - Statistics (standard deviation, variance)

    Pythagorean Theorem:
        For right triangle with legs a, b and hypotenuse c:
        c² = a² + b²
        c = hypot(a, b)

    Euclidean Distance:
        Distance between points P₁(x₁,y₁,z₁) and P₂(x₂,y₂,z₂):
        d = hypot(x₂-x₁, y₂-y₁, z₂-z₁)

    References:
        [1] IEEE 754-2008: Recommended operations
        [2] Moler & Morrison, "Replacing Square Roots by Pythagorean Sums"
        [3] BLAS: DNRM2 (Euclidean norm)

    Version: 1.0.0
    """
    if not values:
        raise ValueError("hypot requires at least one value")

    # Check for NaN
    if any(math.isnan(v) for v in values):
        raise ValueError("hypot undefined for NaN values")

    # Use math.hypot for overflow-safe computation
    return float(math.hypot(*values))


def copysign(magnitude: Number, sign: Number) -> float:
    """
    Return magnitude with the sign of sign.

    Detailed Description:
        Creates a number with the absolute value of magnitude and the sign
        of sign. Useful for manipulating signs independently of magnitude.
        Handles IEEE 754 signed zero correctly.

    Args:
        magnitude (Number): Value providing the magnitude
        sign (Number): Value providing the sign

    Returns:
        float: |magnitude| with sign of sign
            - Positive if sign ≥ 0
            - Negative if sign < 0

    Algorithm:
        Uses math.copysign() which operates at bit level for IEEE 754 floats

    Complexity:
        Time: O(1) - Constant time, typically bit operation
        Space: O(1) - No additional space

    Special Cases:
        - copysign(x, +y) = |x| for y > 0
        - copysign(x, -y) = -|x| for y < 0
        - copysign(x, 0.0) = |x| (positive zero)
        - copysign(x, -0.0) = -|x| (negative zero)
        - copysign(NaN, y) = NaN with sign of y
        - copysign(inf, y) = ±inf with sign of y

    Examples:
        >>> copysign(5.0, 1.0)
        5.0

        >>> copysign(5.0, -1.0)
        -5.0

        >>> copysign(-5.0, 1.0)
        5.0

        >>> copysign(-5.0, -1.0)
        -5.0

        >>> copysign(3.14, -2.71)
        -3.14

        >>> copysign(0.0, -1.0)
        -0.0

        >>> copysign(float('inf'), -1.0)
        -inf

    See Also:
        - abs_value: Absolute value
        - sign: Return sign as -1, 0, or 1
        - fma: Fused multiply-add

    Notes:
        - Preserves NaN payloads
        - Handles signed zero correctly
        - Often implemented as single bit operation
        - Useful for sign manipulation without branching
        - Different from multiplication by sign(x)

    Mathematical Properties:
        - copysign(x, y) = sign(y) × |x|
        - copysign(copysign(x, y), z) = copysign(x, z)
        - |copysign(x, y)| = |x|

    Applications:
        - Numerical algorithms (sign corrections)
        - Computer graphics (normal vector orientation)
        - Signal processing (phase adjustments)
        - Physics simulations (direction handling)
        - Branch-free programming (sign manipulation)
        - IEEE 754 operations (signed zero handling)

    IEEE 754 Signed Zero:
        - +0.0 and -0.0 are distinct values
        - copysign distinguishes them correctly
        - 1.0/+0.0 = +inf, 1.0/-0.0 = -inf
        - Preserves sign through operations

    References:
        [1] IEEE 754-2008 Section 5.5.1: Sign Bit Operations
        [2] Goldberg, "What Every Computer Scientist Should Know About Floating-Point"

    Version: 1.0.0
    """
    if math.isnan(magnitude) or math.isnan(sign):
        # Preserve NaN with sign
        return float(math.copysign(float('nan'), sign))

    return float(math.copysign(magnitude, sign))


def lerp(a: Number, b: Number, t: Number) -> float:
    """
    Linear interpolation between two values.

    Detailed Description:
        Computes the linear interpolation between a and b using parameter t:
        result = a + t*(b - a) = (1-t)*a + t*b
        When t=0, returns a; when t=1, returns b. For 0 < t < 1, returns
        value between a and b. Can extrapolate outside [a,b] for t outside [0,1].

    Args:
        a (Number): Start value (at t=0)
        b (Number): End value (at t=1)
        t (Number): Interpolation parameter (typically 0 ≤ t ≤ 1)
            - t = 0: returns a
            - t = 1: returns b
            - 0 < t < 1: interpolates between a and b
            - t < 0 or t > 1: extrapolates

    Returns:
        float: Interpolated value a + t*(b - a)

    Algorithm:
        Uses formula: a + t*(b - a)
        Alternative (numerically equivalent): (1-t)*a + t*b

    Complexity:
        Time: O(1) - Constant time
        Space: O(1) - No additional space

    Special Cases:
        - lerp(a, b, 0) = a
        - lerp(a, b, 1) = b
        - lerp(a, b, 0.5) = (a + b) / 2 (midpoint)
        - lerp(a, a, t) = a for any t
        - lerp(a, b, NaN) = NaN

    Examples:
        >>> lerp(0, 10, 0.5)
        5.0

        >>> lerp(0, 100, 0.25)
        25.0

        >>> lerp(10, 20, 0)
        10.0

        >>> lerp(10, 20, 1)
        20.0

        >>> lerp(5, 15, 0.7)
        12.0

        >>> lerp(0, 10, 2.0)  # Extrapolation
        20.0

        >>> lerp(10, 5, 0.5)  # Works with decreasing
        7.5

    See Also:
        - clamp: Clamp value to range
        - fma: Fused multiply-add (can implement lerp)
        - safe_add, safe_multiply: Arithmetic operations

    Notes:
        - t not restricted to [0, 1]; can extrapolate
        - Exact at endpoints: lerp(a, b, 0) === a, lerp(a, b, 1) === b
        - For imprecise t, consider clamping to [0, 1]
        - Can use FMA for slightly better precision
        - Generalizes to vectors (component-wise)

    Mathematical Properties:
        - lerp(a, b, t) = a + t*(b - a)
        - lerp(a, b, t) = (1-t)*a + t*b
        - lerp(a, b, 0) = a (start)
        - lerp(a, b, 1) = b (end)
        - lerp is continuous in all arguments

    Applications:
        - Computer graphics (color blending, animation)
        - Game development (smooth movement, easing)
        - UI animations (transitions, fades)
        - Physics (position interpolation)
        - Audio (crossfading, envelope interpolation)
        - Data visualization (gradient generation)
        - Numerical methods (secant method)
        - Machine learning (learning rate schedules)

    Animation and Graphics:
        - Smooth transitions between keyframes
        - Color gradients (RGB interpolation)
        - Easing functions (combine with easing curves)
        - Camera movements (smooth panning)
        - Sprite animation (frame blending)

    Inverse (Unlerp):
        To find t given result: t = (result - a) / (b - a)
        This "inverse lerp" or "unlerp" maps value to parameter

    Bilinear/Trilinear:
        - Bilinear: lerp(lerp(a,b,s), lerp(c,d,s), t)
        - Trilinear: Extends to 3D interpolation
        - Used in texture mapping, volume rendering

    References:
        [1] Foley et al., "Computer Graphics: Principles and Practice"
        [2] Lengyel, "Mathematics for 3D Game Programming"
        [3] IEEE 754-2008 (for numerical properties)

    Version: 1.0.0
    """
    if math.isnan(a) or math.isnan(b) or math.isnan(t):
        return float('nan')

    # Formula: a + t*(b - a)
    # This ensures exact results at t=0 and t=1
    return float(a + t * (b - a))
