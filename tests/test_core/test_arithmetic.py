"""
Test suite for gatormath.core.arithmetic module.

Tests cover:
- Safe arithmetic operations
- Overflow detection
- Division by zero handling
- Edge cases
- Precision handling
"""

import math

import pytest

from gatormath.core import arithmetic


class TestSafeAdd:
    """Tests for safe_add function."""

    def test_basic_addition(self) -> None:
        """Test basic integer addition."""
        assert arithmetic.safe_add(2, 3) == 5
        assert arithmetic.safe_add(-2, 3) == 1
        assert arithmetic.safe_add(-2, -3) == -5

    def test_float_addition(self) -> None:
        """Test floating-point addition."""
        result = arithmetic.safe_add(0.1, 0.2)
        assert abs(result - 0.3) < 1e-10

    def test_overflow_detection(self) -> None:
        """Test overflow detection."""
        with pytest.raises(OverflowError):
            arithmetic.safe_add(1e308, 1e308)


class TestSafeDivide:
    """Tests for safe_divide function."""

    def test_basic_division(self) -> None:
        """Test basic division."""
        assert arithmetic.safe_divide(10, 2) == 5.0
        assert abs(arithmetic.safe_divide(10, 3) - 3.333333) < 1e-5

    def test_zero_division(self) -> None:
        """Test division by zero raises error."""
        with pytest.raises(ZeroDivisionError):
            arithmetic.safe_divide(10, 0)

    def test_zero_division_with_default(self) -> None:
        """Test division by zero with default value."""
        assert arithmetic.safe_divide(10, 0, default=float('inf')) == float('inf')


class TestSafeSqrt:
    """Tests for safe_sqrt function."""

    def test_perfect_squares(self) -> None:
        """Test square roots of perfect squares."""
        assert arithmetic.safe_sqrt(0) == 0
        assert arithmetic.safe_sqrt(1) == 1
        assert arithmetic.safe_sqrt(4) == 2
        assert arithmetic.safe_sqrt(9) == 3
        assert arithmetic.safe_sqrt(144) == 12

    def test_negative_input(self) -> None:
        """Test that negative input raises ValueError."""
        with pytest.raises(ValueError):
            arithmetic.safe_sqrt(-1)


class TestFactorial:
    """Tests for factorial function."""

    def test_small_factorials(self) -> None:
        """Test factorials of small numbers."""
        assert arithmetic.factorial(0) == 1
        assert arithmetic.factorial(1) == 1
        assert arithmetic.factorial(5) == 120
        assert arithmetic.factorial(10) == 3628800

    def test_negative_input(self) -> None:
        """Test that negative input raises ValueError."""
        with pytest.raises(ValueError):
            arithmetic.factorial(-1)


class TestGCDandLCM:
    """Tests for GCD and LCM functions."""

    def test_gcd(self) -> None:
        """Test greatest common divisor."""
        assert arithmetic.gcd(48, 18) == 6
        assert arithmetic.gcd(100, 35) == 5
        assert arithmetic.gcd(17, 13) == 1

    def test_lcm(self) -> None:
        """Test least common multiple."""
        assert arithmetic.lcm(12, 18) == 36
        assert arithmetic.lcm(21, 6) == 42
        assert arithmetic.lcm(5, 7) == 35


class TestClamp:
    """Tests for clamp function."""

    def test_value_in_range(self) -> None:
        """Test clamping value within range."""
        assert arithmetic.clamp(5, 0, 10) == 5

    def test_value_below_range(self) -> None:
        """Test clamping value below range."""
        assert arithmetic.clamp(-5, 0, 10) == 0

    def test_value_above_range(self) -> None:
        """Test clamping value above range."""
        assert arithmetic.clamp(15, 0, 10) == 10


class TestSign:
    """Tests for sign function."""

    def test_positive(self) -> None:
        """Test sign of positive numbers."""
        assert arithmetic.sign(5) == 1
        assert arithmetic.sign(0.1) == 1

    def test_negative(self) -> None:
        """Test sign of negative numbers."""
        assert arithmetic.sign(-5) == -1
        assert arithmetic.sign(-0.1) == -1

    def test_zero(self) -> None:
        """Test sign of zero."""
        assert arithmetic.sign(0) == 0
        assert arithmetic.sign(1e-15) == 0  # Within epsilon
