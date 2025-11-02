# GatorMath API Documentation

**Version:** 0.1.0
**Last Updated:** 2025-11-02
**Document Path:** `/docs/API_DOCS.md`

---

## Table of Contents

1. [Overview](#overview)
2. [Python API](#python-api)
   - [Core Arithmetic](#core-arithmetic)
   - [Precision Comparison](#precision-comparison)
   - [Geometry Shapes2D](#geometry-shapes2d)
3. [REST API](#rest-api)
   - [Arithmetic Endpoints](#arithmetic-endpoints)
   - [Geometry Endpoints](#geometry-endpoints)
   - [Precision Endpoints](#precision-endpoints)
4. [Error Handling](#error-handling)
5. [Examples](#examples)

---

## Overview

GatorMath provides two API interfaces:

1. **Python API**: Import and use directly in Python code
2. **REST API**: HTTP endpoints for web applications and external clients

Both APIs provide the same mathematical operations with consistent error handling and precision management.

---

## Python API

### Core Arithmetic

**Module:** `gatormath.core.arithmetic`

#### Functions

**safe_add(a, b) → float**
- Add two numbers with overflow checking
- **Example:** `arithmetic.safe_add(0.1, 0.2)` → `0.3`

**safe_subtract(a, b) → float**
- Subtract two numbers
- **Example:** `arithmetic.safe_subtract(5.0, 3.0)` → `2.0`

**safe_multiply(a, b) → float**
- Multiply two numbers
- **Example:** `arithmetic.safe_multiply(3.0, 4.0)` → `12.0`

**safe_divide(a, b) → float**
- Divide with zero checking
- **Raises:** `ZeroDivisionError` if b == 0

**safe_power(base, exponent) → float**
- Exponentiation
- **Example:** `arithmetic.safe_power(2.0, 3.0)` → `8.0`

**safe_sqrt(value) → float**
- Square root with negative checking
- **Example:** `arithmetic.safe_sqrt(16.0)` → `4.0`

**safe_mod(a, b) → float**
- Modulo operation
- **Example:** `arithmetic.safe_mod(10.0, 3.0)` → `1.0`

**factorial(n) → int**
- Factorial (n!)
- **Example:** `arithmetic.factorial(5)` → `120`
- **Complexity:** O(n)

**gcd(a, b) → int**
- Greatest common divisor
- **Example:** `arithmetic.gcd(48, 18)` → `6`
- **Complexity:** O(log(min(a, b)))

**lcm(a, b) → int**
- Least common multiple
- **Example:** `arithmetic.lcm(12, 18)` → `36`

**clamp(value, min_val, max_val) → float**
- Clamp value between bounds
- **Example:** `arithmetic.clamp(15.0, 0.0, 10.0)` → `10.0`

**sign(value) → int**
- Return -1, 0, or 1
- **Example:** `arithmetic.sign(5.0)` → `1`

---

### Precision Comparison

**Module:** `gatormath.precision.comparison`

**is_close(a, b, rel_tol=1e-9, abs_tol=1e-9) → bool**
- Check if two numbers are approximately equal
- **Example:** `comparison.is_close(0.1 + 0.2, 0.3)` → `True`
- **Solves:** Classic 0.1 + 0.2 != 0.3 problem

**is_zero(value, tolerance=1e-9) → bool**
- Check if approximately zero
- **Example:** `comparison.is_zero(1e-15)` → `True`

**compare(a, b, tolerance=1e-9) → int**
- Three-way comparison (-1, 0, 1)
- **Example:** `comparison.compare(5.0, 3.0)` → `1`

---

### Geometry Shapes2D

**Module:** `gatormath.geometry.shapes2d`

#### Circle(radius)

```python
circle = shapes2d.Circle(radius=5.0)
circle.area()          # 78.54
circle.circumference() # 31.42
circle.diameter()      # 10.0
```

**Methods:**
- `area()` → float: πr²
- `circumference()` → float: 2πr
- `diameter()` → float: 2r

---

#### Rectangle(width, height)

```python
rect = shapes2d.Rectangle(width=4.0, height=3.0)
rect.area()       # 12.0
rect.perimeter()  # 14.0
rect.diagonal()   # 5.0
rect.is_square()  # False
```

**Methods:**
- `area()` → float: width × height
- `perimeter()` → float: 2(width + height)
- `diagonal()` → float: √(width² + height²)
- `is_square()` → bool

---

#### Square(side)

```python
square = shapes2d.Square(side=5.0)
square.area()       # 25.0
square.perimeter()  # 20.0
square.diagonal()   # 7.07
```

---

#### Triangle(a, b, c)

```python
triangle = shapes2d.Triangle(a=3.0, b=4.0, c=5.0)
triangle.area()               # 6.0 (Heron's formula)
triangle.perimeter()          # 12.0
triangle.is_right_triangle()  # True
triangle.is_equilateral()     # False
triangle.is_isosceles()       # False
triangle.triangle_type()      # 'scalene'
```

**Methods:**
- `area()` → float: Heron's formula
- `perimeter()` → float
- `is_right_triangle()` → bool: Pythagorean check
- `is_equilateral()` → bool: All sides equal
- `is_isosceles()` → bool: Two sides equal
- `triangle_type()` → str: "equilateral", "isosceles", or "scalene"

---

## REST API

**Base URL:** `http://localhost:5000/api`

All endpoints accept JSON and return JSON.

### Arithmetic Endpoints

#### POST /api/arithmetic/add
```json
Request:  {"a": 0.1, "b": 0.2}
Response: {"result": 0.3}
```

#### POST /api/arithmetic/multiply
```json
Request:  {"a": 3.0, "b": 4.0}
Response: {"result": 12.0}
```

#### POST /api/arithmetic/divide
```json
Request:  {"a": 10.0, "b": 2.0}
Response: {"result": 5.0}
```

#### POST /api/arithmetic/sqrt
```json
Request:  {"value": 16.0}
Response: {"result": 4.0}
```

#### POST /api/arithmetic/factorial
```json
Request:  {"n": 5}
Response: {"result": 120}
```

#### POST /api/arithmetic/gcd
```json
Request:  {"a": 48, "b": 18}
Response: {"result": 6}
```

---

### Geometry Endpoints

#### POST /api/geometry/circle
```json
Request:  {"radius": 5.0}
Response: {
  "area": 78.54,
  "circumference": 31.42,
  "diameter": 10.0
}
```

#### POST /api/geometry/rectangle
```json
Request:  {"width": 4.0, "height": 3.0}
Response: {
  "area": 12.0,
  "perimeter": 14.0,
  "diagonal": 5.0,
  "is_square": false
}
```

#### POST /api/geometry/triangle
```json
Request:  {"a": 3.0, "b": 4.0, "c": 5.0}
Response: {
  "area": 6.0,
  "perimeter": 12.0,
  "is_right_triangle": true,
  "triangle_type": "scalene"
}
```

---

### Precision Endpoints

#### POST /api/precision/compare
```json
Request:  {"a": 0.1, "b": 0.2, "tolerance": 1e-9}
Response: {"result": -1, "is_close": false}
```

---

## Error Handling

### Python Exceptions

- `ValueError`: Invalid inputs, NaN values, negative where positive required
- `ZeroDivisionError`: Division/modulo by zero
- `OverflowError`: Result exceeds float range

### REST API Errors

**400 Bad Request:**
```json
{"error": "Error message"}
```

**500 Internal Server Error:**
```json
{"error": "Internal server error"}
```

---

## Examples

### Python Usage

```python
from gatormath.core import arithmetic
from gatormath.geometry import shapes2d
from gatormath.precision import comparison

# Safe arithmetic
result = arithmetic.safe_add(0.1, 0.2)

# Precision comparison
if comparison.is_close(0.1 + 0.2, 0.3):
    print("Math works!")

# Geometry
circle = shapes2d.Circle(radius=5.0)
print(f"Area: {circle.area()}")

triangle = shapes2d.Triangle(a=3.0, b=4.0, c=5.0)
print(f"Type: {triangle.triangle_type()}")
```

### JavaScript (Fetch API)

```javascript
async function calculateArea(radius) {
    const response = await fetch('http://localhost:5000/api/geometry/circle', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ radius })
    });
    const data = await response.json();
    return data.area;
}
```

### Python (requests)

```python
import requests

response = requests.post(
    'http://localhost:5000/api/arithmetic/factorial',
    json={'n': 10}
)
print(response.json()['result'])
```

---

**Version:** 0.1.0
**See Also:** [CLI Docs](CLI_DOCS.md) | [Development Guide](DEVELOPMENT.md) | [Standards](STANDARDS.md)
