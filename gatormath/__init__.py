"""
Module Name: gatormath

Description:
    GatorMath is a comprehensive mathematical and geometric toolkit for Python
    that provides robust numerical operations, precision handling, and an
    intuitive CLI interface. Designed for developers who need reliable
    mathematical computations without fighting floating-point edge cases.

Module Path: gatormath/__init__.py
Package: gatormath

Author: GatorMath Development Team
Created: 2025-11-01
Modified: 2025-11-01
Version: 0.1.0

Exports:
    Core Mathematics:
        - arithmetic: Basic arithmetic operations with precision handling
        - algebra: Algebraic operations and equation solving
        - calculus: Differentiation and integration utilities
        - statistics: Statistical functions and distributions

    Geometry:
        - shapes2d: Two-dimensional geometric shapes and operations
        - shapes3d: Three-dimensional geometric shapes and operations
        - transforms: Geometric transformations (rotation, scaling, etc.)
        - spatial: Spatial algorithms and computational geometry

    Precision:
        - comparison: Safe floating-point comparisons
        - rounding: Robust rounding with configurable precision

    Utilities:
        - validation: Input validation and type checking
        - logging: Structured logging configuration

Features:
    - Robust floating-point precision handling
    - Comprehensive geometric primitives
    - Fast numerical operations
    - Beautiful CLI interface with Rich
    - Type-safe with full type hints
    - Extensive test coverage (>90%)

Usage:
    >>> import gatormath as gm
    >>> from gatormath.core import arithmetic
    >>> from gatormath.geometry import shapes2d
    >>>
    >>> # Safe floating-point comparison
    >>> gm.precision.comparison.is_close(0.1 + 0.2, 0.3)
    True
    >>>
    >>> # Geometric operations
    >>> circle = shapes2d.Circle(radius=5.0)
    >>> circle.area()
    78.53981633974483

Examples:
    Basic arithmetic with precision:
    >>> from gatormath.core import arithmetic
    >>> result = arithmetic.safe_add(0.1, 0.2)
    >>> arithmetic.is_effectively_equal(result, 0.3)
    True

    Geometric calculations:
    >>> from gatormath.geometry import shapes2d
    >>> triangle = shapes2d.Triangle(a=3.0, b=4.0, c=5.0)
    >>> triangle.area()
    6.0
    >>> triangle.is_right_triangle()
    True

    CLI usage:
    $ gatormath calculate --expr "sqrt(144)"
    $ gatormath geometry circle --radius 10 --show-area

Installation:
    pip install gatormath

    # With all optional dependencies
    pip install gatormath[all]

    # Development installation
    pip install -e ".[dev]"

Documentation:
    Full documentation available at: https://gatormath.readthedocs.io

Notes:
    - All floating-point operations use configurable epsilon for comparisons
    - Default epsilon: 1e-9 (can be adjusted via precision.config)
    - Geometric operations handle degenerate cases gracefully
    - CLI uses Rich library for beautiful terminal output

References:
    [1] IEEE 754 Floating-Point Arithmetic Standard
    [2] Computational Geometry: Algorithms and Applications
        (de Berg, Cheong, van Kreveld, Overmars)

See Also:
    - numpy: For array-based numerical computing
    - scipy: For scientific computing
    - sympy: For symbolic mathematics
"""

# Standard library imports
import sys
from typing import Final


# Version information
__version__: Final[str] = "0.1.0"
__author__: Final[str] = "GatorMath Development Team"
__license__: Final[str] = "MIT"
__copyright__: Final[str] = "Copyright 2025 GatorMath Development Team"


# Package metadata
__all__: list[str] = [
    # Version info
    "__version__",
    "__author__",
    "__license__",
    "__copyright__",
    # Submodules (imported on-demand)
    "core",
    "geometry",
    "precision",
    "cli",
    "utils",
]


# Python version check
if sys.version_info < (3, 9):
    raise RuntimeError(
        f"GatorMath requires Python 3.9 or later. "
        f"Current version: {sys.version_info.major}.{sys.version_info.minor}"
    )


def get_version() -> str:
    """
    Get the current version of GatorMath.

    Returns:
        str: Version string in format "MAJOR.MINOR.PATCH"

    Examples:
        >>> import gatormath
        >>> gatormath.get_version()
        '0.1.0'
    """
    return __version__


def get_info() -> dict[str, str]:
    """
    Get comprehensive package information.

    Returns:
        dict[str, str]: Dictionary containing package metadata including
            version, author, license, copyright, and Python version.

    Examples:
        >>> import gatormath
        >>> info = gatormath.get_info()
        >>> info['version']
        '0.1.0'
        >>> info['license']
        'MIT'
    """
    return {
        "version": __version__,
        "author": __author__,
        "license": __license__,
        "copyright": __copyright__,
        "python_version": f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}",
        "python_implementation": sys.implementation.name,
    }


# Lazy imports for performance
# Submodules are imported on first access to reduce startup time
def __getattr__(name: str) -> object:
    """
    Lazy import mechanism for submodules.

    This function enables importing submodules only when they are accessed,
    reducing initial import time and memory footprint.

    Args:
        name (str): Name of the attribute/module being accessed

    Returns:
        object: The requested module or attribute

    Raises:
        AttributeError: If the requested attribute/module doesn't exist

    Notes:
        This is automatically called by Python when an attribute is not
        found in the module's __dict__. It enables lazy loading of heavy
        submodules.
    """
    if name in __all__:
        import importlib

        # Import the requested submodule
        module = importlib.import_module(f".{name}", __name__)
        # Cache it in globals to avoid repeated imports
        globals()[name] = module
        return module

    raise AttributeError(f"module '{__name__}' has no attribute '{name}'")


# Configure module-level exports for better IDE support
if __name__ != "__main__":
    # Type stubs for lazy imports (helps IDEs with autocomplete)
    from typing import TYPE_CHECKING

    if TYPE_CHECKING:
        from gatormath import cli as cli
        from gatormath import core as core
        from gatormath import geometry as geometry
        from gatormath import precision as precision
        from gatormath import utils as utils
