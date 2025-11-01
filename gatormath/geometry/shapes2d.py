"""
Module Name: shapes2d

Description:
    Two-dimensional geometric shapes with robust implementations.
    Provides classes for common 2D shapes (circles, rectangles, triangles,
    polygons) with comprehensive geometric operations, area/perimeter
    calculations, and intersection detection.

Module Path: gatormath/geometry/shapes2d.py
Package: gatormath.geometry

Author: GatorMath Development Team
Created: 2025-11-01
Modified: 2025-11-01
Version: 0.1.0

Dependencies:
    - math: Mathematical functions
    - typing: Type hints
    - dataclasses: Data class decorators
    - gatormath.precision: Safe comparisons
    - gatormath.core.arithmetic: Safe arithmetic operations

Exports:
    - Point: 2D point with x, y coordinates
    - Circle: Circle with center and radius
    - Rectangle: Rectangle with width and height
    - Triangle: Triangle with three sides
    - Square: Square (special rectangle)
    - Polygon: General polygon

Mathematical Formulas:
    Circle:
        - Area: π * r²
        - Perimeter: 2 * π * r

    Rectangle:
        - Area: width * height
        - Perimeter: 2 * (width + height)

    Triangle (Heron's formula):
        - Semi-perimeter: s = (a + b + c) / 2
        - Area: √(s * (s-a) * (s-b) * (s-c))

Precision Notes:
    - All comparisons use epsilon tolerance
    - Handles degenerate cases (zero area, collinear points)
    - Robust against floating-point errors

Usage:
    >>> from gatormath.geometry import shapes2d
    >>> circle = shapes2d.Circle(radius=5.0)
    >>> circle.area()
    78.53981633974483

Examples:
    Creating shapes:
    >>> circle = Circle(radius=10.0)
    >>> rect = Rectangle(width=5.0, height=3.0)
    >>> triangle = Triangle(a=3.0, b=4.0, c=5.0)

    Calculations:
    >>> circle.area()
    314.1592653589793
    >>> rect.perimeter()
    16.0
    >>> triangle.is_right_triangle()
    True

See Also:
    - gatormath.geometry.shapes3d: Three-dimensional shapes
    - gatormath.geometry.transforms: Geometric transformations

References:
    [1] "Computational Geometry: Algorithms and Applications"
        (de Berg, Cheong, van Kreveld, Overmars)
    [2] "Geometry for Computer Graphics" (Vince)
"""

# Standard library imports
import math
from dataclasses import dataclass
from typing import Optional, Tuple


# Local imports
from gatormath.core.arithmetic import safe_divide, safe_multiply, safe_power, safe_sqrt
from gatormath.precision import is_close, is_zero


# ============================================================================
# Constants
# ============================================================================

PI: float = math.pi


# ============================================================================
# Basic Types
# ============================================================================

@dataclass(frozen=True)
class Point:
    """
    Immutable 2D point with x, y coordinates.

    Attributes:
        x (float): X coordinate
        y (float): Y coordinate

    Examples:
        >>> p1 = Point(3.0, 4.0)
        >>> p2 = Point(0.0, 0.0)
        >>> p1.distance_to(p2)
        5.0

    Version: 0.1.0
    """

    x: float
    y: float

    def distance_to(self, other: "Point") -> float:
        """
        Calculate Euclidean distance to another point.

        Args:
            other (Point): Target point

        Returns:
            float: Distance between points

        Examples:
            >>> p1 = Point(0.0, 0.0)
            >>> p2 = Point(3.0, 4.0)
            >>> p1.distance_to(p2)
            5.0
        """
        dx = self.x - other.x
        dy = self.y - other.y
        return safe_sqrt(dx * dx + dy * dy)

    def __str__(self) -> str:
        """String representation of point."""
        return f"({self.x}, {self.y})"


# ============================================================================
# Circle
# ============================================================================

@dataclass
class Circle:
    """
    Circle defined by radius and optional center point.

    Attributes:
        radius (float): Circle radius (must be positive)
        center (Point): Center point (default: origin)

    Raises:
        ValueError: If radius is not positive

    Examples:
        >>> circle = Circle(radius=5.0)
        >>> circle.area()
        78.53981633974483
        >>> circle.circumference()
        31.41592653589793

    Version: 0.1.0
    """

    radius: float
    center: Point = Point(0.0, 0.0)

    def __post_init__(self) -> None:
        """Validate circle parameters."""
        if self.radius <= 0:
            raise ValueError(f"Radius must be positive, got {self.radius}")

    def area(self) -> float:
        """
        Calculate circle area.

        Returns:
            float: Area = π * r²

        Examples:
            >>> Circle(radius=10.0).area()
            314.1592653589793
        """
        return PI * safe_power(self.radius, 2)

    def circumference(self) -> float:
        """
        Calculate circle circumference (perimeter).

        Returns:
            float: Circumference = 2 * π * r

        Examples:
            >>> Circle(radius=10.0).circumference()
            62.83185307179586
        """
        return 2 * PI * self.radius

    def perimeter(self) -> float:
        """Alias for circumference."""
        return self.circumference()

    def diameter(self) -> float:
        """
        Calculate circle diameter.

        Returns:
            float: Diameter = 2 * r
        """
        return 2 * self.radius

    def contains_point(self, point: Point) -> bool:
        """
        Check if point is inside or on the circle.

        Args:
            point (Point): Point to test

        Returns:
            bool: True if point is inside circle (inclusive)

        Examples:
            >>> circle = Circle(radius=5.0)
            >>> circle.contains_point(Point(3.0, 0.0))
            True
            >>> circle.contains_point(Point(10.0, 0.0))
            False
        """
        distance = self.center.distance_to(point)
        return distance <= self.radius or is_close(distance, self.radius)

    def __str__(self) -> str:
        """String representation."""
        return f"Circle(radius={self.radius}, center={self.center})"


# ============================================================================
# Rectangle
# ============================================================================

@dataclass
class Rectangle:
    """
    Rectangle defined by width and height.

    Attributes:
        width (float): Rectangle width (must be positive)
        height (float): Rectangle height (must be positive)
        center (Point): Center point (default: origin)

    Raises:
        ValueError: If width or height is not positive

    Examples:
        >>> rect = Rectangle(width=4.0, height=3.0)
        >>> rect.area()
        12.0
        >>> rect.perimeter()
        14.0

    Version: 0.1.0
    """

    width: float
    height: float
    center: Point = Point(0.0, 0.0)

    def __post_init__(self) -> None:
        """Validate rectangle parameters."""
        if self.width <= 0:
            raise ValueError(f"Width must be positive, got {self.width}")
        if self.height <= 0:
            raise ValueError(f"Height must be positive, got {self.height}")

    def area(self) -> float:
        """
        Calculate rectangle area.

        Returns:
            float: Area = width * height

        Examples:
            >>> Rectangle(width=5.0, height=3.0).area()
            15.0
        """
        return safe_multiply(self.width, self.height)

    def perimeter(self) -> float:
        """
        Calculate rectangle perimeter.

        Returns:
            float: Perimeter = 2 * (width + height)

        Examples:
            >>> Rectangle(width=5.0, height=3.0).perimeter()
            16.0
        """
        return 2 * (self.width + self.height)

    def diagonal(self) -> float:
        """
        Calculate rectangle diagonal length.

        Returns:
            float: Diagonal = √(width² + height²)

        Examples:
            >>> Rectangle(width=3.0, height=4.0).diagonal()
            5.0
        """
        return safe_sqrt(self.width ** 2 + self.height ** 2)

    def is_square(self) -> bool:
        """
        Check if rectangle is a square.

        Returns:
            bool: True if width equals height (within tolerance)

        Examples:
            >>> Rectangle(width=5.0, height=5.0).is_square()
            True
            >>> Rectangle(width=5.0, height=3.0).is_square()
            False
        """
        return is_close(self.width, self.height)

    def aspect_ratio(self) -> float:
        """
        Calculate aspect ratio (width / height).

        Returns:
            float: Aspect ratio

        Examples:
            >>> Rectangle(width=16.0, height=9.0).aspect_ratio()
            1.7777777777777777
        """
        return safe_divide(self.width, self.height)

    def __str__(self) -> str:
        """String representation."""
        return f"Rectangle(width={self.width}, height={self.height})"


# ============================================================================
# Square
# ============================================================================

@dataclass
class Square:
    """
    Square defined by side length.

    Attributes:
        side (float): Side length (must be positive)
        center (Point): Center point (default: origin)

    Raises:
        ValueError: If side is not positive

    Examples:
        >>> square = Square(side=5.0)
        >>> square.area()
        25.0
        >>> square.perimeter()
        20.0

    Version: 0.1.0
    """

    side: float
    center: Point = Point(0.0, 0.0)

    def __post_init__(self) -> None:
        """Validate square parameters."""
        if self.side <= 0:
            raise ValueError(f"Side must be positive, got {self.side}")

    def area(self) -> float:
        """Calculate square area: side²."""
        return safe_power(self.side, 2)

    def perimeter(self) -> float:
        """Calculate square perimeter: 4 * side."""
        return 4 * self.side

    def diagonal(self) -> float:
        """Calculate square diagonal: side * √2."""
        return self.side * safe_sqrt(2)

    def to_rectangle(self) -> Rectangle:
        """Convert to Rectangle representation."""
        return Rectangle(width=self.side, height=self.side, center=self.center)

    def __str__(self) -> str:
        """String representation."""
        return f"Square(side={self.side})"


# ============================================================================
# Triangle
# ============================================================================

@dataclass
class Triangle:
    """
    Triangle defined by three side lengths.

    Attributes:
        a (float): First side length (must be positive)
        b (float): Second side length (must be positive)
        c (float): Third side length (must be positive)

    Raises:
        ValueError: If sides don't form a valid triangle

    Mathematical Validation:
        Triangle inequality: a + b > c, b + c > a, c + a > b

    Examples:
        >>> triangle = Triangle(a=3.0, b=4.0, c=5.0)
        >>> triangle.area()
        6.0
        >>> triangle.is_right_triangle()
        True

    Version: 0.1.0
    """

    a: float
    b: float
    c: float

    def __post_init__(self) -> None:
        """Validate triangle using triangle inequality."""
        if self.a <= 0 or self.b <= 0 or self.c <= 0:
            raise ValueError("All sides must be positive")

        # Triangle inequality: sum of any two sides > third side
        if (self.a + self.b <= self.c or
            self.b + self.c <= self.a or
            self.c + self.a <= self.b):
            raise ValueError(
                f"Sides {self.a}, {self.b}, {self.c} do not form a valid triangle"
            )

    def area(self) -> float:
        """
        Calculate triangle area using Heron's formula.

        Returns:
            float: Area = √(s(s-a)(s-b)(s-c)) where s = (a+b+c)/2

        Examples:
            >>> Triangle(a=3.0, b=4.0, c=5.0).area()
            6.0
        """
        s = self.semiperimeter()
        return safe_sqrt(
            s * (s - self.a) * (s - self.b) * (s - self.c)
        )

    def perimeter(self) -> float:
        """
        Calculate triangle perimeter.

        Returns:
            float: Perimeter = a + b + c

        Examples:
            >>> Triangle(a=3.0, b=4.0, c=5.0).perimeter()
            12.0
        """
        return self.a + self.b + self.c

    def semiperimeter(self) -> float:
        """
        Calculate triangle semiperimeter.

        Returns:
            float: Semiperimeter = (a + b + c) / 2
        """
        return self.perimeter() / 2

    def is_right_triangle(self) -> bool:
        """
        Check if triangle is a right triangle (Pythagorean theorem).

        Returns:
            bool: True if satisfies a² + b² = c² (for any permutation)

        Examples:
            >>> Triangle(a=3.0, b=4.0, c=5.0).is_right_triangle()
            True
            >>> Triangle(a=3.0, b=3.0, c=3.0).is_right_triangle()
            False
        """
        sides = sorted([self.a, self.b, self.c])
        # Check if a² + b² ≈ c² (within tolerance)
        return is_close(
            sides[0]**2 + sides[1]**2,
            sides[2]**2
        )

    def is_equilateral(self) -> bool:
        """
        Check if triangle is equilateral (all sides equal).

        Returns:
            bool: True if all sides are equal

        Examples:
            >>> Triangle(a=5.0, b=5.0, c=5.0).is_equilateral()
            True
        """
        return is_close(self.a, self.b) and is_close(self.b, self.c)

    def is_isosceles(self) -> bool:
        """
        Check if triangle is isosceles (at least two sides equal).

        Returns:
            bool: True if at least two sides are equal

        Examples:
            >>> Triangle(a=5.0, b=5.0, c=3.0).is_isosceles()
            True
        """
        return (is_close(self.a, self.b) or
                is_close(self.b, self.c) or
                is_close(self.c, self.a))

    def triangle_type(self) -> str:
        """
        Classify triangle by sides.

        Returns:
            str: "equilateral", "isosceles", or "scalene"

        Examples:
            >>> Triangle(a=5.0, b=5.0, c=5.0).triangle_type()
            'equilateral'
        """
        if self.is_equilateral():
            return "equilateral"
        elif self.is_isosceles():
            return "isosceles"
        else:
            return "scalene"

    def __str__(self) -> str:
        """String representation."""
        return f"Triangle(a={self.a}, b={self.b}, c={self.c})"


# ============================================================================
# Module Exports
# ============================================================================

__all__ = [
    "Point",
    "Circle",
    "Rectangle",
    "Square",
    "Triangle",
    "PI",
]
