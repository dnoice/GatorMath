#!/usr/bin/env python3
"""
GatorMath Basic Usage Examples

Demonstrates fundamental usage of GatorMath library including:
- Safe arithmetic operations
- Precision handling
- Geometric calculations
- CLI theming

Author: GatorMath Development Team
Version: 0.1.0
"""

from rich.console import Console

from gatormath.cli.theme import create_console
from gatormath.core import arithmetic
from gatormath.geometry import shapes2d
from gatormath.precision import is_close


def main() -> None:
    """Run all example demonstrations."""
    console = create_console()

    console.print("[header]GatorMath Basic Usage Examples[/]\n")

    # ========================================================================
    # 1. Arithmetic Operations
    # ========================================================================
    console.print("[subheader]1. Safe Arithmetic Operations[/]")

    # Basic operations
    console.print(f"  2 + 2 = [math.result]{arithmetic.safe_add(2, 2)}[/]")
    console.print(f"  10 / 3 = [math.result]{arithmetic.safe_divide(10, 3):.6f}[/]")
    console.print(f"  √144 = [math.result]{arithmetic.safe_sqrt(144)}[/]")
    console.print(f"  2^10 = [math.result]{arithmetic.safe_power(2, 10)}[/]")
    console.print(f"  5! = [math.result]{arithmetic.factorial(5)}[/]")
    console.print(f"  gcd(48, 18) = [math.result]{arithmetic.gcd(48, 18)}[/]")
    console.print(f"  lcm(12, 18) = [math.result]{arithmetic.lcm(12, 18)}[/]")
    console.print()

    # ========================================================================
    # 2. Precision Handling
    # ========================================================================
    console.print("[subheader]2. Floating-Point Precision[/]")

    val1 = 0.1 + 0.2
    val2 = 0.3

    console.print(f"  0.1 + 0.2 = [code]{val1:.20f}[/]")
    console.print(f"  0.3       = [code]{val2:.20f}[/]")
    console.print(f"  Standard (==): [error]{val1 == val2}[/]")
    console.print(f"  GatorMath: [success]{is_close(val1, val2)}[/]")
    console.print()

    # ========================================================================
    # 3. Geometric Shapes
    # ========================================================================
    console.print("[subheader]3. Geometric Calculations[/]")

    # Circle
    circle = shapes2d.Circle(radius=10.0)
    console.print(f"  Circle (r=10):")
    console.print(f"    Area: [geometry.area]{circle.area():.4f}[/]")
    console.print(f"    Circumference: [geometry.area]{circle.circumference():.4f}[/]")

    # Rectangle
    rect = shapes2d.Rectangle(width=5.0, height=3.0)
    console.print(f"  Rectangle (5×3):")
    console.print(f"    Area: [geometry.area]{rect.area():.4f}[/]")
    console.print(f"    Perimeter: [geometry.area]{rect.perimeter():.4f}[/]")
    console.print(f"    Diagonal: [geometry.area]{rect.diagonal():.4f}[/]")

    # Triangle (3-4-5 right triangle)
    triangle = shapes2d.Triangle(a=3.0, b=4.0, c=5.0)
    console.print(f"  Triangle (3-4-5):")
    console.print(f"    Area: [geometry.area]{triangle.area():.4f}[/]")
    console.print(f"    Type: [geometry.shape]{triangle.triangle_type()}[/]")
    console.print(f"    Right triangle: [success]{triangle.is_right_triangle()}[/]")
    console.print()

    # ========================================================================
    # 4. Error Handling
    # ========================================================================
    console.print("[subheader]4. Error Handling[/]")

    # Division by zero
    try:
        arithmetic.safe_divide(10, 0)
    except ZeroDivisionError as e:
        console.print(f"  [error]Division by zero caught:[/] {e}")

    # Invalid triangle
    try:
        shapes2d.Triangle(a=1.0, b=2.0, c=10.0)
    except ValueError as e:
        console.print(f"  [error]Invalid triangle caught:[/] {e}")

    console.print()
    console.print("[success]✓ All examples completed![/]")


if __name__ == "__main__":
    main()
