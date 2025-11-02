# GatorMath Development Guide

**Version:** 0.1.0
**Last Updated:** 2025-11-02
**Document Path:** `/docs/DEVELOPMENT.md`

---

## Table of Contents

1. [Getting Started](#getting-started)
2. [Development Environment](#development-environment)
3. [Project Structure](#project-structure)
4. [Development Workflow](#development-workflow)
5. [Testing](#testing)
6. [Code Style](#code-style)
7. [Documentation](#documentation)
8. [Git Workflow](#git-workflow)
9. [Release Process](#release-process)
10. [Troubleshooting](#troubleshooting)

---

## Getting Started

### Prerequisites

**Required:**
- Python 3.9 or higher
- Git
- pip package manager

**Recommended:**
- Virtual environment tool (venv, virtualenv, conda)
- Code editor with Python support (VSCode, PyCharm)
- Modern web browser (Chrome, Firefox, Safari)

### Quick Start

```bash
# Clone repository
git clone https://github.com/dnoice/GatorMath.git
cd GatorMath

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install development dependencies
pip install -e ".[dev]"

# Run tests
pytest

# Start development server
gatormath serve --debug
```

---

## Development Environment

### Virtual Environment Setup

**Using venv (recommended):**
```bash
python -m venv venv
source venv/bin/activate
```

**Using conda:**
```bash
conda create -n gatormath python=3.11
conda activate gatormath
```

### Install Dependencies

**Development mode with all extras:**
```bash
pip install -e ".[dev,test,docs]"
```

**Individual dependency groups:**
```bash
# Core dependencies only
pip install -e .

# Development tools
pip install -e ".[dev]"

# Testing tools
pip install -e ".[test]"

# Documentation tools
pip install -e ".[docs]"
```

### IDE Configuration

**VSCode (.vscode/settings.json):**
```json
{
  "python.defaultInterpreterPath": "${workspaceFolder}/venv/bin/python",
  "python.linting.enabled": true,
  "python.linting.pylintEnabled": false,
  "python.linting.flake8Enabled": true,
  "python.formatting.provider": "black",
  "python.testing.pytestEnabled": true,
  "python.testing.unittestEnabled": false,
  "[python]": {
    "editor.formatOnSave": true,
    "editor.codeActionsOnSave": {
      "source.organizeImports": true
    }
  }
}
```

**PyCharm:**
- Set Project Interpreter to `venv/bin/python`
- Enable pytest as test runner
- Configure Black as formatter
- Enable mypy type checking

---

## Project Structure

```
GatorMath/
├── gatormath/                          # Python package (source code)
│   ├── __init__.py                     # Package initialization
│   ├── core/                           # Core mathematical operations
│   │   ├── __init__.py                 # Core package init
│   │   └── arithmetic.py               # Safe arithmetic operations
│   ├── geometry/                       # Geometric shapes & algorithms
│   │   ├── __init__.py                 # Geometry package init
│   │   └── shapes2d.py                 # 2D shapes (Circle, Triangle, etc.)
│   ├── precision/                      # Floating-point precision handling
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
├── tests/                              # Test suite (coming soon)
│   ├── __init__.py                     # Tests package init
│   ├── test_arithmetic.py              # Core arithmetic tests
│   ├── test_geometry.py                # Geometry tests
│   ├── test_precision.py               # Precision tests
│   ├── test_web.py                     # Web application tests
│   └── test_cli.py                     # CLI tests
├── docs/                               # Documentation
│   ├── API_DOCS.md                     # API reference
│   ├── CLI_DOCS.md                     # CLI documentation
│   ├── DEVELOPMENT.md                  # This file
│   ├── STANDARDS.md                    # Coding standards
│   ├── BRANDING.md                     # Brand guidelines
│   ├── ASSETS.md                       # Asset documentation
│   ├── AUTHENTICATION.md               # Auth documentation
│   └── branches/                       # Branch-specific docs
│       └── BRANCHES.md                 # Branch documentation
├── pyproject.toml                      # Python project configuration
├── README.md                           # Project overview
├── LICENSE                             # MIT License
└── .gitignore                          # Git ignore patterns
```

---

## Development Workflow

### Branch Strategy

**Main Branches:**
- `main` - Production-ready code
- `develop` - Integration branch for features
- `claude/*` - AI-assisted development branches

**Feature Branches:**
```bash
# Create feature branch
git checkout -b feature/new-calculator

# Work on feature
# ... make changes ...

# Commit changes
git add .
git commit -m "feat: Add advanced calculator"

# Push to remote
git push -u origin feature/new-calculator
```

### Making Changes

**1. Create Branch:**
```bash
git checkout -b feature/your-feature-name
```

**2. Make Changes:**
- Edit code following [STANDARDS.md](STANDARDS.md)
- Add tests for new functionality
- Update documentation

**3. Run Tests:**
```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=gatormath --cov-report=html

# Run specific test file
pytest tests/test_arithmetic.py

# Run specific test
pytest tests/test_arithmetic.py::test_safe_add
```

**4. Format Code:**
```bash
# Format with Black
black gatormath/ tests/

# Sort imports
isort gatormath/ tests/

# Check types
mypy gatormath/
```

**5. Commit Changes:**
```bash
git add .
git commit -m "feat: Add new feature"
```

**6. Push to Remote:**
```bash
git push -u origin feature/your-feature-name
```

### Development Server

**Start development server:**
```bash
gatormath serve --debug
```

**Features in debug mode:**
- Auto-reload on code changes
- Detailed error pages
- Debug toolbar (if installed)

**Access the application:**
```
http://localhost:5000
```

---

## Testing

### Test Structure

```
tests/
├── test_arithmetic.py      # Core arithmetic tests
├── test_geometry.py        # Geometry tests
├── test_precision.py       # Precision comparison tests
├── test_web.py            # Flask API tests
└── test_cli.py            # CLI tests
```

### Running Tests

**All tests:**
```bash
pytest
```

**With coverage report:**
```bash
pytest --cov=gatormath --cov-report=term-missing
```

**Specific test file:**
```bash
pytest tests/test_arithmetic.py
```

**Specific test function:**
```bash
pytest tests/test_arithmetic.py::test_safe_add
```

**Verbose output:**
```bash
pytest -v
```

**Stop on first failure:**
```bash
pytest -x
```

### Writing Tests

**Test file template:**
```python
"""
Tests for gatormath.core.arithmetic module.

Author: GatorMath Development Team
Created: 2025-11-02
Version: 0.1.0
"""

import pytest
from gatormath.core import arithmetic


def test_safe_add():
    """Test safe addition of two numbers."""
    assert arithmetic.safe_add(1.0, 2.0) == 3.0
    assert arithmetic.safe_add(0.1, 0.2) == pytest.approx(0.3)


def test_safe_add_overflow():
    """Test overflow detection in addition."""
    with pytest.raises(OverflowError):
        arithmetic.safe_add(1e308, 1e308)


def test_safe_add_nan():
    """Test NaN value handling."""
    with pytest.raises(ValueError):
        arithmetic.safe_add(float('nan'), 1.0)
```

**Test requirements:**
- Each module must have >90% test coverage
- Test both success and error cases
- Use descriptive test names
- Include docstrings
- Use pytest fixtures for setup/teardown

---

## Code Style

GatorMath follows strict coding standards. See [STANDARDS.md](STANDARDS.md) for complete guidelines.

### Key Standards

**Formatting:**
- Use Black for code formatting
- Line length: 100 characters
- Use double quotes for strings

**Type Hints:**
```python
def safe_add(a: Number, b: Number) -> float:
    """Add two numbers safely."""
    return float(a) + float(b)
```

**Docstrings:**
```python
def safe_add(a: Number, b: Number) -> float:
    """
    Add two numbers with overflow checking.

    Args:
        a: First number
        b: Second number

    Returns:
        Sum of a and b

    Raises:
        ValueError: If either value is NaN
        OverflowError: If result exceeds float range

    Examples:
        >>> safe_add(1.0, 2.0)
        3.0
        >>> safe_add(0.1, 0.2)
        0.3

    Complexity: O(1)
    Version: 0.1.0
    """
```

**Imports:**
```python
# Standard library (alphabetical)
import math
import sys
from typing import Union

# Third-party (alphabetical)
import numpy as np
from flask import Flask, jsonify

# Local (relative imports)
from gatormath.core import arithmetic
from gatormath.precision import comparison
```

### Linting and Type Checking

**Run linters:**
```bash
# Black (formatter)
black --check gatormath/ tests/

# Flake8 (linter)
flake8 gatormath/ tests/

# isort (import sorter)
isort --check gatormath/ tests/

# mypy (type checker)
mypy gatormath/
```

**Auto-fix:**
```bash
black gatormath/ tests/
isort gatormath/ tests/
```

---

## Documentation

### Documentation Standards

All documentation must follow the templates in [STANDARDS.md](STANDARDS.md).

**Module docstrings:**
```python
"""
Module Name: arithmetic

Description:
    Safe arithmetic operations with overflow detection and NaN handling.

Module Path: gatormath/core/arithmetic.py
Package: gatormath.core

Author: GatorMath Development Team
Created: 2025-11-02
Modified: 2025-11-02
Version: 0.1.0

Dependencies:
    - math: Standard math functions
    - typing: Type hints

Exports:
    - safe_add: Safe addition
    - safe_subtract: Safe subtraction
    ...

Examples:
    >>> from gatormath.core import arithmetic
    >>> arithmetic.safe_add(1.0, 2.0)
    3.0

Notes:
    All functions handle NaN and infinity values appropriately
"""
```

### Building Documentation

**Generate API docs:**
```bash
# Using pdoc
pdoc --html gatormath -o docs/api/

# Using Sphinx (if configured)
cd docs/
make html
```

---

## Git Workflow

### Commit Message Format

Follow conventional commits:

```
<type>(<scope>): <subject>

<body>

<footer>
```

**Types:**
- `feat:` New feature
- `fix:` Bug fix
- `docs:` Documentation changes
- `style:` Code style changes (formatting)
- `refactor:` Code refactoring
- `test:` Test additions or changes
- `chore:` Build process or auxiliary tool changes

**Examples:**
```bash
git commit -m "feat(arithmetic): Add safe_power function"
git commit -m "fix(web): Handle division by zero in API"
git commit -m "docs: Update CLI documentation"
git commit -m "test(geometry): Add Triangle validation tests"
```

### Pull Request Process

**1. Create PR:**
- Push branch to remote
- Create PR via GitHub interface
- Fill out PR template

**2. PR Requirements:**
- All tests passing
- Code coverage >90%
- Documentation updated
- Code style checks passing
- At least one reviewer approval

**3. Review Process:**
- Address reviewer comments
- Push new commits to same branch
- Request re-review

**4. Merge:**
- Squash and merge (preferred)
- Delete feature branch after merge

---

## Release Process

### Version Numbering

Follow Semantic Versioning (SemVer):

```
MAJOR.MINOR.PATCH
```

- `MAJOR`: Breaking changes
- `MINOR`: New features (backwards compatible)
- `PATCH`: Bug fixes (backwards compatible)

### Creating a Release

**1. Update Version:**
```python
# gatormath/__init__.py
__version__ = "0.2.0"
```

**2. Update Changelog:**
```markdown
## [0.2.0] - 2025-11-02

### Added
- New calculator feature
- Advanced geometry shapes

### Fixed
- Division by zero bug
- Memory leak in web server

### Changed
- Improved precision handling
```

**3. Create Git Tag:**
```bash
git tag -a v0.2.0 -m "Release version 0.2.0"
git push origin v0.2.0
```

**4. Build Distribution:**
```bash
python -m build
```

**5. Publish to PyPI:**
```bash
python -m twine upload dist/*
```

---

## Troubleshooting

### Common Issues

**Import errors after changes:**
```bash
# Reinstall in development mode
pip install -e .
```

**Tests failing after dependency update:**
```bash
# Update all dependencies
pip install -e ".[dev,test]" --upgrade
```

**Port already in use:**
```bash
# Kill process using port 5000
lsof -i :5000
kill -9 <PID>
```

**Black and flake8 conflicts:**
```bash
# Use flake8 configuration that's compatible with Black
# .flake8:
[flake8]
max-line-length = 100
extend-ignore = E203, E266, E501, W503
```

### Getting Help

**Resources:**
- [STANDARDS.md](STANDARDS.md) - Coding standards
- [API_DOCS.md](API_DOCS.md) - API reference
- [CLI_DOCS.md](CLI_DOCS.md) - CLI documentation
- GitHub Issues - Report bugs
- GitHub Discussions - Ask questions

**Debug Mode:**
```bash
# Enable Flask debug mode
export FLASK_DEBUG=true
gatormath serve

# Enable Python warnings
export PYTHONWARNINGS=all
python -m pytest
```

---

**Version:** 0.1.0
**See Also:** [API Docs](API_DOCS.md) | [CLI Docs](CLI_DOCS.md) | [Standards](STANDARDS.md)
