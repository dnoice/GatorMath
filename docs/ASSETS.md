# GatorMath Assets Documentation

**Version:** 0.1.0
**Last Updated:** 2025-11-02
**Document Path:** `/docs/ASSETS.md`

---

## Table of Contents

1. [Overview](#overview)
2. [Asset Directory Structure](#asset-directory-structure)
3. [Web Assets](#web-assets)
4. [Brand Assets](#brand-assets)
5. [File Naming Conventions](#file-naming-conventions)
6. [Optimization Guidelines](#optimization-guidelines)
7. [Version Control](#version-control)
8. [Usage Guidelines](#usage-guidelines)

---

## Overview

This document defines the organization, naming, optimization, and usage of all GatorMath assets including stylesheets, JavaScript files, images, fonts, and branding materials.

### Asset Categories

**Web Assets** (Production)
- CSS stylesheets
- JavaScript modules
- HTML templates
- Web fonts

**Brand Assets** (Marketing & Identity)
- Logos and wordmarks
- Icons and favicons
- Diagrams and illustrations
- Color palettes

**Documentation Assets**
- Technical diagrams
- Architecture charts
- Tutorial images
- Screenshots

---

## Asset Directory Structure

### Web Application Assets

```
gatormath/web/
├── static/
│   ├── css/                        # Stylesheets (5 files)
│   │   ├── base.css               # CSS variables, resets, animations
│   │   ├── layout.css             # Navigation, sections, grids
│   │   ├── components.css         # Buttons, cards, calculators
│   │   ├── playground.css         # Interactive canvas styles
│   │   └── responsive.css         # Media queries
│   │
│   ├── js/                        # JavaScript modules (10 files)
│   │   ├── utils.js               # Shared utilities
│   │   ├── three-background.js    # 3D particle system
│   │   ├── animations.js          # GSAP scroll animations
│   │   ├── vector-canvas.js       # Vector operations playground
│   │   ├── bezier-canvas.js       # Bezier curve editor
│   │   ├── matrix-canvas.js       # Matrix transformations
│   │   ├── triangle-canvas.js     # Triangle calculator
│   │   ├── calculators.js         # Live calculators
│   │   ├── code-playground.js     # Code editor
│   │   └── init.js                # Initialization
│   │
│   ├── fonts/                     # Web fonts (if self-hosted)
│   │   ├── jetbrains-mono/
│   │   └── inter/
│   │
│   └── images/                    # Web images
│       ├── og-image.png           # Open Graph image (1200×630)
│       ├── favicon.svg            # Scalable favicon
│       └── icons/                 # UI icons
│
└── templates/
    └── index.html                 # Main HTML template
```

### Brand Assets

```
docs/branding/
├── logos/
│   ├── gatormath-primary.svg      # Full logo with mascot
│   ├── gatormath-icon.svg         # Icon/mascot only
│   ├── gatormath-wordmark.svg     # Text only
│   └── variations/
│       ├── gatormath-light.svg    # Light background variant
│       ├── gatormath-dark.svg     # Dark background variant
│       └── gatormath-monochrome.svg
│
├── icons/
│   ├── favicon.ico                # Multi-size ICO
│   ├── favicon.svg                # Modern browsers
│   ├── apple-touch-icon.png       # iOS (180×180)
│   ├── android-chrome-192x192.png
│   ├── android-chrome-512x512.png
│   └── ui-icons/
│       ├── calculator.svg
│       ├── geometry.svg
│       └── precision.svg
│
├── diagrams/
│   ├── architecture.svg           # System architecture
│   ├── workflow.svg              # Development workflow
│   ├── data-flow.svg             # Data flow diagrams
│   └── concepts/
│       ├── precision.svg         # Floating-point precision
│       └── geometry.svg          # Geometric concepts
│
├── colors/
│   ├── palette.svg               # Visual palette
│   ├── swatches.json             # Color definitions
│   └── gradients.svg             # Brand gradients
│
└── patterns/
    ├── background-pattern.svg    # Repeatable patterns
    └── texture.png               # Subtle textures
```

---

## Web Assets

### CSS Structure

**base.css** (Foundation)
- CSS custom properties (variables)
- CSS resets and normalize
- Global animations (@keyframes)
- Typography base styles

**Key Variables:**
```css
:root {
  /* Colors */
  --color-gator-green: #2D5016;
  --color-gator-teal: #0D7377;
  --color-gator-orange: #FF8C42;

  /* Spacing */
  --spacing-xs: 0.25rem;
  --spacing-sm: 0.5rem;
  --spacing-md: 1rem;
  --spacing-lg: 2rem;
  --spacing-xl: 4rem;

  /* Typography */
  --font-mono: 'JetBrains Mono', monospace;
  --font-sans: 'Inter', -apple-system, sans-serif;

  /* Breakpoints (for JS) */
  --breakpoint-sm: 640px;
  --breakpoint-md: 768px;
  --breakpoint-lg: 1024px;
  --breakpoint-xl: 1280px;
}
```

**layout.css** (Structure)
- Navigation styles
- Section layouts
- Grid systems
- Flex containers
- Positioning

**components.css** (UI Elements)
- Buttons
- Cards
- Forms
- Calculators
- Modals
- Tooltips

**playground.css** (Interactive Elements)
- Canvas containers
- Control panels
- Code editors
- Interactive visualizations

**responsive.css** (Media Queries)
- Mobile-first approach
- Breakpoint definitions
- Touch-friendly adjustments

### JavaScript Structure

**utils.js** (Shared Utilities)
- API client functions
- DOM helpers
- Math utilities
- Formatting functions

**Exports:**
```javascript
export const API_BASE_URL = '/api';
export async function apiCall(endpoint, data);
export function formatNumber(num, decimals);
export function debounce(func, wait);
```

**three-background.js** (3D Graphics)
- Three.js particle system
- Animated background
- Performance optimized

**animations.js** (Scroll Effects)
- GSAP animations
- Scroll-triggered effects
- Intersection observers

**Individual Canvas Modules**
- vector-canvas.js: Vector operations visualization
- bezier-canvas.js: Bezier curve editor
- matrix-canvas.js: Matrix transformation playground
- triangle-canvas.js: Triangle calculator

**calculators.js** (Live Calculators)
- Real-time calculation
- API integration
- Result formatting

**code-playground.js** (Code Editor)
- Syntax highlighting
- Code execution
- Example templates

**init.js** (Initialization)
- Module orchestration
- Event binding
- Initial state setup

---

## Brand Assets

### Logo Files

**gatormath-primary.svg**
- Full logo with mascot and wordmark
- Use for: Headers, hero sections, print materials
- Minimum width: 120px
- Colors: Swamp Green (#2D5016)

**gatormath-icon.svg**
- Mascot head or geometric alligator icon
- Use for: Favicons, app icons, small spaces
- Minimum size: 32×32px
- Square aspect ratio

**gatormath-wordmark.svg**
- Text "GatorMath" without mascot
- Use for: Inline citations, footers, limited space
- Minimum width: 80px

### Logo Variants

**Light Background:** `gatormath-light.svg`
- Dark logo on light backgrounds
- Contrast ratio: 4.5:1 minimum

**Dark Background:** `gatormath-dark.svg`
- Light logo on dark backgrounds
- Contrast ratio: 4.5:1 minimum

**Monochrome:** `gatormath-monochrome.svg`
- Single-color version for special use
- Use when color printing unavailable

### Favicons

**Required Files:**
```
favicon.ico          # 16×16, 32×32, 48×48 (multi-resolution)
favicon.svg          # Scalable for modern browsers
apple-touch-icon.png # 180×180 (iOS)
android-chrome-192x192.png
android-chrome-512x512.png
```

**HTML Implementation:**
```html
<link rel="icon" type="image/svg+xml" href="/static/images/favicon.svg">
<link rel="icon" type="image/x-icon" href="/static/images/favicon.ico">
<link rel="apple-touch-icon" sizes="180x180" href="/static/images/apple-touch-icon.png">
```

### Open Graph Images

**og-image.png**
- Dimensions: 1200×630px
- Format: PNG
- File size: <300KB
- Content: Logo + tagline on branded background

**HTML Implementation:**
```html
<meta property="og:image" content="https://example.com/static/images/og-image.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
```

---

## File Naming Conventions

### General Rules

**Pattern:** `{category}-{descriptor}-{variant}.{ext}`

**Conventions:**
- Use lowercase
- Separate words with hyphens
- Be descriptive but concise
- Include version if multiple iterations exist

### Examples

**CSS Files:**
```
base.css
layout.css
components.css
playground.css
responsive.css
```

**JavaScript Files:**
```
utils.js
three-background.js
vector-canvas.js
calculators.js
init.js
```

**Logo Files:**
```
gatormath-logo-primary.svg
gatormath-logo-light.svg
gatormath-icon-monochrome.svg
gatormath-wordmark-dark.svg
```

**Image Files:**
```
og-image.png
hero-background.jpg
calculator-screenshot.png
architecture-diagram-v2.svg
```

---

## Optimization Guidelines

### CSS Optimization

**Development:**
```css
/* Readable, commented, verbose */
.calculator-button {
  background-color: var(--color-gator-green);
  border-radius: 0.5rem;
  padding: 0.75rem 1.5rem;
  /* More properties... */
}
```

**Production:**
- Minify with cssnano or clean-css
- Remove comments
- Combine media queries
- Remove unused CSS (PurgeCSS)

**Build Command:**
```bash
npx cssnano base.css base.min.css
```

### JavaScript Optimization

**Development:**
```javascript
// Readable, commented, verbose
export async function calculateTriangleArea(a, b, c) {
  const response = await fetch('/api/geometry/triangle', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ a, b, c })
  });
  return await response.json();
}
```

**Production:**
- Minify with Terser or UglifyJS
- Tree-shake unused code
- Bundle with Rollup or Webpack (optional)

**Build Command:**
```bash
npx terser calculators.js -o calculators.min.js -c -m
```

### SVG Optimization

**Before:**
```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- Generator: Adobe Illustrator -->
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100">
  <metadata>...</metadata>
  <path d="M 10 10 L 90 10 L 90 90 L 10 90 Z" fill="#2D5016"/>
</svg>
```

**After (SVGO):**
```xml
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100">
  <path d="M10 10h80v80H10z" fill="#2D5016"/>
</svg>
```

**Optimization Tools:**
- SVGO CLI: `svgo logo.svg -o logo-optimized.svg`
- SVGOMG (web): https://jakearchibald.github.io/svgomg/

**Optimization Steps:**
1. Remove unnecessary metadata
2. Simplify paths
3. Remove invisible elements
4. Reduce decimal precision
5. Combine paths where possible
6. Remove default values

### Image Optimization

**PNG:**
- Use TinyPNG or ImageOptim
- Target: <100KB for icons, <300KB for OG images

**JPG:**
- Quality: 80-85% for photos
- Progressive encoding
- Target: <200KB for hero images

**WebP (Modern Alternative):**
- Better compression than PNG/JPG
- Serve with fallback for older browsers

**HTML Implementation:**
```html
<picture>
  <source srcset="hero.webp" type="image/webp">
  <img src="hero.jpg" alt="Hero image">
</picture>
```

---

## Version Control

### Tracked Assets

**Always commit:**
- Source SVG files
- Unminified CSS/JS
- Documentation assets
- Brand files

**Never commit:**
- Minified files (generate in build)
- Temporary files
- Very large binaries (>10MB)
- Generated favicons (if scripted)

### .gitignore Patterns

```gitignore
# Minified assets
*.min.css
*.min.js

# Build outputs
gatormath/web/static/dist/

# Temporary files
*.tmp
*.cache

# OS files
.DS_Store
Thumbs.db
```

### Asset Versioning

**For Major Changes:**
```
gatormath-logo-v1.svg
gatormath-logo-v2.svg
gatormath-logo-v3.svg
```

**Current Version:**
```
gatormath-logo.svg → gatormath-logo-v3.svg (symlink)
```

---

## Usage Guidelines

### Loading Assets in HTML

**CSS Loading:**
```html
<!-- Development -->
<link rel="stylesheet" href="{{ url_for('static', filename='css/base.css') }}">
<link rel="stylesheet" href="{{ url_for('static', filename='css/layout.css') }}">

<!-- Production -->
<link rel="stylesheet" href="{{ url_for('static', filename='css/main.min.css') }}">
```

**JavaScript Loading:**
```html
<!-- Defer for non-critical JS -->
<script defer src="{{ url_for('static', filename='js/animations.js') }}"></script>

<!-- Module type for ES6 -->
<script type="module" src="{{ url_for('static', filename='js/init.js') }}"></script>
```

### Asset Loading Best Practices

**Critical CSS:**
- Inline critical CSS in `<head>`
- Load remaining CSS asynchronously
- Minimize render-blocking resources

**JavaScript Loading Strategies:**
- `defer`: Load after HTML parsing (order preserved)
- `async`: Load and execute ASAP (order not guaranteed)
- `type="module"`: ES6 modules with automatic defer

**Image Loading:**
```html
<!-- Lazy loading -->
<img src="image.jpg" loading="lazy" alt="Description">

<!-- Responsive images -->
<img srcset="image-320.jpg 320w,
             image-640.jpg 640w,
             image-1280.jpg 1280w"
     sizes="(max-width: 640px) 320px,
            (max-width: 1280px) 640px,
            1280px"
     src="image-640.jpg" alt="Description">
```

### Cache Busting

**Query String Method:**
```html
<link rel="stylesheet" href="/static/css/main.css?v=0.1.0">
```

**Filename Hash Method (Preferred):**
```html
<link rel="stylesheet" href="/static/css/main.a1b2c3d4.css">
```

**Flask Implementation:**
```python
from flask import url_for
import hashlib

def asset_url(filename):
    filepath = os.path.join(app.static_folder, filename)
    with open(filepath, 'rb') as f:
        file_hash = hashlib.md5(f.read()).hexdigest()[:8]
    return url_for('static', filename=f'{filename}?v={file_hash}')
```

### CDN Usage

**External Libraries:**
```html
<!-- Three.js from CDN -->
<script src="https://cdn.jsdelivr.net/npm/three@0.160.0/build/three.min.js"></script>

<!-- GSAP from CDN -->
<script src="https://cdn.jsdelivr.net/npm/gsap@3.12.0/dist/gsap.min.js"></script>

<!-- With integrity check -->
<script
  src="https://cdn.jsdelivr.net/npm/three@0.160.0/build/three.min.js"
  integrity="sha384-..."
  crossorigin="anonymous"></script>
```

**Self-Hosted (Preferred for Production):**
- Better control over versions
- No external dependencies
- Faster load times (same domain)
- Works offline in development

---

## Asset Performance Checklist

### CSS
- [ ] Minified and concatenated
- [ ] Critical CSS inlined
- [ ] Unused CSS removed
- [ ] Media queries combined
- [ ] File size <50KB (uncompressed)

### JavaScript
- [ ] Minified and bundled
- [ ] Tree-shaken (unused code removed)
- [ ] Deferred or async loading
- [ ] Code split by route/feature
- [ ] File size <100KB per bundle

### Images
- [ ] Optimized with appropriate tools
- [ ] Correct format (SVG > WebP > PNG > JPG)
- [ ] Lazy loading implemented
- [ ] Responsive images with srcset
- [ ] Alt text provided

### Fonts
- [ ] Subset to used characters (if custom)
- [ ] WOFF2 format (best compression)
- [ ] font-display: swap (avoid FOIT)
- [ ] Preload critical fonts

### SVG
- [ ] Optimized with SVGO
- [ ] Inline for small icons (<2KB)
- [ ] External file for large graphics
- [ ] Accessible (title, aria-label)

---

**Version:** 0.1.0
**See Also:** [Branding](BRANDING.md) | [Development Guide](DEVELOPMENT.md) | [Standards](STANDARDS.md)
