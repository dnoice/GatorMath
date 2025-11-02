"""
Module Name: gatormath

Description:
    GatorMath - A comprehensive math and geometry Python toolkit with bite.

    GatorMath provides robust mathematical operations, geometric calculations,
    floating-point precision handling, a beautiful CLI interface, and an
    interactive Flask web application. All operations handle edge cases, check
    for overflow, and manage floating-point precision issues.

Module Path: gatormath/__init__.py
Package: gatormath

Author: GatorMath Development Team
Created: 2025-11-02
Modified: 2025-11-02
Version: 0.1.0

Modules:
    - core: Mathematical operations (arithmetic, algebra, calculus, statistics)
    - geometry: Geometric shapes and algorithms (2D and 3D)
    - precision: Floating-point precision handling
    - cli: Command-line interface with Rich theming
    - web: Flask web application with interactive visualizations
    - utils: Utility functions

Exports:
    - __version__: Package version string
    - __author__: Author information
    - __license__: License type

Examples:
    >>> import gatormath
    >>> print(gatormath.__version__)
    0.1.0

    >>> from gatormath.core import arithmetic
    >>> arithmetic.safe_add(0.1, 0.2)
    0.3

    >>> from gatormath.geometry import shapes2d
    >>> circle = shapes2d.Circle(radius=5.0)
    >>> circle.area()
    78.53981633974483

CLI Usage:
    $ gatormath --help
    $ gatormath calculate "sqrt(144)"
    $ gatormath geometry circle --radius 10
    $ gatormath serve  # Launch Flask web application

Design Principles:
    1. Robustness: All code handles edge cases and floating-point issues
    2. Comprehensiveness: No half-implementations; production-ready only
    3. Beauty: CLI and web output are intuitive and visually appealing
    4. Documentation: Complete docstrings with metadata for every artifact
    5. Cohesiveness: Unified branding, theming, and user experience

Brand Colors:
    - Gator Green (#2D5016): Primary branding, success
    - Deep Teal (#0D7377): Interactive elements
    - Golden Yellow (#F4D35E): Information
    - Sunset Orange (#FF8C42): Warnings
    - Blood Red (#C1292E): Errors

References:
    [1] IEEE 754 Standard for Floating-Point Arithmetic
    [2] Python Enhancement Proposals (PEP 8, PEP 257, PEP 484)

Notes:
    Requires Python 3.9+ for full functionality
    All public APIs are type-hinted and mypy-compliant
"""

__version__ = "0.1.0"
__author__ = "GatorMath Development Team"
__license__ = "MIT"
__all__ = ["__version__", "__author__", "__license__"]

# Package metadata
__title__ = "gatormath"
__description__ = "Mathematical precision with bite"
__url__ = "https://github.com/dnoice/GatorMath"
