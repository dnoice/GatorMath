"""
Module Name: shapes2d

Description:
    2D geometric shapes with comprehensive property calculations, type
    classification, and degenerate case handling. Provides Circle, Rectangle,
    Square, and Triangle classes with area, perimeter, and geometric properties.

Module Path: gatormath/geometry/shapes2d.py
Package: gatormath.geometry

Author: Dennis 'dnoice' Smaltz
AI Acknowledgement: Claude Code
Created: 2025-11-02
Modified: 2025-11-02
Version: 0.1.0

Dependencies:
    - math: Standard library math functions
    - typing: Type hints
    - gatormath.precision: Floating-point comparison utilities

Exports:
    - Circle: Circle shape with radius
    - Rectangle: Rectangle shape with width and height
    - Square: Square shape with side length
    - Triangle: Triangle shape with three sides

Examples:
    >>> circle = Circle(radius=5.0)
    >>> circle.area()
    78.53981633974483

    >>> triangle = Triangle(a=3.0, b=4.0, c=5.0)
    >>> triangle.is_right_triangle()
    True

Notes:
    All shapes validate inputs and handle degenerate cases appropriately
    Precision-aware comparisons used throughout

References:
    [1] Euclidean geometry principles
    [2] Triangle inequality theorem
"""

import math
from typing import Literal

from gatormath.precision.comparison import is_close, is_zero


class Circle:
    """
    Circle geometric shape.

    Detailed Description:
        Represents a circle defined by its radius. Provides methods for
        calculating area, circumference, diameter, and other properties.
        Validates that radius is non-negative.

    Attributes:
        radius (float): Circle radius (must be non-negative)

    Methods:
        area: Calculate circle area (πr²)
        circumference: Calculate circle circumference (2πr)
        diameter: Calculate circle diameter (2r)

    Mathematical Formulation:
        Area = πr²
        Circumference = 2πr
        Diameter = 2r

    Precision Notes:
        Uses math.pi for π constant
        Subject to floating-point precision limits

    Examples:
        >>> circle = Circle(radius=5.0)
        >>> circle.area()
        78.53981633974483

        >>> circle.circumference()
        31.41592653589793

        >>> circle.diameter()
        10.0

    See Also:
        - Rectangle: Rectangular shape
        - Triangle: Triangular shape

    Version: 0.1.0
    """

    def __init__(self, radius: float) -> None:
        """
        Initialize Circle with radius.

        Args:
            radius (float): Circle radius
                - Range: radius >= 0
                - Constraint: Must be non-negative

        Raises:
            ValueError: If radius is negative

        Examples:
            >>> circle = Circle(radius=5.0)
            >>> circle.radius
            5.0

            >>> Circle(radius=-1.0)
            Traceback (most recent call last):
                ...
            ValueError: Radius must be non-negative, got -1.0

        Version: 0.1.0
        """
        if radius < 0:
            raise ValueError(f"Radius must be non-negative, got {radius}")

        self.radius = float(radius)

    def area(self) -> float:
        """
        Calculate circle area.

        Returns:
            float: Area of circle (πr²)

        Algorithm:
            Area = π * radius²

        Complexity:
            Time: O(1)
            Space: O(1)

        Examples:
            >>> circle = Circle(radius=5.0)
            >>> circle.area()
            78.53981633974483

            >>> Circle(radius=0.0).area()
            0.0

        Version: 0.1.0
        """
        return math.pi * self.radius ** 2

    def circumference(self) -> float:
        """
        Calculate circle circumference.

        Returns:
            float: Circumference of circle (2πr)

        Algorithm:
            Circumference = 2 * π * radius

        Complexity:
            Time: O(1)
            Space: O(1)

        Examples:
            >>> circle = Circle(radius=5.0)
            >>> circle.circumference()
            31.41592653589793

        Version: 0.1.0
        """
        return 2.0 * math.pi * self.radius

    def diameter(self) -> float:
        """
        Calculate circle diameter.

        Returns:
            float: Diameter of circle (2r)

        Complexity:
            Time: O(1)
            Space: O(1)

        Examples:
            >>> circle = Circle(radius=5.0)
            >>> circle.diameter()
            10.0

        Version: 0.1.0
        """
        return 2.0 * self.radius

    def __repr__(self) -> str:
        return f"Circle(radius={self.radius})"


class Rectangle:
    """
    Rectangle geometric shape.

    Detailed Description:
        Represents a rectangle defined by width and height. Provides methods
        for calculating area, perimeter, diagonal, and checking if it's a square.
        Validates that dimensions are non-negative.

    Attributes:
        width (float): Rectangle width (must be non-negative)
        height (float): Rectangle height (must be non-negative)

    Methods:
        area: Calculate rectangle area (w × h)
        perimeter: Calculate rectangle perimeter (2w + 2h)
        diagonal: Calculate diagonal length (√(w² + h²))
        is_square: Check if rectangle is a square

    Mathematical Formulation:
        Area = width × height
        Perimeter = 2(width + height)
        Diagonal = √(width² + height²)

    Examples:
        >>> rect = Rectangle(width=4.0, height=3.0)
        >>> rect.area()
        12.0

        >>> rect.perimeter()
        14.0

        >>> rect.diagonal()
        5.0

    Version: 0.1.0
    """

    def __init__(self, width: float, height: float) -> None:
        """
        Initialize Rectangle with width and height.

        Args:
            width (float): Rectangle width
                - Range: width >= 0
            height (float): Rectangle height
                - Range: height >= 0

        Raises:
            ValueError: If width or height is negative

        Examples:
            >>> rect = Rectangle(width=4.0, height=3.0)
            >>> rect.width
            4.0

        Version: 0.1.0
        """
        if width < 0:
            raise ValueError(f"Width must be non-negative, got {width}")
        if height < 0:
            raise ValueError(f"Height must be non-negative, got {height}")

        self.width = float(width)
        self.height = float(height)

    def area(self) -> float:
        """Calculate rectangle area."""
        return self.width * self.height

    def perimeter(self) -> float:
        """Calculate rectangle perimeter."""
        return 2.0 * (self.width + self.height)

    def diagonal(self) -> float:
        """Calculate diagonal length using Pythagorean theorem."""
        return math.sqrt(self.width ** 2 + self.height ** 2)

    def is_square(self) -> bool:
        """Check if rectangle is a square (width ≈ height)."""
        return is_close(self.width, self.height)

    def __repr__(self) -> str:
        return f"Rectangle(width={self.width}, height={self.height})"


class Square:
    """
    Square geometric shape.

    Detailed Description:
        Represents a square defined by side length. Special case of rectangle
        where all sides are equal. Provides methods for area, perimeter,
        and diagonal calculations.

    Attributes:
        side (float): Square side length (must be non-negative)

    Methods:
        area: Calculate square area (s²)
        perimeter: Calculate square perimeter (4s)
        diagonal: Calculate diagonal length (s√2)

    Mathematical Formulation:
        Area = side²
        Perimeter = 4 × side
        Diagonal = side × √2

    Examples:
        >>> square = Square(side=5.0)
        >>> square.area()
        25.0

        >>> square.perimeter()
        20.0

    Version: 0.1.0
    """

    def __init__(self, side: float) -> None:
        """Initialize Square with side length."""
        if side < 0:
            raise ValueError(f"Side must be non-negative, got {side}")

        self.side = float(side)

    def area(self) -> float:
        """Calculate square area."""
        return self.side ** 2

    def perimeter(self) -> float:
        """Calculate square perimeter."""
        return 4.0 * self.side

    def diagonal(self) -> float:
        """Calculate diagonal length."""
        return self.side * math.sqrt(2.0)

    def __repr__(self) -> str:
        return f"Square(side={self.side})"


class Triangle:
    """
    Triangle geometric shape.

    Detailed Description:
        Represents a triangle defined by three side lengths. Validates
        triangle inequality theorem. Provides comprehensive methods for
        area calculation (Heron's formula), perimeter, angle calculations,
        and triangle type classification.

    Attributes:
        a (float): First side length
        b (float): Second side length
        c (float): Third side length

    Methods:
        area: Calculate area using Heron's formula
        perimeter: Calculate perimeter (a + b + c)
        is_valid: Check if sides form valid triangle
        is_right_triangle: Check if triangle is right-angled
        is_equilateral: Check if all sides are equal
        is_isosceles: Check if two sides are equal
        triangle_type: Classify triangle type

    Mathematical Formulation:
        Area = √(s(s-a)(s-b)(s-c)) where s = (a+b+c)/2 (Heron's formula)
        Triangle Inequality: a + b > c, b + c > a, a + c > b

    Examples:
        >>> triangle = Triangle(a=3.0, b=4.0, c=5.0)
        >>> triangle.area()
        6.0

        >>> triangle.is_right_triangle()
        True

        >>> triangle.triangle_type()
        'scalene'

    Version: 0.1.0
    """

    def __init__(self, a: float, b: float, c: float) -> None:
        """
        Initialize Triangle with three side lengths.

        Args:
            a (float): First side length (must be positive)
            b (float): Second side length (must be positive)
            c (float): Third side length (must be positive)

        Raises:
            ValueError: If any side is non-positive or triangle inequality fails

        Examples:
            >>> triangle = Triangle(a=3.0, b=4.0, c=5.0)
            >>> triangle.a
            3.0

        Version: 0.1.0
        """
        if a <= 0 or b <= 0 or c <= 0:
            raise ValueError("All sides must be positive")

        # Check triangle inequality
        if not (a + b > c and b + c > a and a + c > b):
            raise ValueError(
                f"Sides do not satisfy triangle inequality: {a}, {b}, {c}"
            )

        self.a = float(a)
        self.b = float(b)
        self.c = float(c)

    def area(self) -> float:
        """
        Calculate triangle area using Heron's formula.

        Algorithm:
            s = (a + b + c) / 2  (semi-perimeter)
            Area = √(s(s-a)(s-b)(s-c))

        Complexity:
            Time: O(1)
            Space: O(1)

        Examples:
            >>> Triangle(a=3.0, b=4.0, c=5.0).area()
            6.0

        Version: 0.1.0
        """
        s = (self.a + self.b + self.c) / 2.0
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def perimeter(self) -> float:
        """Calculate triangle perimeter."""
        return self.a + self.b + self.c

    def is_valid(self) -> bool:
        """Check if triangle is valid (redundant, already checked in __init__)."""
        return True

    def is_right_triangle(self) -> bool:
        """
        Check if triangle is right-angled using Pythagorean theorem.

        Examples:
            >>> Triangle(a=3.0, b=4.0, c=5.0).is_right_triangle()
            True

        Version: 0.1.0
        """
        sides = sorted([self.a, self.b, self.c])
        return is_close(sides[0] ** 2 + sides[1] ** 2, sides[2] ** 2)

    def is_equilateral(self) -> bool:
        """Check if all sides are equal."""
        return is_close(self.a, self.b) and is_close(self.b, self.c)

    def is_isosceles(self) -> bool:
        """Check if at least two sides are equal."""
        return (is_close(self.a, self.b) or
                is_close(self.b, self.c) or
                is_close(self.a, self.c))

    def triangle_type(self) -> Literal["equilateral", "isosceles", "scalene"]:
        """
        Classify triangle type based on side lengths.

        Returns:
            str: "equilateral", "isosceles", or "scalene"

        Examples:
            >>> Triangle(a=5.0, b=5.0, c=5.0).triangle_type()
            'equilateral'

            >>> Triangle(a=5.0, b=5.0, c=3.0).triangle_type()
            'isosceles'

            >>> Triangle(a=3.0, b=4.0, c=5.0).triangle_type()
            'scalene'

        Version: 0.1.0
        """
        if self.is_equilateral():
            return "equilateral"
        elif self.is_isosceles():
            return "isosceles"
        else:
            return "scalene"

    def __repr__(self) -> str:
        return f"Triangle(a={self.a}, b={self.b}, c={self.c})"
