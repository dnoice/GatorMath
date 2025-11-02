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
- rich (CLI theming)
- typer (CLI framework)
- flask (Web framework)
- flask-cors (CORS support)

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

# Display version
gatormath version

# Launch Flask web server
gatormath serve
gatormath serve --port 8000
gatormath serve --debug
```

---

## Documentation

### Project Structure

```
GatorMath/
├── gatormath/                          # Python package (backend)
│   ├── __init__.py                     # Package initialization
│   ├── core/                           # Mathematical operations
│   │   ├── __init__.py                 # Core package init
│   │   └── arithmetic.py               # Safe arithmetic operations
│   ├── geometry/                       # Geometric shapes & algorithms
│   │   ├── __init__.py                 # Geometry package init
│   │   └── shapes2d.py                 # 2D shapes (Circle, Triangle, etc.)
│   ├── precision/                      # Floating-point precision
│   │   ├── __init__.py                 # Precision package init
│   │   └── comparison.py               # Safe comparisons
│   ├── cli/                            # CLI interface with Rich theming
│   │   ├── __init__.py                 # CLI package init
│   │   └── app.py                      # Main Typer CLI application
│   ├── web/                            # Flask web application
│   │   ├── __init__.py                 # Web package init
│   │   ├── app.py                      # Flask application factory
│   │   ├── routes/                     # API and page routes
│   │   │   ├── __init__.py             # Routes package init
│   │   │   ├── api.py                  # REST API endpoints
│   │   │   └── pages.py                # Page routes
│   │   ├── static/                     # Frontend assets
│   │   │   ├── css/                    # Modular stylesheets
│   │   │   │   ├── base.css            # CSS variables, resets, animations
│   │   │   │   ├── layout.css          # Navigation, sections, grids
│   │   │   │   ├── components.css      # Buttons, cards, calculators
│   │   │   │   ├── playground.css      # Interactive canvas styles
│   │   │   │   └── responsive.css      # Media queries
│   │   │   └── js/                     # Modular JavaScript
│   │   │       ├── utils.js            # Shared utilities
│   │   │       ├── three-background.js # 3D background animation
│   │   │       ├── animations.js       # GSAP scroll animations
│   │   │       ├── vector-canvas.js    # Vector operations playground
│   │   │       ├── bezier-canvas.js    # Bezier curve editor
│   │   │       ├── matrix-canvas.js    # Matrix transformations
│   │   │       ├── triangle-canvas.js  # Triangle calculator
│   │   │       ├── calculators.js      # Live calculators
│   │   │       ├── code-playground.js  # Interactive code editor
│   │   │       └── init.js             # Initialization coordinator
│   │   └── templates/                  # Jinja2 templates
│   │       └── index.html              # Main web interface
│   └── utils/                          # Utility functions
│       └── __init__.py                 # Utils package init
├── pyproject.toml                      # Python project configuration
├── README.md                           # This file
└── LICENSE                             # MIT License
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

### Interactive Frontend

GatorMath includes a beautiful, interactive web interface showcasing mathematical concepts:

#### Features
- **Vector Operations Playground**: Drag vectors to see dot products, cross products, and transformations in real-time
- **Bezier Curve Editor**: Interactive control points with animated point traversal
- **Matrix Transformations**: Live visualization of rotation and scaling operations
- **Triangle Calculator**: Drag vertices to calculate area, perimeter, and angles dynamically
- **Live Calculators**: Distance, circle properties, angle conversion, vector projection, matrix determinants, quadratic roots
- **Code Playground**: Interactive JavaScript console for experimenting with math operations
- **3D Background**: Animated Three.js particle grid that responds to mouse movement

#### Frontend Architecture
- **Modular CSS**: Separation of concerns (base, layout, components, playground, responsive)
- **Modular JavaScript**: Each feature in its own file with clear dependencies
- **Modern Stack**: Three.js for 3D graphics, GSAP for smooth animations
- **Responsive Design**: Fully responsive from mobile to 4K displays

Access the web interface via Flask:
```bash
# Using the GatorMath CLI
gatormath serve

# Or directly with Python
python -m gatormath.web.app

# Navigate to http://localhost:5000
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

Tests coming soon! We aim for comprehensive test coverage with:
- Unit tests for all core modules
- Integration tests for web endpoints
- Property-based testing with hypothesis
- Performance benchmarks

Target coverage: **>90%**

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

All code follows these standards:
- **Documentation**: Every file has standardized metadata docstrings
- **Branding**: Gator Green (#00A676) and Swamp Gold (#F2C94C) color scheme
- **Type Safety**: Full type hints throughout
- **Testing**: Comprehensive test coverage (target >90%)
- **Formatting**: Black for Python, consistent style for CSS/JS

---

## Examples

Examples coming soon! Will include:
- Basic arithmetic and geometry operations
- Precision handling demonstrations
- CLI usage patterns
- Web API integration examples

---

## Contributing

Contributions welcome! Please:

1. Follow the established coding standards and documentation format
2. Write comprehensive tests for new features
3. Include detailed docstrings with standardized metadata
4. Follow the GatorMath branding (Gator Green, Swamp Gold)
5. Ensure code is properly formatted and type-hinted

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
- [Flask](https://flask.palletsprojects.com/) - Web framework
- [Rich](https://github.com/Textualize/rich) - Beautiful terminal output
- [Typer](https://github.com/tiangolo/typer) - Modern CLI framework
- [Three.js](https://threejs.org/) - 3D graphics
- [GSAP](https://greensock.com/gsap/) - Animation library

---

**Chomp chomp.** 🐊
