# GatorMath Project Standards & Guidelines

**Document Version:** 1.0.0
**Last Updated:** 2025-11-01
**Document Path:** `/STANDARDS.md`

---

## Table of Contents

1. [Project Overview](#project-overview)
2. [Branding & Visual Identity](#branding--visual-identity)
3. [Color Schemes](#color-schemes)
4. [Code Documentation Standards](#code-documentation-standards)
5. [Module Structure Standards](#module-structure-standards)
6. [CLI Interface Standards](#cli-interface-standards)
7. [Testing Standards](#testing-standards)
8. [Git Workflow Standards](#git-workflow-standards)

---

## Project Overview

**Project Name:** GatorMath
**Tagline:** "A math and geometry Pythonic toolkit that refuses to be boring"
**Mission:** Provide clean APIs, fast numerics, robust geometry handling, and comprehensive functionality for mathematical and geometric operations.

**Core Principles:**
- **Robustness:** All code must handle edge cases and floating-point precision issues
- **Comprehensiveness:** No half-implementations; complete, production-ready modules only
- **Beauty:** CLI output should be intuitive, interactive, and visually appealing
- **Documentation:** Every artifact must have complete docstrings with metadata
- **Cohesiveness:** Unified branding, theming, and user experience across all components

---

## Branding & Visual Identity

### Name & Mascot
- **Primary Name:** GatorMath
- **Mascot:** Mathematical Alligator (represented via SVG, no emojis)
- **Personality:** Smart, efficient, powerful, playful but professional

### Typography
- **Code Font:** JetBrains Mono, Fira Code, or system monospace
- **Documentation Headers:** Bold, clear hierarchy
- **CLI Output:** Rich library with custom styling

### SVG Assets
All visual branding uses SVG format for scalability and terminal compatibility.

**Asset Locations:**
- `/docs/branding/logos/` - Logo variations
- `/docs/branding/icons/` - UI icons and symbols
- `/docs/branding/diagrams/` - Technical diagrams

---

## Color Schemes

### Primary Palette

#### Swamp Green (Brand Primary)
- **Hex:** `#2D5016`
- **RGB:** `(45, 80, 22)`
- **Usage:** Primary branding, headers, success states
- **Rich Name:** `gator_green`

#### Deep Teal (Accent)
- **Hex:** `#0D7377`
- **RGB:** `(13, 115, 119)`
- **Usage:** Interactive elements, links, highlights
- **Rich Name:** `gator_teal`

#### Sunset Orange (Warning)
- **Hex:** `#FF8C42`
- **RGB:** `(255, 140, 66)`
- **Usage:** Warnings, important notices
- **Rich Name:** `gator_orange`

#### Blood Red (Error)
- **Hex:** `#C1292E`
- **RGB:** `(193, 41, 46)`
- **Usage:** Errors, critical states
- **Rich Name:** `gator_red`

#### Golden Yellow (Info)
- **Hex:** `#F4D35E`
- **RGB:** `(244, 211, 94)`
- **Usage:** Information, tips, highlights
- **Rich Name:** `gator_gold`

### Secondary Palette

#### Slate Gray (Text Primary)
- **Hex:** `#E8E9EB`
- **RGB:** `(232, 233, 235)`
- **Usage:** Primary text on dark backgrounds
- **Rich Name:** `gator_slate`

#### Charcoal (Background)
- **Hex:** `#1A1D1E`
- **RGB:** `(26, 29, 30)`
- **Usage:** Dark backgrounds, panels
- **Rich Name:** `gator_charcoal`

#### Mist Gray (Subtle)
- **Hex:** `#6B7280`
- **RGB:** `(107, 114, 128)`
- **Usage:** Subtle text, borders, dividers
- **Rich Name:** `gator_mist`

### CLI Color Usage Matrix

| Element Type | Color | Rich Style |
|-------------|-------|-----------|
| Headers | Gator Green | `bold gator_green` |
| Success Messages | Gator Green | `bold gator_green` |
| Info Messages | Gator Gold | `gator_gold` |
| Warnings | Gator Orange | `bold gator_orange` |
| Errors | Gator Red | `bold gator_red` |
| Interactive Prompts | Gator Teal | `bold gator_teal` |
| Code/Data | Slate Gray | `gator_slate` |
| Subtle Text | Mist Gray | `gator_mist` |
| Highlights | Deep Teal | `on gator_teal` |

---

## Code Documentation Standards

### Module Docstring Template

Every Python module must include a comprehensive docstring following this template:

```python
"""
Module Name: [module_name]

Description:
    [Detailed description of module purpose and functionality]

Module Path: [relative/path/from/project/root.py]
Package: gatormath.[subpackage]

Author: GatorMath Development Team
Created: [YYYY-MM-DD]
Modified: [YYYY-MM-DD]
Version: [X.Y.Z]

Dependencies:
    - [dependency1]: [purpose]
    - [dependency2]: [purpose]

Exports:
    - [Class/Function1]: [brief description]
    - [Class/Function2]: [brief description]

Examples:
    >>> [usage example 1]
    >>> [usage example 2]

Notes:
    [Any important notes, caveats, or implementation details]

References:
    [1] [Citation or reference if applicable]
"""
```

### Class Docstring Template

```python
class ClassName:
    """
    Brief one-line description.

    Detailed Description:
        [Comprehensive explanation of the class purpose, behavior,
        and usage patterns. Multiple paragraphs if needed.]

    Attributes:
        attr1 (type): Description of attribute
        attr2 (type): Description of attribute

    Methods:
        method1: Brief description
        method2: Brief description

    Mathematical Formulation:
        [If applicable, include mathematical notation or formulas]

    Precision Notes:
        [If applicable, discuss floating-point considerations]

    Examples:
        >>> obj = ClassName(param1, param2)
        >>> obj.method1()
        [expected output]

    See Also:
        - RelatedClass: [relationship description]
        - related_function: [relationship description]

    Version: X.Y.Z
    """
```

### Function Docstring Template

```python
def function_name(param1: Type1, param2: Type2) -> ReturnType:
    """
    Brief one-line description.

    Detailed Description:
        [Comprehensive explanation of function behavior, algorithm,
        and use cases. Multiple paragraphs if needed.]

    Args:
        param1 (Type1): Description of parameter 1
            - Range: [if applicable]
            - Constraints: [if applicable]
        param2 (Type2): Description of parameter 2

    Returns:
        ReturnType: Description of return value
            - Range: [if applicable]
            - Format: [if applicable]

    Raises:
        ExceptionType1: Condition when this is raised
        ExceptionType2: Condition when this is raised

    Algorithm:
        1. [Step 1 of algorithm]
        2. [Step 2 of algorithm]

    Complexity:
        Time: O(...)
        Space: O(...)

    Precision:
        [Floating-point considerations if applicable]

    Examples:
        >>> function_name(arg1, arg2)
        [expected output]

        >>> # Edge case example
        >>> function_name(edge_case_arg)
        [expected output]

    See Also:
        - related_function: [relationship]

    Notes:
        [Important implementation notes or caveats]

    Version: X.Y.Z
    """
```

---

## Module Structure Standards

### Project Directory Structure

```
GatorMath/
├── gatormath/                  # Main package
│   ├── __init__.py            # Package initialization with metadata
│   ├── core/                  # Core mathematical operations
│   │   ├── __init__.py
│   │   ├── arithmetic.py      # Basic arithmetic operations
│   │   ├── algebra.py         # Algebraic operations
│   │   ├── calculus.py        # Calculus operations
│   │   └── statistics.py      # Statistical functions
│   ├── geometry/              # Geometric operations
│   │   ├── __init__.py
│   │   ├── shapes2d.py        # 2D shapes
│   │   ├── shapes3d.py        # 3D shapes
│   │   ├── transforms.py      # Geometric transformations
│   │   └── spatial.py         # Spatial algorithms
│   ├── precision/             # Floating-point precision handling
│   │   ├── __init__.py
│   │   ├── comparison.py      # Safe comparisons
│   │   └── rounding.py        # Robust rounding
│   ├── cli/                   # CLI interface
│   │   ├── __init__.py
│   │   ├── app.py            # Main CLI application
│   │   ├── theme.py          # Rich theme configuration
│   │   ├── commands/         # CLI commands
│   │   │   ├── __init__.py
│   │   │   ├── math_cmd.py
│   │   │   └── geometry_cmd.py
│   │   └── interactive/      # Interactive components
│   │       ├── __init__.py
│   │       ├── prompts.py
│   │       └── visualizers.py
│   └── utils/                # Utility functions
│       ├── __init__.py
│       ├── validation.py
│       └── logging.py
├── tests/                    # Test suite
│   ├── __init__.py
│   ├── test_core/
│   ├── test_geometry/
│   └── test_precision/
├── docs/                     # Documentation
│   ├── branding/            # Branding assets
│   │   ├── logos/
│   │   ├── icons/
│   │   └── color_palette.md
│   ├── api/                 # API documentation
│   └── guides/              # User guides
├── examples/                # Example scripts
├── pyproject.toml          # Project configuration
├── STANDARDS.md            # This document
├── CONTRIBUTING.md         # Contribution guidelines
├── README.md              # Project readme
└── LICENSE                # License file
```

### Import Organization

All imports must follow this order:
1. Standard library imports
2. Third-party imports (alphabetical)
3. Local application imports (alphabetical)

```python
# Standard library
import math
import sys
from typing import List, Optional, Union

# Third-party
import numpy as np
from rich.console import Console

# Local
from gatormath.core import arithmetic
from gatormath.precision import comparison
```

---

## CLI Interface Standards

### Rich Console Configuration

All CLI output must use the Rich library for consistent, beautiful output.

**Standard Console Setup:**
```python
from rich.console import Console
from rich.theme import Theme
from gatormath.cli.theme import GATOR_THEME

console = Console(theme=GATOR_THEME)
```

### Interactive Elements

**Required Components:**
- Progress bars for long operations
- Tables for structured data display
- Panels for grouped information
- Syntax highlighting for code/formulas
- Interactive prompts for user input
- Tree views for hierarchical data

### Output Standards

1. **Headers:** Always use styled headers with consistent formatting
2. **Results:** Display in formatted tables or panels
3. **Errors:** Clear, actionable error messages with suggestions
4. **Progress:** Show progress for operations taking >1 second
5. **Confirmation:** Request confirmation for destructive operations

---

## Testing Standards

### Test Coverage Requirements
- **Minimum Coverage:** 90% overall
- **Critical Modules:** 100% coverage required
- **Test Types:** Unit, integration, property-based

### Test Naming Convention
```python
def test_[function_name]_[scenario]_[expected_result]():
    """
    Test: [function_name]
    Scenario: [detailed scenario description]
    Expected: [expected outcome]
    """
```

### Test Organization
- One test file per module
- Group related tests in classes
- Use fixtures for common setup
- Include edge cases and error conditions

---

## Git Workflow Standards

### Branch Naming
- Feature branches: `claude/[feature-description]-[session-id]`
- All development on designated feature branches
- Never commit directly to main

### Commit Messages
Format:
```
[TYPE]: Brief description (50 chars max)

Detailed description of changes:
- Change 1
- Change 2
- Change 3

Affects: [modules/files affected]
Testing: [testing performed]
```

**Types:** feat, fix, docs, style, refactor, test, chore

### Commit Scope
- Logical, atomic commits
- Each commit should build successfully
- Include tests with feature commits

---

## Version Control

**Current Version:** 0.1.0
**Versioning Scheme:** Semantic Versioning (MAJOR.MINOR.PATCH)

**Version Locations:**
- `pyproject.toml`
- `gatormath/__init__.py`
- Documentation headers

---

## Compliance Checklist

Before committing any code, verify:

- [ ] Complete docstrings with all required metadata
- [ ] Type hints on all function signatures
- [ ] Comprehensive error handling
- [ ] Edge case coverage
- [ ] Tests written and passing
- [ ] CLI output uses Rich theming
- [ ] Colors match brand palette
- [ ] No emoji usage (SVG only)
- [ ] Import organization correct
- [ ] No lazy implementations or TODO comments
- [ ] Documentation updated
- [ ] Version numbers consistent

---

**Document Maintained By:** GatorMath Development Team
**Review Cycle:** Quarterly or as needed for major changes
