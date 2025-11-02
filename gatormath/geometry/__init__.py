"""
Metadata:
    Project: GatorMath
    File Name: __init__.py
    File Path: gatormath/geometry/__init__.py
    Module: Geometry Package
    Created: 2025-11-02
    Modified: 2025-11-02
    Version: 0.1.0
    Author: Dennis 'dnoice' Smaltz
    AI Acknowledgement: Claude Code

Description:
    Geometric shapes and algorithms module providing comprehensive 2D and 3D
    shape classes with area, perimeter, volume calculations, and spatial
    algorithms.

Usage:
    >>> from gatormath.geometry import shapes2d
    >>> circle = shapes2d.Circle(radius=5.0)
    >>> circle.area()
    78.53981633974483

Contents:
    Submodules:
        - shapes2d: 2D geometric shapes (Circle, Rectangle, Square, Triangle)
        - shapes3d: 3D geometric shapes (future)
        - transforms: Geometric transformations (future)
        - spatial: Spatial algorithms (future)

    Exports:
        - shapes2d: 2D shapes module

Dependencies:
    - gatormath.geometry.shapes2d: 2D shape classes

Notes:
    All shapes handle degenerate cases and floating-point precision issues
    Follows mathematical conventions for geometric calculations
"""

from gatormath.geometry import shapes2d

__all__ = ["shapes2d"]
