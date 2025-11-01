"""
Test suite for gatormath.geometry.shapes2d module.

Tests cover:
- Circle calculations
- Rectangle calculations
- Square calculations
- Triangle calculations and validation
- Edge cases
"""

import math

import pytest

from gatormath.geometry import shapes2d


class TestCircle:
    """Tests for Circle class."""

    def test_circle_creation(self) -> None:
        """Test circle creation."""
        circle = shapes2d.Circle(radius=5.0)
        assert circle.radius == 5.0

    def test_invalid_radius(self) -> None:
        """Test that negative radius raises ValueError."""
        with pytest.raises(ValueError):
            shapes2d.Circle(radius=-5.0)

    def test_area(self) -> None:
        """Test circle area calculation."""
        circle = shapes2d.Circle(radius=10.0)
        expected = math.pi * 100
        assert abs(circle.area() - expected) < 1e-10

    def test_circumference(self) -> None:
        """Test circle circumference."""
        circle = shapes2d.Circle(radius=10.0)
        expected = 2 * math.pi * 10
        assert abs(circle.circumference() - expected) < 1e-10

    def test_diameter(self) -> None:
        """Test circle diameter."""
        circle = shapes2d.Circle(radius=5.0)
        assert circle.diameter() == 10.0


class TestRectangle:
    """Tests for Rectangle class."""

    def test_rectangle_creation(self) -> None:
        """Test rectangle creation."""
        rect = shapes2d.Rectangle(width=4.0, height=3.0)
        assert rect.width == 4.0
        assert rect.height == 3.0

    def test_area(self) -> None:
        """Test rectangle area."""
        rect = shapes2d.Rectangle(width=5.0, height=3.0)
        assert rect.area() == 15.0

    def test_perimeter(self) -> None:
        """Test rectangle perimeter."""
        rect = shapes2d.Rectangle(width=5.0, height=3.0)
        assert rect.perimeter() == 16.0

    def test_diagonal(self) -> None:
        """Test rectangle diagonal (3-4-5 triangle)."""
        rect = shapes2d.Rectangle(width=3.0, height=4.0)
        assert rect.diagonal() == 5.0

    def test_is_square(self) -> None:
        """Test square detection."""
        square_rect = shapes2d.Rectangle(width=5.0, height=5.0)
        non_square = shapes2d.Rectangle(width=5.0, height=3.0)
        assert square_rect.is_square()
        assert not non_square.is_square()


class TestSquare:
    """Tests for Square class."""

    def test_square_creation(self) -> None:
        """Test square creation."""
        square = shapes2d.Square(side=5.0)
        assert square.side == 5.0

    def test_area(self) -> None:
        """Test square area."""
        square = shapes2d.Square(side=4.0)
        assert square.area() == 16.0

    def test_perimeter(self) -> None:
        """Test square perimeter."""
        square = shapes2d.Square(side=4.0)
        assert square.perimeter() == 16.0

    def test_diagonal(self) -> None:
        """Test square diagonal."""
        square = shapes2d.Square(side=1.0)
        assert abs(square.diagonal() - math.sqrt(2)) < 1e-10


class TestTriangle:
    """Tests for Triangle class."""

    def test_valid_triangle(self) -> None:
        """Test valid triangle creation."""
        triangle = shapes2d.Triangle(a=3.0, b=4.0, c=5.0)
        assert triangle.a == 3.0
        assert triangle.b == 4.0
        assert triangle.c == 5.0

    def test_invalid_triangle(self) -> None:
        """Test that invalid sides raise ValueError."""
        with pytest.raises(ValueError):
            shapes2d.Triangle(a=1.0, b=2.0, c=10.0)

    def test_right_triangle_area(self) -> None:
        """Test area of 3-4-5 right triangle."""
        triangle = shapes2d.Triangle(a=3.0, b=4.0, c=5.0)
        assert triangle.area() == 6.0

    def test_perimeter(self) -> None:
        """Test triangle perimeter."""
        triangle = shapes2d.Triangle(a=3.0, b=4.0, c=5.0)
        assert triangle.perimeter() == 12.0

    def test_is_right_triangle(self) -> None:
        """Test right triangle detection."""
        right_triangle = shapes2d.Triangle(a=3.0, b=4.0, c=5.0)
        not_right = shapes2d.Triangle(a=3.0, b=3.0, c=3.0)
        assert right_triangle.is_right_triangle()
        assert not not_right.is_right_triangle()

    def test_is_equilateral(self) -> None:
        """Test equilateral triangle detection."""
        equilateral = shapes2d.Triangle(a=5.0, b=5.0, c=5.0)
        not_equilateral = shapes2d.Triangle(a=3.0, b=4.0, c=5.0)
        assert equilateral.is_equilateral()
        assert not not_equilateral.is_equilateral()

    def test_is_isosceles(self) -> None:
        """Test isosceles triangle detection."""
        isosceles = shapes2d.Triangle(a=5.0, b=5.0, c=3.0)
        scalene = shapes2d.Triangle(a=3.0, b=4.0, c=5.0)
        assert isosceles.is_isosceles()
        assert not scalene.is_isosceles()

    def test_triangle_type(self) -> None:
        """Test triangle type classification."""
        equilateral = shapes2d.Triangle(a=5.0, b=5.0, c=5.0)
        isosceles = shapes2d.Triangle(a=5.0, b=5.0, c=3.0)
        scalene = shapes2d.Triangle(a=3.0, b=4.0, c=5.0)

        assert equilateral.triangle_type() == "equilateral"
        assert isosceles.triangle_type() == "isosceles"
        assert scalene.triangle_type() == "scalene"


class TestPoint:
    """Tests for Point class."""

    def test_point_creation(self) -> None:
        """Test point creation."""
        p = shapes2d.Point(3.0, 4.0)
        assert p.x == 3.0
        assert p.y == 4.0

    def test_distance(self) -> None:
        """Test distance calculation between points."""
        p1 = shapes2d.Point(0.0, 0.0)
        p2 = shapes2d.Point(3.0, 4.0)
        assert p1.distance_to(p2) == 5.0
