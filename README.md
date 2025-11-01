# GatorMath

**Mathematical precision with bite** 🐊

A comprehensive math and geometry Python toolkit that refuses to be boring and actually gets work done. Clean APIs, fast numerics, robust geometry handling, and a beautiful CLI interface with Rich theming.

[![Python Version](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

---

## Features

### 🔢 **Safe Arithmetic**
- Overflow and underflow detection
- Division by zero handling
- Precision-aware operations
- Support for Decimal arithmetic

### 📐 **Robust Geometry**
- 2D shapes (Circle, Rectangle, Square, Triangle)
- Comprehensive area/perimeter calculations
- Degenerate case handling
- Floating-point precision management

### ✨ **Precision Handling**
- Safe floating-point comparisons
- Configurable epsilon tolerance
- Handles classic precision issues (0.1 + 0.2 == 0.3)
- NaN and infinity aware

### 🎨 **Beautiful CLI**
- Rich-themed interface with brand colors
- Interactive commands and demos
- Progress indicators and tables
- Syntax highlighting for code/math

---

## Installation

### From Source

```bash
# Clone the repository
git clone https://github.com/dnoice/GatorMath.git
cd GatorMath

# Install in development mode
pip install -e .

# Or install with all dependencies
pip install -e ".[all]"
```

### Dependencies

**Core:**
- Python 3.9+
- numpy
- rich (CLI theming)
- typer (CLI framework)

**Development:**
- pytest (testing)
- black (formatting)
- mypy (type checking)
- ruff (linting)

---

## Quick Start

### Python API

```python
# Safe arithmetic operations
from gatormath.core import arithmetic

result = arithmetic.safe_add(0.1, 0.2)
print(f"0.1 + 0.2 = {result}")

# Geometric calculations
from gatormath.geometry import shapes2d

circle = shapes2d.Circle(radius=10.0)
print(f"Circle area: {circle.area():.4f}")

triangle = shapes2d.Triangle(a=3.0, b=4.0, c=5.0)
print(f"Triangle area: {triangle.area()}")
print(f"Is right triangle: {triangle.is_right_triangle()}")

# Precision handling
from gatormath.precision import is_close

print(is_close(0.1 + 0.2, 0.3))  # True
```

### Command-Line Interface

```bash
# Get package info
gatormath info

# Mathematical calculations
gatormath calculate "sqrt(144)"
gatormath calculate "factorial(5)"
gatormath calculate "gcd(48, 18)"

# Geometric calculations
gatormath geometry circle --radius 10
gatormath geometry triangle --a 3 --b 4 --c 5

# Precision demonstration
gatormath precision

# Interactive demo
gatormath demo
```

---

## Documentation

### Project Structure

```
GatorMath/
├── gatormath/              # Main package
│   ├── core/              # Mathematical operations
│   │   └── arithmetic.py  # Safe arithmetic
│   ├── geometry/          # Geometric shapes
│   │   └── shapes2d.py    # 2D shapes
│   ├── precision/         # Precision handling
│   │   └── comparison.py  # Safe comparisons
│   ├── cli/               # CLI interface
│   │   ├── app.py        # Main CLI app
│   │   └── theme.py      # Rich theming
│   └── utils/            # Utilities
├── tests/                # Test suite
├── examples/             # Usage examples
├── docs/                 # Documentation
│   └── branding/        # Brand assets
├── STANDARDS.md         # Project standards
└── pyproject.toml       # Project configuration
```

### Core Modules

#### `gatormath.core.arithmetic`

Safe arithmetic operations with overflow detection:

```python
from gatormath.core import arithmetic

# Basic operations
arithmetic.safe_add(a, b)
arithmetic.safe_subtract(a, b)
arithmetic.safe_multiply(a, b)
arithmetic.safe_divide(a, b)
arithmetic.safe_power(base, exponent)
arithmetic.safe_sqrt(value)
arithmetic.safe_mod(a, b)

# Utilities
arithmetic.clamp(value, min_val, max_val)
arithmetic.sign(value)
arithmetic.factorial(n)
arithmetic.gcd(a, b)
arithmetic.lcm(a, b)
```

#### `gatormath.geometry.shapes2d`

2D geometric shapes:

```python
from gatormath.geometry import shapes2d

# Create shapes
circle = shapes2d.Circle(radius=5.0)
rect = shapes2d.Rectangle(width=4.0, height=3.0)
square = shapes2d.Square(side=5.0)
triangle = shapes2d.Triangle(a=3.0, b=4.0, c=5.0)

# Calculate properties
circle.area()
circle.circumference()
rect.perimeter()
rect.diagonal()
triangle.is_right_triangle()
triangle.triangle_type()  # "equilateral", "isosceles", or "scalene"
```

#### `gatormath.precision.comparison`

Safe floating-point comparisons:

```python
from gatormath.precision import is_close, is_zero, compare

# Comparison with tolerance
is_close(0.1 + 0.2, 0.3)  # True
is_zero(1e-15)  # True

# Three-way comparison
compare(5.0, 3.0)  # Returns 1 (greater)
compare(3.0, 5.0)  # Returns -1 (less)
compare(3.0, 3.0000001)  # Returns 0 (equal within tolerance)
```

---

## Design Principles

### 1. **Robustness**
All operations handle edge cases, check for overflow, and manage floating-point precision issues.

### 2. **Comprehensive Documentation**
Every module, class, and function includes detailed docstrings with:
- Description and purpose
- Mathematical formulas (where applicable)
- Algorithm complexity
- Precision notes
- Examples
- References

### 3. **Type Safety**
Full type hints throughout the codebase, verified with mypy.

### 4. **Beautiful UX**
CLI uses Rich library with custom GatorMath theme:
- Swamp Green (#2D5016) - Primary brand
- Deep Teal (#0D7377) - Interactive elements
- Golden Yellow (#F4D35E) - Information
- Sunset Orange (#FF8C42) - Warnings
- Blood Red (#C1292E) - Errors

### 5. **No Lazy Implementations**
Production-ready code with proper error handling, validation, and comprehensive test coverage.

---

## Testing

Run the test suite:

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=gatormath --cov-report=html

# Run specific test file
pytest tests/test_core/test_arithmetic.py

# Run with verbose output
pytest -v
```

Current test coverage: **>90%**

---

## Development

### Setup Development Environment

```bash
# Install development dependencies
pip install -e ".[dev]"

# Run code formatters
black gatormath tests
isort gatormath tests

# Run linters
ruff gatormath tests
mypy gatormath

# Run all quality checks
pytest && black --check gatormath && ruff gatormath && mypy gatormath
```

### Code Standards

See [STANDARDS.md](STANDARDS.md) for complete coding standards, including:
- Branding and color schemes
- Documentation templates
- Testing requirements
- Git workflow
- Module structure

---

## Examples

See the [examples/](examples/) directory for comprehensive usage examples:

- `basic_usage.py` - Fundamental operations and patterns

Run examples:

```bash
python examples/basic_usage.py
```

---

## Contributing

Contributions welcome! Please:

1. Read [STANDARDS.md](STANDARDS.md) for coding standards
2. Write comprehensive tests for new features
3. Include detailed docstrings with metadata
4. Follow the established branding and theming
5. Ensure all tests pass and coverage remains >90%

---

## License

MIT License - see [LICENSE](LICENSE) file for details.

---

## Roadmap

### Version 0.2.0
- [ ] 3D geometry module
- [ ] Matrix operations
- [ ] Symbolic mathematics integration
- [ ] Visualization with matplotlib/plotly

### Version 0.3.0
- [ ] Advanced calculus operations
- [ ] Statistical distributions
- [ ] Optimization algorithms
- [ ] Performance benchmarks

---

## Credits

**GatorMath Development Team**

Built with:
- [Rich](https://github.com/Textualize/rich) - Beautiful terminal output
- [Typer](https://github.com/tiangolo/typer) - Modern CLI framework
- [NumPy](https://numpy.org/) - Numerical computing
- [pytest](https://pytest.org/) - Testing framework

---

**Chomp chomp.** 🐊
