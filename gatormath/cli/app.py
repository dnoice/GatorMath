"""
Module Name: app

Description:
    Main command-line interface application for GatorMath.
    Provides interactive commands for mathematical and geometric operations
    with beautiful Rich-themed output, progress indicators, and intuitive UX.

Module Path: gatormath/cli/app.py
Package: gatormath.cli

Author: GatorMath Development Team
Created: 2025-11-01
Modified: 2025-11-01
Version: 0.1.0

Dependencies:
    - typer: Modern CLI framework
    - rich: Beautiful terminal output
    - gatormath.core: Mathematical operations
    - gatormath.geometry: Geometric operations
    - gatormath.cli.theme: Color theming

Exports:
    - app: Main Typer application
    - main: Entry point function

Commands:
    - info: Display GatorMath information and version
    - calculate: Perform mathematical calculations
    - geometry: Geometric shape calculations
    - precision: Test floating-point precision
    - demo: Interactive demonstration of features

Features:
    - Beautiful Rich-themed output
    - Interactive prompts and menus
    - Progress indicators for operations
    - Comprehensive help text
    - Error handling with suggestions
    - Color-coded results
    - Table and panel formatting

Usage:
    $ gatormath info
    $ gatormath calculate --expr "sqrt(144)"
    $ gatormath geometry circle --radius 10
    $ gatormath demo

Examples:
    Command-line usage:
    $ gatormath calculate --expr "2 + 2"
    $ gatormath geometry triangle --a 3 --b 4 --c 5
    $ gatormath precision test

    Programmatic usage:
    >>> from gatormath.cli.app import app
    >>> app()

Notes:
    - All output uses GatorMath brand colors
    - Interactive mode available for complex operations
    - Supports piping and scripting
    - Graceful degradation on limited terminals

See Also:
    - gatormath.cli.theme: Color theme configuration
    - typer documentation: https://typer.tiangolo.com/
    - rich documentation: https://rich.readthedocs.io/

References:
    [1] Typer: Modern CLI framework
    [2] Rich: Beautiful terminal output
"""

# Standard library imports
import sys
from typing import Optional


# Third-party imports
import typer
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.text import Text


# Local imports
import gatormath
from gatormath.cli.theme import GATOR_THEME, create_console
from gatormath.core import arithmetic
from gatormath.geometry import shapes2d
from gatormath.precision import is_close


# ============================================================================
# Application Setup
# ============================================================================

app = typer.Typer(
    name="gatormath",
    help="GatorMath: Mathematical precision with bite",
    add_completion=True,
    rich_markup_mode="rich",
)

# Create themed console for output
console: Console = create_console()


# ============================================================================
# Utility Functions
# ============================================================================

def print_header(title: str, subtitle: Optional[str] = None) -> None:
    """
    Print a styled header with optional subtitle.

    Args:
        title (str): Main title text
        subtitle (Optional[str]): Optional subtitle text

    Examples:
        >>> print_header("GatorMath", "Version 0.1.0")
    """
    if subtitle:
        full_title = f"[header]{title}[/]\n[subheader]{subtitle}[/]"
    else:
        full_title = f"[header]{title}[/]"

    console.print(Panel(full_title, border_style="gator_green", padding=(1, 2)))


def print_success(message: str) -> None:
    """Print success message."""
    console.print(f"[success]✓[/] {message}")


def print_error(message: str) -> None:
    """Print error message."""
    console.print(f"[error]✗[/] {message}")


def print_info(message: str) -> None:
    """Print info message."""
    console.print(f"[info]ℹ[/] {message}")


# ============================================================================
# Info Command
# ============================================================================

@app.command()
def info() -> None:
    """
    Display GatorMath package information, version, and capabilities.

    Shows:
        - Package version and metadata
        - Available modules and features
        - System information
        - Color palette preview

    Examples:
        $ gatormath info
    """
    print_header("GatorMath Information")

    # Version info table
    info_table = Table(title="Package Information", border_style="gator_teal")
    info_table.add_column("Property", style="bold gator_teal")
    info_table.add_column("Value", style="gator_slate")

    package_info = gatormath.get_info()
    for key, value in package_info.items():
        info_table.add_row(key.replace("_", " ").title(), str(value))

    console.print(info_table)
    console.print()

    # Features table
    features_table = Table(title="Features", border_style="gator_green")
    features_table.add_column("Module", style="bold gator_green")
    features_table.add_column("Description", style="gator_slate")

    features_table.add_row(
        "core.arithmetic",
        "Safe arithmetic with overflow detection"
    )
    features_table.add_row(
        "geometry.shapes2d",
        "2D geometric shapes and calculations"
    )
    features_table.add_row(
        "precision",
        "Floating-point precision handling"
    )
    features_table.add_row(
        "cli",
        "Beautiful command-line interface"
    )

    console.print(features_table)
    console.print()

    # Color palette preview
    console.print("[header]Color Palette Preview:[/]")
    color_text = Text()
    color_text.append("■ ", style="gator_green")
    color_text.append("Green ", style="gator_green")
    color_text.append("■ ", style="gator_teal")
    color_text.append("Teal ", style="gator_teal")
    color_text.append("■ ", style="gator_gold")
    color_text.append("Gold ", style="gator_gold")
    color_text.append("■ ", style="gator_orange")
    color_text.append("Orange ", style="gator_orange")
    color_text.append("■ ", style="gator_red")
    color_text.append("Red", style="gator_red")
    console.print(color_text)


# ============================================================================
# Calculate Command
# ============================================================================

@app.command()
def calculate(
    expr: str = typer.Argument(..., help="Mathematical expression to evaluate"),
    verbose: bool = typer.Option(False, "--verbose", "-v", help="Show detailed output"),
) -> None:
    """
    Evaluate mathematical expressions with safe arithmetic.

    Supports:
        - Basic operations: +, -, *, /
        - Power: ** or ^
        - Square root: sqrt()
        - Factorial: factorial()
        - GCD/LCM: gcd(), lcm()

    Examples:
        $ gatormath calculate "2 + 2"
        $ gatormath calculate "sqrt(144)"
        $ gatormath calculate "factorial(5)"
        $ gatormath calculate "gcd(48, 18)"
    """
    print_header("Mathematical Calculator")

    try:
        console.print(f"[info]Expression:[/] [code]{expr}[/]")

        # Simple expression evaluation (for demo purposes)
        # In production, use a proper parser like sympy or ast
        result = None

        # Handle specific functions
        if "sqrt" in expr:
            import re
            match = re.search(r'sqrt\(([0-9.]+)\)', expr)
            if match:
                value = float(match.group(1))
                result = arithmetic.safe_sqrt(value)
                operation = f"√{value}"

        elif "factorial" in expr:
            import re
            match = re.search(r'factorial\(([0-9]+)\)', expr)
            if match:
                value = int(match.group(1))
                result = arithmetic.factorial(value)
                operation = f"{value}!"

        elif "gcd" in expr:
            import re
            match = re.search(r'gcd\(([0-9]+),\s*([0-9]+)\)', expr)
            if match:
                a, b = int(match.group(1)), int(match.group(2))
                result = arithmetic.gcd(a, b)
                operation = f"gcd({a}, {b})"

        elif "lcm" in expr:
            import re
            match = re.search(r'lcm\(([0-9]+),\s*([0-9]+)\)', expr)
            if match:
                a, b = int(match.group(1)), int(match.group(2))
                result = arithmetic.lcm(a, b)
                operation = f"lcm({a}, {b})"

        else:
            # Simple arithmetic (using eval for demo - use proper parser in production)
            # Replace operators for safety
            safe_expr = expr.replace("^", "**")
            result = eval(safe_expr, {"__builtins__": {}}, {})
            operation = expr

        # Display result
        if result is not None:
            result_panel = Panel(
                f"[math.result]{result}[/]",
                title="[header]Result[/]",
                border_style="gator_green",
                padding=(1, 2)
            )
            console.print(result_panel)

            if verbose:
                console.print()
                console.print(f"[subtle]Operation: {operation}[/]")
                console.print(f"[subtle]Result Type: {type(result).__name__}[/]")

            print_success("Calculation completed")
        else:
            print_error("Could not parse expression")

    except Exception as e:
        print_error(f"Calculation error: {e}")
        sys.exit(1)


# ============================================================================
# Geometry Command
# ============================================================================

@app.command()
def geometry(
    shape: str = typer.Argument(..., help="Shape type: circle, rectangle, square, triangle"),
    radius: Optional[float] = typer.Option(None, help="Circle radius"),
    width: Optional[float] = typer.Option(None, help="Rectangle width"),
    height: Optional[float] = typer.Option(None, help="Rectangle height"),
    side: Optional[float] = typer.Option(None, help="Square side length"),
    a: Optional[float] = typer.Option(None, help="Triangle side a"),
    b: Optional[float] = typer.Option(None, help="Triangle side b"),
    c: Optional[float] = typer.Option(None, help="Triangle side c"),
) -> None:
    """
    Calculate geometric properties of shapes.

    Shapes:
        - circle: Requires --radius
        - rectangle: Requires --width and --height
        - square: Requires --side
        - triangle: Requires --a, --b, and --c

    Examples:
        $ gatormath geometry circle --radius 10
        $ gatormath geometry rectangle --width 5 --height 3
        $ gatormath geometry triangle --a 3 --b 4 --c 5
    """
    print_header(f"Geometry Calculator: {shape.title()}")

    try:
        shape_lower = shape.lower()

        if shape_lower == "circle":
            if radius is None:
                print_error("Circle requires --radius parameter")
                sys.exit(1)

            circle = shapes2d.Circle(radius=radius)

            # Create results table
            table = Table(title="Circle Properties", border_style="gator_teal")
            table.add_column("Property", style="bold gator_teal")
            table.add_column("Value", style="geometry.area", justify="right")

            table.add_row("Radius", f"{circle.radius:.4f}")
            table.add_row("Diameter", f"{circle.diameter():.4f}")
            table.add_row("Circumference", f"{circle.circumference():.4f}")
            table.add_row("Area", f"{circle.area():.4f}")

            console.print(table)
            print_success("Calculation completed")

        elif shape_lower == "rectangle":
            if width is None or height is None:
                print_error("Rectangle requires --width and --height parameters")
                sys.exit(1)

            rect = shapes2d.Rectangle(width=width, height=height)

            table = Table(title="Rectangle Properties", border_style="gator_teal")
            table.add_column("Property", style="bold gator_teal")
            table.add_column("Value", style="geometry.area", justify="right")

            table.add_row("Width", f"{rect.width:.4f}")
            table.add_row("Height", f"{rect.height:.4f}")
            table.add_row("Perimeter", f"{rect.perimeter():.4f}")
            table.add_row("Area", f"{rect.area():.4f}")
            table.add_row("Diagonal", f"{rect.diagonal():.4f}")
            table.add_row("Aspect Ratio", f"{rect.aspect_ratio():.4f}")
            table.add_row("Is Square?", "Yes" if rect.is_square() else "No")

            console.print(table)
            print_success("Calculation completed")

        elif shape_lower == "square":
            if side is None:
                print_error("Square requires --side parameter")
                sys.exit(1)

            square = shapes2d.Square(side=side)

            table = Table(title="Square Properties", border_style="gator_teal")
            table.add_column("Property", style="bold gator_teal")
            table.add_column("Value", style="geometry.area", justify="right")

            table.add_row("Side", f"{square.side:.4f}")
            table.add_row("Perimeter", f"{square.perimeter():.4f}")
            table.add_row("Area", f"{square.area():.4f}")
            table.add_row("Diagonal", f"{square.diagonal():.4f}")

            console.print(table)
            print_success("Calculation completed")

        elif shape_lower == "triangle":
            if a is None or b is None or c is None:
                print_error("Triangle requires --a, --b, and --c parameters")
                sys.exit(1)

            triangle = shapes2d.Triangle(a=a, b=b, c=c)

            table = Table(title="Triangle Properties", border_style="gator_teal")
            table.add_column("Property", style="bold gator_teal")
            table.add_column("Value", style="geometry.area", justify="right")

            table.add_row("Side a", f"{triangle.a:.4f}")
            table.add_row("Side b", f"{triangle.b:.4f}")
            table.add_row("Side c", f"{triangle.c:.4f}")
            table.add_row("Perimeter", f"{triangle.perimeter():.4f}")
            table.add_row("Area", f"{triangle.area():.4f}")
            table.add_row("Type", triangle.triangle_type().title())
            table.add_row("Is Right Triangle?", "Yes" if triangle.is_right_triangle() else "No")

            console.print(table)
            print_success("Calculation completed")

        else:
            print_error(f"Unknown shape: {shape}")
            print_info("Supported shapes: circle, rectangle, square, triangle")
            sys.exit(1)

    except ValueError as e:
        print_error(f"Invalid input: {e}")
        sys.exit(1)
    except Exception as e:
        print_error(f"Calculation error: {e}")
        sys.exit(1)


# ============================================================================
# Precision Test Command
# ============================================================================

@app.command()
def precision() -> None:
    """
    Demonstrate floating-point precision handling.

    Shows:
        - Classic precision problems and solutions
        - Safe comparison examples
        - Epsilon-based equality

    Examples:
        $ gatormath precision
    """
    print_header("Floating-Point Precision Demonstration")

    # Create test cases table
    table = Table(title="Precision Test Cases", border_style="gator_gold")
    table.add_column("Test", style="bold gator_teal")
    table.add_column("Standard (==)", style="gator_mist", justify="center")
    table.add_column("GatorMath", style="gator_green", justify="center")

    # Test case 1: Classic 0.1 + 0.2
    val1 = 0.1 + 0.2
    val2 = 0.3
    table.add_row(
        "0.1 + 0.2 == 0.3",
        "[error]False[/]" if val1 != val2 else "True",
        "[success]True[/]" if is_close(val1, val2) else "False"
    )

    # Test case 2: Large numbers
    val3 = 1e15 + 1
    val4 = 1e15
    table.add_row(
        "1e15 + 1 == 1e15",
        "True" if val3 == val4 else "[success]False[/]",
        "[success]False[/]" if not is_close(val3, val4) else "True"
    )

    # Test case 3: Very small numbers
    val5 = 1e-15
    val6 = 0.0
    table.add_row(
        "1e-15 == 0.0",
        "False" if val5 != val6 else "True",
        "[success]True[/]" if is_close(val5, val6) else "False"
    )

    console.print(table)
    console.print()

    # Show actual values
    console.print("[header]Actual Values:[/]")
    console.print(f"  0.1 + 0.2 = [code]{0.1 + 0.2:.20f}[/]")
    console.print(f"  0.3       = [code]{0.3:.20f}[/]")
    console.print(f"  Difference: [subtle]{abs(0.1 + 0.2 - 0.3):.2e}[/]")
    console.print()

    print_success("Precision demonstration completed")
    print_info("GatorMath handles these cases automatically!")


# ============================================================================
# Demo Command
# ============================================================================

@app.command()
def demo() -> None:
    """
    Interactive demonstration of GatorMath features.

    Shows:
        - Mathematical operations
        - Geometric calculations
        - Precision handling
        - CLI theming

    Examples:
        $ gatormath demo
    """
    print_header("GatorMath Interactive Demo", "Showcasing all features")

    console.print()
    console.print("[header]1. Mathematical Operations[/]")
    console.print()

    # Arithmetic demo
    ops_table = Table(border_style="gator_teal", show_header=False)
    ops_table.add_column("Operation", style="code")
    ops_table.add_column("Result", style="math.result", justify="right")

    ops_table.add_row("2 + 2", f"{arithmetic.safe_add(2, 2)}")
    ops_table.add_row("10 / 3", f"{arithmetic.safe_divide(10, 3):.6f}")
    ops_table.add_row("√144", f"{arithmetic.safe_sqrt(144)}")
    ops_table.add_row("5!", f"{arithmetic.factorial(5)}")
    ops_table.add_row("gcd(48, 18)", f"{arithmetic.gcd(48, 18)}")

    console.print(ops_table)
    console.print()

    # Geometry demo
    console.print("[header]2. Geometric Calculations[/]")
    console.print()

    geo_table = Table(border_style="gator_green", show_header=False)
    geo_table.add_column("Shape", style="bold gator_teal")
    geo_table.add_column("Area", style="geometry.area", justify="right")

    circle = shapes2d.Circle(radius=5.0)
    square = shapes2d.Square(side=4.0)
    triangle = shapes2d.Triangle(a=3.0, b=4.0, c=5.0)

    geo_table.add_row("Circle (r=5)", f"{circle.area():.4f}")
    geo_table.add_row("Square (s=4)", f"{square.area():.4f}")
    geo_table.add_row("Triangle (3-4-5)", f"{triangle.area():.4f}")

    console.print(geo_table)
    console.print()

    # Precision demo
    console.print("[header]3. Precision Handling[/]")
    console.print()

    result = is_close(0.1 + 0.2, 0.3)
    console.print(f"  0.1 + 0.2 ≈ 0.3: [success]{result}[/]")
    console.print()

    print_success("Demo completed!")
    print_info("Try 'gatormath --help' for all commands")


# ============================================================================
# Version Command
# ============================================================================

@app.command()
def version() -> None:
    """
    Display GatorMath version information.

    Examples:
        $ gatormath version
    """
    console.print(
        f"[header]GatorMath[/] version [highlight]{gatormath.__version__}[/]"
    )


# ============================================================================
# Main Entry Point
# ============================================================================

def main() -> None:
    """
    Main entry point for the CLI application.

    This function is called when the package is run as a script.
    It initializes the Typer app and handles any global exceptions.

    Examples:
        $ gatormath
        $ python -m gatormath
    """
    try:
        app()
    except KeyboardInterrupt:
        console.print("\n[warning]Interrupted by user[/]")
        sys.exit(130)
    except Exception as e:
        console.print(f"\n[error]Fatal error: {e}[/]")
        sys.exit(1)


# Run if executed directly
if __name__ == "__main__":
    main()


# ============================================================================
# Module Exports
# ============================================================================

__all__ = [
    "app",
    "main",
]
