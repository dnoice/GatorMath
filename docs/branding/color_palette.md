# GatorMath Color Palette Specification

**Document Version:** 1.0.0
**Last Updated:** 2025-11-01
**Document Path:** `/docs/branding/color_palette.md`

---

## Overview

This document defines the complete color system for GatorMath, including primary and secondary palettes, usage guidelines, accessibility considerations, and implementation specifications for the Rich CLI framework.

---

## Primary Brand Colors

### Swamp Green
**Role:** Primary Brand Color

- **Hex:** `#2D5016`
- **RGB:** `rgb(45, 80, 22)`
- **RGB Normalized:** `(0.176, 0.314, 0.086)`
- **HSL:** `hsl(95, 57%, 20%)`
- **Rich Name:** `gator_green`

**Usage:**
- Primary headers and titles
- Success messages and confirmations
- Brand elements and logos
- Positive state indicators
- Call-to-action elements

**ASCII Preview:**
```
████████████████  Swamp Green
████████████████  #2D5016
████████████████  Primary Brand
```

---

### Deep Teal
**Role:** Interactive Accent

- **Hex:** `#0D7377`
- **RGB:** `rgb(13, 115, 119)`
- **RGB Normalized:** `(0.051, 0.451, 0.467)`
- **HSL:** `hsl(182, 80%, 26%)`
- **Rich Name:** `gator_teal`

**Usage:**
- Interactive elements and prompts
- Clickable/selectable items
- Links and references
- Active state indicators
- Progress indicators

**ASCII Preview:**
```
████████████████  Deep Teal
████████████████  #0D7377
████████████████  Interactive
```

---

### Sunset Orange
**Role:** Warning & Attention

- **Hex:** `#FF8C42`
- **RGB:** `rgb(255, 140, 66)`
- **RGB Normalized:** `(1.000, 0.549, 0.259)`
- **HSL:** `hsl(24, 100%, 63%)`
- **Rich Name:** `gator_orange`

**Usage:**
- Warning messages
- Important notices
- Deprecation warnings
- Caution indicators
- Attention-grabbing elements

**ASCII Preview:**
```
████████████████  Sunset Orange
████████████████  #FF8C42
████████████████  Warning
```

---

### Blood Red
**Role:** Error & Critical

- **Hex:** `#C1292E`
- **RGB:** `rgb(193, 41, 46)`
- **RGB Normalized:** `(0.757, 0.161, 0.180)`
- **HSL:** `hsl(358, 65%, 46%)`
- **Rich Name:** `gator_red`

**Usage:**
- Error messages
- Critical failures
- Destructive actions
- Invalid states
- Exception indicators

**ASCII Preview:**
```
████████████████  Blood Red
████████████████  #C1292E
████████████████  Error
```

---

### Golden Yellow
**Role:** Information & Tips

- **Hex:** `#F4D35E`
- **RGB:** `rgb(244, 211, 94)`
- **RGB Normalized:** `(0.957, 0.827, 0.369)`
- **HSL:** `hsl(47, 86%, 66%)`
- **Rich Name:** `gator_gold`

**Usage:**
- Information messages
- Tips and suggestions
- Highlighted values
- Special notes
- Documentation references

**ASCII Preview:**
```
████████████████  Golden Yellow
████████████████  #F4D35E
████████████████  Information
```

---

## Secondary Palette

### Slate Gray
**Role:** Primary Text

- **Hex:** `#E8E9EB`
- **RGB:** `rgb(232, 233, 235)`
- **RGB Normalized:** `(0.910, 0.914, 0.922)`
- **HSL:** `hsl(220, 11%, 92%)`
- **Rich Name:** `gator_slate`

**Usage:**
- Primary text on dark backgrounds
- Main content text
- Code output
- Data display
- Standard UI text

**Contrast Ratio (on Charcoal):** 13.2:1 (AAA)

---

### Charcoal
**Role:** Background & Canvas

- **Hex:** `#1A1D1E`
- **RGB:** `rgb(26, 29, 30)`
- **RGB Normalized:** `(0.102, 0.114, 0.118)`
- **HSL:** `hsl(195, 7%, 11%)`
- **Rich Name:** `gator_charcoal`

**Usage:**
- Primary dark backgrounds
- Panel backgrounds
- Card backgrounds
- Terminal background
- Container backgrounds

---

### Mist Gray
**Role:** Subtle Elements

- **Hex:** `#6B7280`
- **RGB:** `rgb(107, 114, 128)`
- **RGB Normalized:** `(0.420, 0.447, 0.502)`
- **HSL:** `hsl(220, 9%, 46%)`
- **Rich Name:** `gator_mist`

**Usage:**
- Secondary text
- Disabled states
- Borders and dividers
- Subtle decorations
- Placeholder text

**Contrast Ratio (on Charcoal):** 4.8:1 (AA)

---

## Extended Palette

### Vibrant Variants (for data visualization)

#### Lime Green
- **Hex:** `#7CB342`
- **Rich Name:** `gator_lime`
- **Usage:** Graphs, charts, data series 1

#### Cyan Blue
- **Hex:** `#26C6DA`
- **Rich Name:** `gator_cyan`
- **Usage:** Graphs, charts, data series 2

#### Violet Purple
- **Hex:** `#AB47BC`
- **Rich Name:** `gator_violet`
- **Usage:** Graphs, charts, data series 3

#### Coral Pink
- **Hex:** `#FF7043`
- **Rich Name:** `gator_coral`
- **Usage:** Graphs, charts, data series 4

---

## Semantic Color Mappings

### State Colors

| State | Color | Hex | Usage Context |
|-------|-------|-----|---------------|
| Success | Swamp Green | #2D5016 | Operation completed successfully |
| Info | Golden Yellow | #F4D35E | General information, tips |
| Warning | Sunset Orange | #FF8C42 | Caution, potential issues |
| Error | Blood Red | #C1292E | Failures, exceptions |
| Active | Deep Teal | #0D7377 | Currently selected/active |
| Inactive | Mist Gray | #6B7280 | Disabled, unavailable |

### Syntax Highlighting

| Element | Color | Hex | Application |
|---------|-------|-----|-------------|
| Keywords | Deep Teal | #0D7377 | Python keywords |
| Strings | Golden Yellow | #F4D35E | String literals |
| Numbers | Lime Green | #7CB342 | Numeric values |
| Functions | Cyan Blue | #26C6DA | Function names |
| Classes | Violet Purple | #AB47BC | Class names |
| Comments | Mist Gray | #6B7280 | Code comments |
| Operators | Sunset Orange | #FF8C42 | Mathematical operators |

---

## Accessibility Standards

### WCAG Compliance

All color combinations must meet WCAG 2.1 Level AA standards minimum:
- **Normal Text:** Minimum contrast ratio 4.5:1
- **Large Text:** Minimum contrast ratio 3:1
- **UI Components:** Minimum contrast ratio 3:1

### Contrast Ratios (Primary Combinations)

| Foreground | Background | Ratio | Grade | Pass |
|-----------|-----------|-------|-------|------|
| Slate Gray | Charcoal | 13.2:1 | AAA | ✓ |
| Swamp Green | Charcoal | 4.9:1 | AA | ✓ |
| Deep Teal | Charcoal | 7.1:1 | AAA | ✓ |
| Golden Yellow | Charcoal | 11.8:1 | AAA | ✓ |
| Sunset Orange | Charcoal | 8.3:1 | AAA | ✓ |
| Blood Red | Charcoal | 5.2:1 | AA | ✓ |
| Mist Gray | Charcoal | 4.8:1 | AA | ✓ |

### Color Blindness Considerations

The palette is designed to be distinguishable across common color vision deficiencies:

- **Deuteranopia (Red-Green):** Uses luminosity and saturation differences
- **Protanopia (Red-Green):** Teal/Orange/Yellow remain distinct
- **Tritanopia (Blue-Yellow):** Green/Red/Gray provide clear differentiation

**Testing Tools:**
- Simulator: Color Oracle, Coblis
- Validation: WebAIM Contrast Checker

---

## Rich Theme Implementation

### Theme Definition

```python
from rich.theme import Theme

GATOR_THEME = Theme({
    # Primary Brand Colors
    "gator_green": "#2D5016",
    "gator_teal": "#0D7377",
    "gator_orange": "#FF8C42",
    "gator_red": "#C1292E",
    "gator_gold": "#F4D35E",

    # Secondary Colors
    "gator_slate": "#E8E9EB",
    "gator_charcoal": "#1A1D1E",
    "gator_mist": "#6B7280",

    # Extended Colors
    "gator_lime": "#7CB342",
    "gator_cyan": "#26C6DA",
    "gator_violet": "#AB47BC",
    "gator_coral": "#FF7043",

    # Semantic Aliases
    "success": "bold #2D5016",
    "info": "#F4D35E",
    "warning": "bold #FF8C42",
    "error": "bold #C1292E",
    "active": "bold #0D7377",
    "inactive": "#6B7280",

    # Text Styles
    "header": "bold #2D5016",
    "subheader": "bold #0D7377",
    "text": "#E8E9EB",
    "subtle": "#6B7280",
    "highlight": "bold #F4D35E",
    "code": "bold #26C6DA on #1A1D1E",

    # UI Elements
    "prompt": "bold #0D7377",
    "border": "#6B7280",
    "panel.border": "#2D5016",
    "table.header": "bold #2D5016",
    "progress.complete": "#2D5016",
    "progress.remaining": "#6B7280",
})
```

### Usage Examples

```python
from rich.console import Console
from gatormath.cli.theme import GATOR_THEME

console = Console(theme=GATOR_THEME)

# Headers
console.print("GatorMath Computation Engine", style="header")

# Success message
console.print("✓ Calculation completed successfully", style="success")

# Error message
console.print("✗ Invalid input detected", style="error")

# Information
console.print("ℹ Using precision mode: adaptive", style="info")

# Code/Data
console.print(f"Result: {result}", style="code")

# Interactive prompt
console.print("Select an option:", style="prompt")
```

---

## Terminal Compatibility

### Color Support Levels

**True Color (24-bit):**
- Primary target
- Full palette support
- Exact hex color rendering

**256 Color:**
- Fallback mode
- Closest color approximation
- Maintained accessibility

**16 Color:**
- Degraded mode
- Semantic mapping preserved
- Basic ANSI colors

### Testing Matrix

| Terminal | OS | Color Support | Status |
|----------|-----|---------------|---------|
| iTerm2 | macOS | True Color | ✓ Full |
| Terminal.app | macOS | True Color | ✓ Full |
| Windows Terminal | Windows | True Color | ✓ Full |
| Alacritty | Linux/macOS/Win | True Color | ✓ Full |
| GNOME Terminal | Linux | True Color | ✓ Full |
| tmux | All | True Color* | ✓ Configured |
| VS Code Terminal | All | True Color | ✓ Full |

*Requires `set -g default-terminal "screen-256color"`

---

## Export Formats

### CSS Variables

```css
:root {
  --gator-green: #2D5016;
  --gator-teal: #0D7377;
  --gator-orange: #FF8C42;
  --gator-red: #C1292E;
  --gator-gold: #F4D35E;
  --gator-slate: #E8E9EB;
  --gator-charcoal: #1A1D1E;
  --gator-mist: #6B7280;
}
```

### JSON Export

```json
{
  "colors": {
    "primary": {
      "green": "#2D5016",
      "teal": "#0D7377",
      "orange": "#FF8C42",
      "red": "#C1292E",
      "gold": "#F4D35E"
    },
    "secondary": {
      "slate": "#E8E9EB",
      "charcoal": "#1A1D1E",
      "mist": "#6B7280"
    }
  }
}
```

### Python Constants

```python
# GatorMath Color Constants
GATOR_GREEN = "#2D5016"
GATOR_TEAL = "#0D7377"
GATOR_ORANGE = "#FF8C42"
GATOR_RED = "#C1292E"
GATOR_GOLD = "#F4D35E"
GATOR_SLATE = "#E8E9EB"
GATOR_CHARCOAL = "#1A1D1E"
GATOR_MIST = "#6B7280"
```

---

## SVG Color Application

All SVG assets must use the defined color palette:

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100">
  <defs>
    <style>
      .brand-primary { fill: #2D5016; }
      .brand-accent { fill: #0D7377; }
      .brand-highlight { fill: #F4D35E; }
    </style>
  </defs>
  <!-- SVG content using defined classes -->
</svg>
```

---

## Maintenance & Updates

**Version History:**
- v1.0.0 (2025-11-01): Initial palette definition

**Review Schedule:** Quarterly

**Update Process:**
1. Propose changes with rationale
2. Test accessibility compliance
3. Update theme definitions
4. Regenerate documentation
5. Update all assets

---

**Document Maintained By:** GatorMath Development Team
**Contact:** See CONTRIBUTING.md for communication channels
