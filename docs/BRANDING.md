# GatorMath Branding Guidelines

**Version:** 0.1.0
**Last Updated:** 2025-11-02
**Document Path:** `/docs/BRANDING.md`

---

## Table of Contents

1. [Brand Identity](#brand-identity)
2. [Visual Identity](#visual-identity)
3. [Color Palette](#color-palette)
4. [Typography](#typography)
5. [Logo & Mascot](#logo--mascot)
6. [Voice & Tone](#voice--tone)
7. [UI/UX Guidelines](#uiux-guidelines)
8. [Asset Management](#asset-management)

---

## Brand Identity

### Name

**Primary:** GatorMath
**Pronunciation:** GAY-tor-Math
**Capitalization:** Always capitalize 'G' and 'M', no spaces

**Acceptable:**
- GatorMath
- gatormath (in code/URLs only)

**Incorrect:**
- Gator Math
- gator math
- GATORMATH
- GatorMaths

### Tagline

**Primary:** "Mathematical precision with bite"
**Alternative:** "A math and geometry Pythonic toolkit that refuses to be boring"

### Mission Statement

Provide clean APIs, fast numerics, robust geometry handling, and comprehensive functionality for mathematical and geometric operations with beautiful, intuitive interfaces.

### Core Values

**Robustness**
- Handle edge cases gracefully
- Comprehensive error handling
- Floating-point precision awareness

**Beauty**
- Intuitive interfaces
- Visually appealing output
- Thoughtful UX design

**Comprehensiveness**
- No half-implementations
- Production-ready modules
- Complete documentation

**Pythonic Excellence**
- Follow Python best practices
- Clean, readable code
- Type hints throughout

---

## Visual Identity

### Mascot

**Character:** Mathematical Alligator
**Personality:** Smart, efficient, powerful, playful but professional

**Characteristics:**
- Sharp mind (like sharp teeth)
- Precise calculations (like precise bites)
- Patient and methodical (like alligators hunting)
- Powerful but controlled

**Visual Representation:**
- SVG format only (no emojis in production)
- Clean, geometric design
- Mathematical elements integrated (equations, graphs, geometric shapes)
- Color scheme follows brand palette

### Design Principles

**Minimalism**
- Clean, uncluttered interfaces
- Focus on functionality
- Purposeful use of color and space

**Geometric Precision**
- Sharp angles and clean lines
- Mathematical accuracy in visual elements
- Grid-based layouts

**Professional Playfulness**
- Serious about mathematics
- Approachable and engaging
- Balance between fun and functional

---

## Color Palette

### Primary Palette

#### Swamp Green (Brand Primary)
```
Hex:     #2D5016
RGB:     (45, 80, 22)
HSL:     (97°, 57%, 20%)
CMYK:    (44%, 0%, 72%, 69%)
```
**Usage:**
- Primary branding and headers
- Success states and confirmations
- Call-to-action buttons
- Active states

**Rich Name:** `gator_green`

**Code Example:**
```python
from rich.console import Console
console = Console()
console.print("[bold gator_green]GatorMath[/bold gator_green]")
```

---

#### Deep Teal (Accent)
```
Hex:     #0D7377
RGB:     (13, 115, 119)
HSL:     (182°, 80%, 26%)
CMYK:    (89%, 3%, 0%, 53%)
```
**Usage:**
- Interactive elements
- Links and navigation
- Highlights and focus states
- Secondary buttons

**Rich Name:** `gator_teal`

---

#### Sunset Orange (Warning)
```
Hex:     #FF8C42
RGB:     (255, 140, 66)
HSL:     (23°, 100%, 63%)
CMYK:    (0%, 45%, 74%, 0%)
```
**Usage:**
- Warning messages
- Important notices
- Attention-grabbing elements
- Progress indicators

**Rich Name:** `gator_orange`

---

#### Blood Red (Error)
```
Hex:     #C1292E
RGB:     (193, 41, 46)
HSL:     (358°, 65%, 46%)
CMYK:    (0%, 79%, 76%, 24%)
```
**Usage:**
- Error messages
- Critical states
- Delete/destructive actions
- Validation failures

**Rich Name:** `gator_red`

---

#### Golden Yellow (Info)
```
Hex:     #F4D35E
RGB:     (244, 211, 94)
HSL:     (47°, 86%, 66%)
CMYK:    (0%, 14%, 61%, 4%)
```
**Usage:**
- Information messages
- Tips and hints
- Highlights
- Special features

**Rich Name:** `gator_gold`

---

### Secondary Palette

#### Slate Gray (Text Primary)
```
Hex:     #E8E9EB
RGB:     (232, 233, 235)
HSL:     (220°, 9%, 92%)
CMYK:    (1%, 1%, 0%, 8%)
```
**Usage:**
- Primary text on dark backgrounds
- Main content
- Readable body text

**Rich Name:** `gator_slate`

---

#### Charcoal (Background)
```
Hex:     #1A1D1E
RGB:     (26, 29, 30)
HSL:     (195°, 7%, 11%)
CMYK:    (13%, 3%, 0%, 88%)
```
**Usage:**
- Dark backgrounds
- Panels and containers
- Code blocks
- Terminal backgrounds

**Rich Name:** `gator_charcoal`

---

#### Mist Gray (Subtle)
```
Hex:     #6B7280
RGB:     (107, 114, 128)
HSL:     (220°, 9%, 46%)
CMYK:    (16%, 11%, 0%, 50%)
```
**Usage:**
- Subtle text
- Borders and dividers
- Disabled states
- Placeholder text

**Rich Name:** `gator_mist`

---

### CLI Color Usage Matrix

| Element Type | Color | Rich Style | Use Case |
|-------------|-------|-----------|----------|
| Headers | Swamp Green | `bold gator_green` | Section titles, banners |
| Success | Swamp Green | `bold gator_green` | Confirmations, completed tasks |
| Info | Golden Yellow | `gator_gold` | Tips, helpful messages |
| Warning | Sunset Orange | `bold gator_orange` | Caution, deprecation notices |
| Error | Blood Red | `bold gator_red` | Failures, exceptions |
| Prompts | Deep Teal | `bold gator_teal` | User input, questions |
| Code/Data | Slate Gray | `gator_slate` | Output, results |
| Subtle | Mist Gray | `gator_mist` | Metadata, timestamps |
| Highlight | Deep Teal | `on gator_teal` | Selected items, focus |

---

### Web Color Usage

**CSS Variables:**
```css
:root {
  /* Primary */
  --color-gator-green: #2D5016;
  --color-gator-teal: #0D7377;
  --color-gator-orange: #FF8C42;
  --color-gator-red: #C1292E;
  --color-gator-gold: #F4D35E;

  /* Secondary */
  --color-gator-slate: #E8E9EB;
  --color-gator-charcoal: #1A1D1E;
  --color-gator-mist: #6B7280;

  /* Semantic */
  --color-primary: var(--color-gator-green);
  --color-accent: var(--color-gator-teal);
  --color-success: var(--color-gator-green);
  --color-warning: var(--color-gator-orange);
  --color-error: var(--color-gator-red);
  --color-info: var(--color-gator-gold);

  /* Text */
  --color-text-primary: var(--color-gator-slate);
  --color-text-subtle: var(--color-gator-mist);

  /* Backgrounds */
  --color-bg-primary: var(--color-gator-charcoal);
  --color-bg-elevated: #242729;
}
```

---

## Typography

### Font Families

**Code/Monospace:**
1. JetBrains Mono (preferred)
2. Fira Code
3. SF Mono
4. Consolas
5. Monaco
6. Courier New (fallback)

**Web Interface:**
1. Inter (preferred for UI)
2. -apple-system, BlinkMacSystemFont (system fonts)
3. "Segoe UI", Roboto
4. Helvetica, Arial (fallback)

**Documentation Headers:**
1. System UI Bold
2. -apple-system Bold
3. Helvetica Bold (fallback)

### Font Sizing

**CLI:**
- Default terminal font size (respects user settings)
- Use Rich library for styling, not font size manipulation

**Web:**
```css
/* Base */
--font-size-xs: 0.75rem;   /* 12px */
--font-size-sm: 0.875rem;  /* 14px */
--font-size-base: 1rem;    /* 16px */
--font-size-lg: 1.125rem;  /* 18px */
--font-size-xl: 1.25rem;   /* 20px */
--font-size-2xl: 1.5rem;   /* 24px */
--font-size-3xl: 1.875rem; /* 30px */
--font-size-4xl: 2.25rem;  /* 36px */

/* Code */
--font-size-code: 0.875rem; /* 14px */
```

### Font Weights

```css
--font-weight-normal: 400;
--font-weight-medium: 500;
--font-weight-semibold: 600;
--font-weight-bold: 700;
```

### Line Heights

```css
--line-height-tight: 1.25;
--line-height-normal: 1.5;
--line-height-relaxed: 1.75;
--line-height-loose: 2;
```

---

## Logo & Mascot

### Logo Variations

**Primary Logo**
- Full GatorMath wordmark with mascot
- Use for: Headers, documentation covers, promotional materials
- Minimum size: 120px wide
- Formats: SVG (preferred), PNG (high-res fallback)

**Icon Only**
- Mascot head or simplified geometric alligator
- Use for: Favicons, app icons, small spaces
- Minimum size: 32px × 32px
- Formats: SVG, PNG, ICO

**Wordmark Only**
- GatorMath text without mascot
- Use for: Terminal banners, footers, inline citations
- Minimum size: 80px wide

### Logo Usage Guidelines

**DO:**
- Maintain clear space around logo (minimum: logo height × 0.25)
- Use on contrasting backgrounds
- Scale proportionally
- Use approved color variations

**DON'T:**
- Stretch or distort
- Rotate or skew
- Change colors outside approved palette
- Add effects (shadows, glows, etc.)
- Place on busy backgrounds without container

### Mascot Personality

**Visual Attributes:**
- Sharp, intelligent eyes
- Mathematical symbols integrated into design
- Geometric, angular style (not cartoonish)
- Professional but approachable

**Emotional Qualities:**
- Confident but not arrogant
- Helpful and friendly
- Precise and methodical
- Powerful yet controlled

---

## Voice & Tone

### Writing Style

**Professional but Approachable**
- Use clear, concise language
- Avoid jargon unless necessary
- Explain technical concepts simply
- Be helpful, not condescending

**Examples:**

**Good:**
```
GatorMath detected a division by zero. Using 0.0 as the denominator
would cause an error. Please provide a non-zero value.
```

**Bad:**
```
ERROR: DIV/0 EXCEPTION
```

### Error Messages

**Structure:**
1. What happened (clear, non-technical)
2. Why it happened (brief explanation)
3. How to fix it (actionable steps)

**Example:**
```
Cannot calculate square root of negative number

Square root is undefined for negative values in real numbers.

Try:
  • Use a positive number: sqrt(16.0) → 4.0
  • Or use complex numbers for advanced operations
```

### Success Messages

**Keep It Simple:**
```
✓ Calculation complete: 42.0
✓ Server running at http://localhost:5000
✓ Tests passed: 95/95
```

### Prompts and Questions

**Be Clear and Specific:**
```
Good: "Enter radius (positive number):"
Bad:  "Value?"

Good: "Choose operation [add/subtract/multiply/divide]:"
Bad:  "Pick one:"
```

---

## UI/UX Guidelines

### CLI Interface

**Banner Format:**
```
╭─────────────────────────────────╮
│ 🐊 GatorMath                    │
│ Mathematical precision with bite │
╰─────────────────────────────────╯
```

**Progress Indicators:**
- Use Rich progress bars
- Show percentage and time estimates
- Clear start/end states

**Tables:**
- Clear headers
- Aligned columns
- Appropriate borders
- Color-coded rows for categories

**Panels:**
- Use for grouping related information
- Clear titles
- Appropriate padding
- Subtle borders

### Web Interface

**Navigation:**
- Clear hierarchy
- Breadcrumbs for deep navigation
- Active state indicators
- Responsive menu for mobile

**Buttons:**
```css
/* Primary */
background: var(--color-gator-green);
color: white;
padding: 0.75rem 1.5rem;
border-radius: 0.5rem;

/* Secondary */
background: transparent;
border: 2px solid var(--color-gator-teal);
color: var(--color-gator-teal);

/* Danger */
background: var(--color-gator-red);
color: white;
```

**Forms:**
- Clear labels above inputs
- Helpful placeholder text
- Inline validation
- Clear error states
- Success confirmation

**Cards:**
- Subtle shadows for depth
- Clear titles and descriptions
- Consistent padding
- Hover states for interactive cards

---

## Asset Management

### Directory Structure

```
docs/branding/
├── logos/
│   ├── gatormath-primary.svg
│   ├── gatormath-icon.svg
│   ├── gatormath-wordmark.svg
│   └── variations/
│       ├── gatormath-light.svg
│       ├── gatormath-dark.svg
│       └── gatormath-monochrome.svg
│
├── icons/
│   ├── favicon.ico
│   ├── favicon.svg
│   ├── apple-touch-icon.png
│   └── ui-icons/
│       ├── calculator.svg
│       ├── geometry.svg
│       └── precision.svg
│
├── diagrams/
│   ├── architecture.svg
│   ├── workflow.svg
│   └── concepts/
│
└── colors/
    ├── palette.svg
    └── swatches.json
```

### File Naming Conventions

**Pattern:** `{project}-{type}-{variant}.{ext}`

**Examples:**
- `gatormath-logo-primary.svg`
- `gatormath-icon-monochrome.svg`
- `gatormath-banner-dark.png`

### SVG Guidelines

**Optimization:**
- Remove unnecessary metadata
- Simplify paths
- Use viewBox for scalability
- Minimize file size

**Accessibility:**
- Include `<title>` element
- Add `role="img"` attribute
- Provide `aria-label` when used inline

**Example:**
```xml
<svg viewBox="0 0 100 100" role="img" aria-label="GatorMath Logo">
  <title>GatorMath Logo</title>
  <!-- paths -->
</svg>
```

### Image Export Guidelines

**SVG (Primary):**
- Use for all logos and icons
- Ensure scalability
- Optimize with SVGO

**PNG (Fallback):**
- High resolution: 2x, 3x for retina
- Transparent backgrounds
- Optimize with ImageOptim or TinyPNG

**Favicon:**
- ICO: 16×16, 32×32, 48×48
- SVG: Scalable favicon for modern browsers
- PNG: Apple touch icon (180×180)

---

**Version:** 0.1.0
**See Also:** [Standards](STANDARDS.md) | [Assets Guide](ASSETS.md) | [Development Guide](DEVELOPMENT.md)
