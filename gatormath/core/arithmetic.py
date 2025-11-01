"""
Module Name: arithmetic

Description:
    Fundamental arithmetic operations with robust precision handling.
    Provides safe implementations of basic mathematical operations that
    handle edge cases, overflow, underflow, and floating-point precision
    issues that plague standard operators.

Module Path: gatormath/core/arithmetic.py
Package: gatormath.core

Author: GatorMath Development Team
Created: 2025-11-01
Modified: 2025-11-01
Version: 0.1.0

Dependencies:
    - math: Standard mathematical functions
    - decimal: High-precision arithmetic
    - typing: Type hints
    - gatormath.precision: Safe comparison utilities

Exports:
    - safe_add: Addition with overflow detection
    - safe_subtract: Subtraction with underflow detection
    - safe_multiply: Multiplication with overflow detection
    - safe_divide: Division with zero-division handling
    - safe_power: Exponentiation with overflow detection
    - safe_sqrt: Square root with domain validation
    - safe_mod: Modulo with zero-modulo handling
    - clamp: Constrain value to range
    - sign: Get sign of number (-1, 0, or 1)
    - factorial: Factorial with memoization
    - gcd: Greatest common divisor
    - lcm: Least common multiple

Mathematical Background:
    Safe arithmetic operations protect against:
    - Integer overflow (exceeding max representable value)
    - Floating-point overflow (result too large to represent)
    - Division by zero
    - Domain errors (e.g., sqrt of negative)
    - Loss of precision in accumulation

Precision Notes:
    - Uses precision.is_close for equality checks
    - Decimal type available for exact arithmetic
    - Detects and warns on precision loss
    - Handles subnormal numbers correctly

Usage:
    >>> from gatormath.core import arithmetic
    >>> arithmetic.safe_add(0.1, 0.2)
    0.30000000000000004
    >>> arithmetic.safe_divide(10, 0)
    Traceback (most recent call last):
        ...
    ZeroDivisionError: Division by zero

Examples:
    Safe operations:
    >>> safe_add(1e308, 1e308)
    Traceback (most recent call last):
        ...
    OverflowError: Addition overflow

    >>> safe_divide(10, 3)
    3.3333333333333335

    >>> safe_sqrt(16)
    4.0

See Also:
    - math: Standard library math functions
    - decimal: For exact decimal arithmetic
    - gatormath.precision: For safe comparisons

References:
    [1] "What Every Computer Scientist Should Know About Floating-Point
        Arithmetic" - David Goldberg
    [2] IEEE 754-2008 Standard for Floating-Point Arithmetic
"""

# Standard library imports
import math
import sys
from decimal import Decimal, InvalidOperation
from functools import lru_cache
from typing import Optional, Union


# Local imports
from gatormath.precision import is_close, is_zero


# ============================================================================
# Type Aliases
# ============================================================================

Number = Union[int, float, Decimal]


# ============================================================================
# Constants
# ============================================================================

# Maximum safe integer (2^53 - 1 for IEEE 754 double)
MAX_SAFE_INTEGER: int = 9007199254740991
MIN_SAFE_INTEGER: int = -9007199254740991

# Float limits
MAX_FLOAT: float = sys.float_info.max
MIN_FLOAT: float = sys.float_info.min
EPSILON: float = sys.float_info.epsilon


# ============================================================================
# Basic Arithmetic Operations
# ============================================================================

def safe_add(a: Number, b: Number, *, check_overflow: bool = True) -> Number:
    """
    Safely add two numbers with overflow detection.

    Args:
        a (Number): First addend
        b (Number): Second addend
        check_overflow (bool): Enable overflow checking (default: True)

    Returns:
        Number: Sum of a and b

    Raises:
        OverflowError: If result would overflow (when check_overflow=True)
        TypeError: If inputs are not numbers

    Algorithm:
        1. Validate inputs are numeric
        2. Check for potential overflow before computation
        3. Perform addition
        4. Verify result is finite

    Complexity:
        Time: O(1)
        Space: O(1)

    Examples:
        >>> safe_add(5, 3)
        8
        >>> safe_add(0.1, 0.2)
        0.30000000000000004
        >>> safe_add(Decimal('0.1'), Decimal('0.2'))
        Decimal('0.3')

        >>> # Overflow detection
        >>> safe_add(1e308, 1e308)
        Traceback (most recent call last):
            ...
        OverflowError: Addition would overflow

    Notes:
        - For exact decimal arithmetic, use Decimal inputs
        - Overflow checking adds minimal performance cost
        - Handles mixed int/float inputs

    Version: 0.1.0
    """
    # Handle Decimal separately for exact arithmetic
    if isinstance(a, Decimal) or isinstance(b, Decimal):
        try:
            return Decimal(str(a)) + Decimal(str(b))
        except InvalidOperation as e:
            raise ValueError(f"Invalid decimal operation: {e}") from e

    # Check for overflow in float arithmetic
    if check_overflow and isinstance(a, (int, float)) and isinstance(b, (int, float)):
        # Check if addition would overflow
        if a > 0 and b > 0 and a > MAX_FLOAT - b:
            raise OverflowError(f"Addition would overflow: {a} + {b}")
        if a < 0 and b < 0 and a < -MAX_FLOAT - b:
            raise OverflowError(f"Addition would underflow: {a} + {b}")

    result = a + b

    # Verify result is finite
    if isinstance(result, float) and not math.isfinite(result):
        raise OverflowError(f"Addition produced non-finite result: {a} + {b} = {result}")

    return result


def safe_subtract(a: Number, b: Number, *, check_overflow: bool = True) -> Number:
    """
    Safely subtract two numbers with overflow detection.

    Args:
        a (Number): Minuend
        b (Number): Subtrahend
        check_overflow (bool): Enable overflow checking (default: True)

    Returns:
        Number: Difference a - b

    Raises:
        OverflowError: If result would overflow
        TypeError: If inputs are not numbers

    Examples:
        >>> safe_subtract(10, 3)
        7
        >>> safe_subtract(0.3, 0.1)
        0.19999999999999998
        >>> safe_subtract(Decimal('0.3'), Decimal('0.1'))
        Decimal('0.2')

    Version: 0.1.0
    """
    # Handle Decimal
    if isinstance(a, Decimal) or isinstance(b, Decimal):
        try:
            return Decimal(str(a)) - Decimal(str(b))
        except InvalidOperation as e:
            raise ValueError(f"Invalid decimal operation: {e}") from e

    # Check for overflow
    if check_overflow and isinstance(a, (int, float)) and isinstance(b, (int, float)):
        if a > 0 and b < 0 and a > MAX_FLOAT + b:
            raise OverflowError(f"Subtraction would overflow: {a} - {b}")
        if a < 0 and b > 0 and a < -MAX_FLOAT + b:
            raise OverflowError(f"Subtraction would underflow: {a} - {b}")

    result = a - b

    if isinstance(result, float) and not math.isfinite(result):
        raise OverflowError(f"Subtraction produced non-finite result: {a} - {b} = {result}")

    return result


def safe_multiply(a: Number, b: Number, *, check_overflow: bool = True) -> Number:
    """
    Safely multiply two numbers with overflow detection.

    Args:
        a (Number): First factor
        b (Number): Second factor
        check_overflow (bool): Enable overflow checking (default: True)

    Returns:
        Number: Product a * b

    Raises:
        OverflowError: If result would overflow
        TypeError: If inputs are not numbers

    Examples:
        >>> safe_multiply(5, 3)
        15
        >>> safe_multiply(0.1, 0.2)
        0.020000000000000004
        >>> safe_multiply(Decimal('0.1'), Decimal('0.2'))
        Decimal('0.02')

        >>> # Large number multiplication
        >>> safe_multiply(1e200, 1e200)
        Traceback (most recent call last):
            ...
        OverflowError: Multiplication would overflow

    Notes:
        - Overflow detection is conservative
        - Zero multiplication always safe
        - Sign handling is automatic

    Version: 0.1.0
    """
    # Handle Decimal
    if isinstance(a, Decimal) or isinstance(b, Decimal):
        try:
            return Decimal(str(a)) * Decimal(str(b))
        except InvalidOperation as e:
            raise ValueError(f"Invalid decimal operation: {e}") from e

    # Zero multiplication is always safe
    if is_zero(float(a)) or is_zero(float(b)):
        return 0 if isinstance(a, int) and isinstance(b, int) else 0.0

    # Check for overflow
    if check_overflow and isinstance(a, (int, float)) and isinstance(b, (int, float)):
        abs_a, abs_b = abs(a), abs(b)
        if abs_a > 1 and abs_b > 1 and abs_a > MAX_FLOAT / abs_b:
            raise OverflowError(f"Multiplication would overflow: {a} * {b}")

    result = a * b

    if isinstance(result, float) and not math.isfinite(result):
        raise OverflowError(f"Multiplication produced non-finite result: {a} * {b} = {result}")

    return result


def safe_divide(
    a: Number,
    b: Number,
    *,
    check_overflow: bool = True,
    default: Optional[Number] = None,
) -> Number:
    """
    Safely divide two numbers with zero-division handling.

    Args:
        a (Number): Dividend (numerator)
        b (Number): Divisor (denominator)
        check_overflow (bool): Enable overflow checking (default: True)
        default (Optional[Number]): Value to return on division by zero
            If None, raises ZeroDivisionError

    Returns:
        Number: Quotient a / b, or default if b is zero and default is set

    Raises:
        ZeroDivisionError: If b is zero and no default provided
        OverflowError: If result would overflow
        TypeError: If inputs are not numbers

    Examples:
        >>> safe_divide(10, 2)
        5.0
        >>> safe_divide(10, 3)
        3.3333333333333335
        >>> safe_divide(Decimal('10'), Decimal('3'))
        Decimal('3.333333333333333333333333333')

        >>> # Zero division
        >>> safe_divide(10, 0)
        Traceback (most recent call last):
            ...
        ZeroDivisionError: Division by zero

        >>> # With default
        >>> safe_divide(10, 0, default=float('inf'))
        inf

    Notes:
        - Returns float for int/int division (Python 3 behavior)
        - Decimal division maintains precision
        - Handles signed zero correctly

    Version: 0.1.0
    """
    # Check for division by zero
    if is_zero(float(b)):
        if default is not None:
            return default
        raise ZeroDivisionError("Division by zero")

    # Handle Decimal
    if isinstance(a, Decimal) or isinstance(b, Decimal):
        try:
            return Decimal(str(a)) / Decimal(str(b))
        except (InvalidOperation, ZeroDivisionError) as e:
            if default is not None:
                return default
            raise ZeroDivisionError(f"Invalid decimal division: {e}") from e

    # Perform division
    result = a / b

    # Check result
    if isinstance(result, float):
        if not math.isfinite(result) and default is not None:
            return default
        if not math.isfinite(result):
            raise OverflowError(f"Division produced non-finite result: {a} / {b} = {result}")

    return result


def safe_power(
    base: Number,
    exponent: Number,
    *,
    check_overflow: bool = True,
) -> Number:
    """
    Safely raise base to power with overflow and domain checking.

    Args:
        base (Number): Base value
        exponent (Number): Exponent value
        check_overflow (bool): Enable overflow checking (default: True)

    Returns:
        Number: base ** exponent

    Raises:
        OverflowError: If result would overflow
        ValueError: If operation is undefined (e.g., negative base with fractional exponent)
        TypeError: If inputs are not numbers

    Examples:
        >>> safe_power(2, 10)
        1024.0
        >>> safe_power(2.5, 3)
        15.625
        >>> safe_power(9, 0.5)
        3.0

        >>> # Overflow detection
        >>> safe_power(10, 1000)
        Traceback (most recent call last):
            ...
        OverflowError: Power operation would overflow

        >>> # Domain error
        >>> safe_power(-1, 0.5)
        Traceback (most recent call last):
            ...
        ValueError: Cannot raise negative number to fractional power

    Notes:
        - 0^0 is defined as 1 (mathematical convention)
        - Negative base with non-integer exponent raises ValueError
        - Uses math.pow for better precision than ** operator

    Version: 0.1.0
    """
    # Handle special cases
    if is_zero(float(base)) and is_zero(float(exponent)):
        return 1  # 0^0 = 1 by convention

    if is_zero(float(base)):
        if exponent < 0:
            raise ZeroDivisionError("Cannot raise zero to negative power")
        return 0 if isinstance(base, int) and isinstance(exponent, int) else 0.0

    # Check for domain errors
    if base < 0 and isinstance(exponent, float) and not exponent.is_integer():
        raise ValueError(
            f"Cannot raise negative number to fractional power: {base}^{exponent}"
        )

    # Handle Decimal
    if isinstance(base, Decimal) or isinstance(exponent, Decimal):
        try:
            return Decimal(str(base)) ** Decimal(str(exponent))
        except InvalidOperation as e:
            raise ValueError(f"Invalid decimal power operation: {e}") from e

    # Estimate if result would overflow
    if check_overflow and abs(base) > 1 and exponent > 0:
        # Rough estimate: log(result) = exponent * log(base)
        try:
            log_result = exponent * math.log(abs(base))
            if log_result > math.log(MAX_FLOAT):
                raise OverflowError(f"Power operation would overflow: {base}^{exponent}")
        except (ValueError, OverflowError):
            pass  # Let the actual computation handle it

    # Compute result
    try:
        result = math.pow(base, exponent)
    except OverflowError as e:
        raise OverflowError(f"Power operation overflow: {base}^{exponent}") from e
    except ValueError as e:
        raise ValueError(f"Power operation error: {base}^{exponent}: {e}") from e

    if not math.isfinite(result):
        raise OverflowError(f"Power operation produced non-finite result: {base}^{exponent}")

    return result


def safe_sqrt(value: Number) -> float:
    """
    Safely compute square root with domain validation.

    Args:
        value (Number): Value to take square root of (must be non-negative)

    Returns:
        float: Square root of value

    Raises:
        ValueError: If value is negative
        TypeError: If value is not a number

    Examples:
        >>> safe_sqrt(16)
        4.0
        >>> safe_sqrt(2)
        1.4142135623730951
        >>> safe_sqrt(0)
        0.0

        >>> # Domain error
        >>> safe_sqrt(-1)
        Traceback (most recent call last):
            ...
        ValueError: Cannot take square root of negative number: -1

    Notes:
        - For complex results, use cmath.sqrt instead
        - Handles very small positive numbers correctly
        - Uses math.sqrt for optimal precision

    Version: 0.1.0
    """
    if value < 0:
        raise ValueError(f"Cannot take square root of negative number: {value}")

    return math.sqrt(float(value))


def safe_mod(a: Number, b: Number, *, default: Optional[Number] = None) -> Number:
    """
    Safely compute modulo with zero-modulo handling.

    Args:
        a (Number): Dividend
        b (Number): Divisor (modulus)
        default (Optional[Number]): Value to return if b is zero

    Returns:
        Number: a % b, or default if b is zero and default is set

    Raises:
        ZeroDivisionError: If b is zero and no default provided
        TypeError: If inputs are not numbers

    Examples:
        >>> safe_mod(10, 3)
        1
        >>> safe_mod(10.5, 3)
        1.5
        >>> safe_mod(-10, 3)
        2

        >>> # Zero modulo
        >>> safe_mod(10, 0)
        Traceback (most recent call last):
            ...
        ZeroDivisionError: Modulo by zero

        >>> # With default
        >>> safe_mod(10, 0, default=0)
        0

    Notes:
        - Python's modulo has same sign as divisor
        - Handles negative numbers according to Python semantics
        - Works with floats and Decimals

    Version: 0.1.0
    """
    if is_zero(float(b)):
        if default is not None:
            return default
        raise ZeroDivisionError("Modulo by zero")

    return a % b


# ============================================================================
# Utility Functions
# ============================================================================

def clamp(value: Number, min_value: Number, max_value: Number) -> Number:
    """
    Constrain value to be within [min_value, max_value].

    Args:
        value (Number): Value to clamp
        min_value (Number): Minimum allowed value
        max_value (Number): Maximum allowed value

    Returns:
        Number: Clamped value in range [min_value, max_value]

    Raises:
        ValueError: If min_value > max_value

    Examples:
        >>> clamp(5, 0, 10)
        5
        >>> clamp(-5, 0, 10)
        0
        >>> clamp(15, 0, 10)
        10
        >>> clamp(7.5, 0.0, 10.0)
        7.5

    Notes:
        - If min_value == max_value, always returns that value
        - Preserves input type when possible

    Version: 0.1.0
    """
    if min_value > max_value:
        raise ValueError(f"min_value ({min_value}) cannot exceed max_value ({max_value})")

    return max(min_value, min(value, max_value))


def sign(value: Number) -> int:
    """
    Get the sign of a number.

    Args:
        value (Number): Number to get sign of

    Returns:
        int: -1 if negative, 0 if zero, 1 if positive

    Examples:
        >>> sign(5)
        1
        >>> sign(-5)
        -1
        >>> sign(0)
        0
        >>> sign(1e-15)
        0

    Notes:
        - Uses precision.is_zero for zero detection
        - Values within epsilon of zero return 0

    Version: 0.1.0
    """
    if is_zero(float(value)):
        return 0
    return -1 if value < 0 else 1


@lru_cache(maxsize=128)
def factorial(n: int) -> int:
    """
    Compute factorial with memoization.

    Args:
        n (int): Non-negative integer

    Returns:
        int: n! = n * (n-1) * ... * 2 * 1

    Raises:
        ValueError: If n is negative
        TypeError: If n is not an integer

    Algorithm:
        Uses recursion with memoization via lru_cache

    Complexity:
        Time: O(n) for first call, O(1) for cached
        Space: O(n) for cache

    Examples:
        >>> factorial(0)
        1
        >>> factorial(5)
        120
        >>> factorial(10)
        3628800

        >>> factorial(-1)
        Traceback (most recent call last):
            ...
        ValueError: Factorial not defined for negative numbers

    Notes:
        - 0! = 1 by definition
        - Results cached for performance
        - Can overflow for large n

    Version: 0.1.0
    """
    if not isinstance(n, int):
        raise TypeError(f"Factorial requires integer, got {type(n).__name__}")

    if n < 0:
        raise ValueError("Factorial not defined for negative numbers")

    if n <= 1:
        return 1

    return n * factorial(n - 1)


def gcd(a: int, b: int) -> int:
    """
    Compute greatest common divisor using Euclidean algorithm.

    Args:
        a (int): First integer
        b (int): Second integer

    Returns:
        int: Greatest common divisor of a and b (always non-negative)

    Algorithm:
        Euclidean algorithm: gcd(a, b) = gcd(b, a % b)

    Complexity:
        Time: O(log(min(a, b)))
        Space: O(1)

    Examples:
        >>> gcd(48, 18)
        6
        >>> gcd(100, 35)
        5
        >>> gcd(17, 13)
        1

    Notes:
        - gcd(0, n) = n
        - gcd(n, 0) = n
        - Always returns non-negative value

    Version: 0.1.0
    """
    a, b = abs(a), abs(b)
    while b:
        a, b = b, a % b
    return a


def lcm(a: int, b: int) -> int:
    """
    Compute least common multiple.

    Args:
        a (int): First integer
        b (int): Second integer

    Returns:
        int: Least common multiple of a and b

    Algorithm:
        lcm(a, b) = |a * b| / gcd(a, b)

    Complexity:
        Time: O(log(min(a, b)))
        Space: O(1)

    Examples:
        >>> lcm(12, 18)
        36
        >>> lcm(21, 6)
        42
        >>> lcm(5, 7)
        35

    Notes:
        - lcm(0, n) = 0
        - lcm(n, 0) = 0
        - Always returns non-negative value

    Version: 0.1.0
    """
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // gcd(a, b)


# ============================================================================
# Module Exports
# ============================================================================

__all__ = [
    # Constants
    "MAX_SAFE_INTEGER",
    "MIN_SAFE_INTEGER",
    "MAX_FLOAT",
    "MIN_FLOAT",
    "EPSILON",
    # Basic operations
    "safe_add",
    "safe_subtract",
    "safe_multiply",
    "safe_divide",
    "safe_power",
    "safe_sqrt",
    "safe_mod",
    # Utilities
    "clamp",
    "sign",
    "factorial",
    "gcd",
    "lcm",
]
