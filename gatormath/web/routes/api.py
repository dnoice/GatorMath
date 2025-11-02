"""
File Name: api.py
File Path: gatormath/web/routes/api.py
Module Name: api

Description:
    REST API endpoints exposing GatorMath Python functions to the frontend.
    Provides JSON API for arithmetic, geometry, and precision operations.

Module Path: gatormath/web/routes/api.py
Package: gatormath.web.routes

Author: Dennis 'dnoice' Smaltz
AI Acknowledgement: Claude Code
Created: 2025-11-02
Modified: 2025-11-02
Version: 0.1.0

Dependencies:
    - flask: Flask framework
    - gatormath.core.arithmetic: Arithmetic operations
    - gatormath.geometry.shapes2d: Geometric shapes
    - gatormath.precision.comparison: Precision utilities

Exports:
    - bp: Flask Blueprint for API routes

API Endpoints:
    POST /api/arithmetic/add - Add two numbers
    POST /api/arithmetic/multiply - Multiply two numbers
    POST /api/arithmetic/divide - Divide two numbers
    POST /api/arithmetic/sqrt - Square root
    POST /api/arithmetic/factorial - Factorial
    POST /api/geometry/circle - Circle calculations
    POST /api/geometry/triangle - Triangle calculations
    POST /api/precision/compare - Precision comparison

Request Format:
    JSON with operation-specific parameters

Response Format:
    JSON with result or error message

Examples:
    POST /api/arithmetic/add
    {"a": 0.1, "b": 0.2}
    -> {"result": 0.3}

    POST /api/geometry/circle
    {"radius": 5.0}
    -> {"area": 78.54, "circumference": 31.42}

Error Handling:
    Returns JSON with error message and appropriate HTTP status code

Version: 0.1.0
"""

from flask import Blueprint, jsonify, request

from gatormath.core import arithmetic
from gatormath.geometry import shapes2d
from gatormath.precision import comparison

bp = Blueprint("api", __name__)


# ===== ARITHMETIC ENDPOINTS =====

@bp.route("/arithmetic/add", methods=["POST"])
def add():
    """
    Add two numbers.

    Request JSON:
        {
            "a": float,
            "b": float
        }

    Response JSON:
        {
            "result": float
        }

    Examples:
        POST /api/arithmetic/add
        {"a": 0.1, "b": 0.2}
        -> {"result": 0.3}

    Version: 0.1.0
    """
    try:
        data = request.get_json()
        a = float(data["a"])
        b = float(data["b"])
        result = arithmetic.safe_add(a, b)
        return jsonify({"result": result})
    except (KeyError, TypeError, ValueError) as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@bp.route("/arithmetic/multiply", methods=["POST"])
def multiply():
    """Multiply two numbers."""
    try:
        data = request.get_json()
        a = float(data["a"])
        b = float(data["b"])
        result = arithmetic.safe_multiply(a, b)
        return jsonify({"result": result})
    except (KeyError, TypeError, ValueError) as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@bp.route("/arithmetic/divide", methods=["POST"])
def divide():
    """Divide two numbers."""
    try:
        data = request.get_json()
        a = float(data["a"])
        b = float(data["b"])
        result = arithmetic.safe_divide(a, b)
        return jsonify({"result": result})
    except (KeyError, TypeError, ValueError, ZeroDivisionError) as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@bp.route("/arithmetic/sqrt", methods=["POST"])
def sqrt():
    """Calculate square root."""
    try:
        data = request.get_json()
        value = float(data["value"])
        result = arithmetic.safe_sqrt(value)
        return jsonify({"result": result})
    except (KeyError, TypeError, ValueError) as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@bp.route("/arithmetic/factorial", methods=["POST"])
def factorial():
    """Calculate factorial."""
    try:
        data = request.get_json()
        n = int(data["n"])
        result = arithmetic.factorial(n)
        return jsonify({"result": result})
    except (KeyError, TypeError, ValueError) as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@bp.route("/arithmetic/gcd", methods=["POST"])
def gcd():
    """Calculate greatest common divisor."""
    try:
        data = request.get_json()
        a = int(data["a"])
        b = int(data["b"])
        result = arithmetic.gcd(a, b)
        return jsonify({"result": result})
    except (KeyError, TypeError, ValueError) as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# ===== GEOMETRY ENDPOINTS =====

@bp.route("/geometry/circle", methods=["POST"])
def circle():
    """
    Calculate circle properties.

    Request JSON:
        {
            "radius": float
        }

    Response JSON:
        {
            "area": float,
            "circumference": float,
            "diameter": float
        }

    Examples:
        POST /api/geometry/circle
        {"radius": 5.0}
        -> {"area": 78.54, "circumference": 31.42, "diameter": 10.0}

    Version: 0.1.0
    """
    try:
        data = request.get_json()
        radius = float(data["radius"])
        c = shapes2d.Circle(radius=radius)
        return jsonify({
            "area": c.area(),
            "circumference": c.circumference(),
            "diameter": c.diameter()
        })
    except (KeyError, TypeError, ValueError) as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@bp.route("/geometry/rectangle", methods=["POST"])
def rectangle():
    """Calculate rectangle properties."""
    try:
        data = request.get_json()
        width = float(data["width"])
        height = float(data["height"])
        r = shapes2d.Rectangle(width=width, height=height)
        return jsonify({
            "area": r.area(),
            "perimeter": r.perimeter(),
            "diagonal": r.diagonal(),
            "is_square": r.is_square()
        })
    except (KeyError, TypeError, ValueError) as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@bp.route("/geometry/triangle", methods=["POST"])
def triangle():
    """
    Calculate triangle properties.

    Request JSON:
        {
            "a": float,
            "b": float,
            "c": float
        }

    Response JSON:
        {
            "area": float,
            "perimeter": float,
            "is_right_triangle": bool,
            "triangle_type": str
        }

    Version: 0.1.0
    """
    try:
        data = request.get_json()
        a = float(data["a"])
        b = float(data["b"])
        c = float(data["c"])
        t = shapes2d.Triangle(a=a, b=b, c=c)
        return jsonify({
            "area": t.area(),
            "perimeter": t.perimeter(),
            "is_right_triangle": t.is_right_triangle(),
            "triangle_type": t.triangle_type()
        })
    except (KeyError, TypeError, ValueError) as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# ===== PRECISION ENDPOINTS =====

@bp.route("/precision/compare", methods=["POST"])
def compare():
    """
    Compare two numbers with tolerance.

    Request JSON:
        {
            "a": float,
            "b": float,
            "tolerance": float (optional)
        }

    Response JSON:
        {
            "result": int (-1, 0, or 1),
            "is_close": bool
        }

    Version: 0.1.0
    """
    try:
        data = request.get_json()
        a = float(data["a"])
        b = float(data["b"])
        tolerance = float(data.get("tolerance", 1e-9))

        result = comparison.compare(a, b, tolerance=tolerance)
        is_close = comparison.is_close(a, b, abs_tol=tolerance, rel_tol=tolerance)

        return jsonify({
            "result": result,
            "is_close": is_close
        })
    except (KeyError, TypeError, ValueError) as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500
