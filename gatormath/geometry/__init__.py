"""
Module Name: gatormath.geometry

Description:
    Geometric shapes and algorithms module providing comprehensive 2D and 3D
    shape classes with area, perimeter, volume calculations, and spatial
    algorithms.

Module Path: gatormath/geometry/__init__.py
Package: gatormath.geometry

Author: Dennis 'dnoice' Smaltz
AI Acknowledgement: Claude Code
Created: 2025-11-02
Modified: 2025-11-02
Version: 0.1.0

Submodules:
    - shapes2d: 2D geometric shapes (Circle, Rectangle, Square, Triangle)
    - shapes3d: 3D geometric shapes (future)
    - transforms: Geometric transformations (future)
    - spatial: Spatial algorithms (future)

Exports:
    All classes from shapes2d module for convenience

Notes:
    All shapes handle degenerate cases and floating-point precision issues
    Follows mathematical conventions for geometric calculations
"""

from gatormath.geometry import shapes2d

__all__ = ["shapes2d"]
