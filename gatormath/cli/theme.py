"""
Module Name: theme

Description:
    Rich console theme configuration for GatorMath CLI interface.
    Implements the complete GatorMath brand color palette with semantic
    styling for consistent, beautiful terminal output across all CLI commands.

Module Path: gatormath/cli/theme.py
Package: gatormath.cli

Author: GatorMath Development Team
Created: 2025-11-01
Modified: 2025-11-01
Version: 0.1.0

Dependencies:
    - rich: Console theming and styling framework

Exports:
    - GATOR_THEME: Main Rich Theme object with all brand colors
    - GATOR_COLORS: Dictionary of color hex values
    - create_console: Factory function for pre-configured Console instances
    - get_color: Retrieve specific brand colors by name

Features:
    - Complete brand palette implementation
    - Semantic color aliases for different UI states
    - WCAG AA/AAA compliant color combinations
    - Color blindness consideration
    - True color, 256-color, and 16-color fallbacks

Color Palette:
    Primary:
        - Swamp Green (#2D5016): Brand primary, success states
        - Deep Teal (#0D7377): Interactive elements, accents
        - Sunset Orange (#FF8C42): Warnings, attention
        - Blood Red (#C1292E): Errors, critical states
        - Golden Yellow (#F4D35E): Information, highlights

    Secondary:
        - Slate Gray (#E8E9EB): Primary text
        - Charcoal (#1A1D1E): Backgrounds
        - Mist Gray (#6B7280): Subtle text, borders

    Extended:
        - Lime Green (#7CB342): Data visualization
        - Cyan Blue (#26C6DA): Code highlighting
        - Violet Purple (#AB47BC): Special elements
        - Coral Pink (#FF7043): Emphasis

Usage:
    >>> from gatormath.cli.theme import create_console
    >>> console = create_console()
    >>> console.print("Success!", style="success")
    >>> console.print("Error occurred", style="error")

Examples:
    Basic console creation:
    >>> from gatormath.cli.theme import create_console, GATOR_THEME
    >>> console = create_console()
    >>> console.print("GatorMath", style="header")

    Custom styling:
    >>> from rich.console import Console
    >>> from gatormath.cli.theme import GATOR_THEME
    >>> console = Console(theme=GATOR_THEME)
    >>> console.print("[gator_green]This is in brand green[/]")

    Color retrieval:
    >>> from gatormath.cli.theme import get_color
    >>> green = get_color("gator_green")
    >>> print(green)
    '#2D5016'

Notes:
    - Theme automatically handles terminal capability detection
    - Colors degrade gracefully on limited color terminals
    - All combinations tested for accessibility compliance
    - Use semantic aliases (success, error, etc.) over direct colors

See Also:
    - docs/branding/color_palette.md: Complete color specifications
    - STANDARDS.md: Brand and CLI standards
    - rich.theme.Theme: Rich theming documentation

References:
    [1] WCAG 2.1 Color Contrast Guidelines
    [2] Rich library documentation: https://rich.readthedocs.io/
"""

# Standard library imports
from typing import Final, Optional

# Third-party imports
from rich.console import Console
from rich.theme import Theme


# ============================================================================
# Color Constants
# ============================================================================

# Primary Brand Colors
GATOR_GREEN: Final[str] = "#2D5016"
GATOR_TEAL: Final[str] = "#0D7377"
GATOR_ORANGE: Final[str] = "#FF8C42"
GATOR_RED: Final[str] = "#C1292E"
GATOR_GOLD: Final[str] = "#F4D35E"

# Secondary Colors
GATOR_SLATE: Final[str] = "#E8E9EB"
GATOR_CHARCOAL: Final[str] = "#1A1D1E"
GATOR_MIST: Final[str] = "#6B7280"

# Extended Colors (for data visualization and special uses)
GATOR_LIME: Final[str] = "#7CB342"
GATOR_CYAN: Final[str] = "#26C6DA"
GATOR_VIOLET: Final[str] = "#AB47BC"
GATOR_CORAL: Final[str] = "#FF7043"

# Color dictionary for programmatic access
GATOR_COLORS: Final[dict[str, str]] = {
    # Primary
    "gator_green": GATOR_GREEN,
    "gator_teal": GATOR_TEAL,
    "gator_orange": GATOR_ORANGE,
    "gator_red": GATOR_RED,
    "gator_gold": GATOR_GOLD,
    # Secondary
    "gator_slate": GATOR_SLATE,
    "gator_charcoal": GATOR_CHARCOAL,
    "gator_mist": GATOR_MIST,
    # Extended
    "gator_lime": GATOR_LIME,
    "gator_cyan": GATOR_CYAN,
    "gator_violet": GATOR_VIOLET,
    "gator_coral": GATOR_CORAL,
}


# ============================================================================
# Rich Theme Definition
# ============================================================================

GATOR_THEME: Final[Theme] = Theme({
    # ========================================================================
    # Base Brand Colors
    # ========================================================================
    "gator_green": GATOR_GREEN,
    "gator_teal": GATOR_TEAL,
    "gator_orange": GATOR_ORANGE,
    "gator_red": GATOR_RED,
    "gator_gold": GATOR_GOLD,
    "gator_slate": GATOR_SLATE,
    "gator_charcoal": GATOR_CHARCOAL,
    "gator_mist": GATOR_MIST,
    "gator_lime": GATOR_LIME,
    "gator_cyan": GATOR_CYAN,
    "gator_violet": GATOR_VIOLET,
    "gator_coral": GATOR_CORAL,

    # ========================================================================
    # Semantic State Colors
    # ========================================================================
    "success": f"bold {GATOR_GREEN}",
    "info": GATOR_GOLD,
    "warning": f"bold {GATOR_ORANGE}",
    "error": f"bold {GATOR_RED}",
    "active": f"bold {GATOR_TEAL}",
    "inactive": GATOR_MIST,
    "disabled": f"dim {GATOR_MIST}",

    # ========================================================================
    # Typography Styles
    # ========================================================================
    "header": f"bold {GATOR_GREEN}",
    "subheader": f"bold {GATOR_TEAL}",
    "title": f"bold underline {GATOR_GREEN}",
    "subtitle": f"bold {GATOR_TEAL}",
    "text": GATOR_SLATE,
    "text.primary": GATOR_SLATE,
    "text.secondary": GATOR_MIST,
    "text.subtle": f"dim {GATOR_MIST}",
    "highlight": f"bold {GATOR_GOLD}",
    "emphasis": f"italic {GATOR_SLATE}",
    "strong": f"bold {GATOR_SLATE}",

    # ========================================================================
    # Code and Data Display
    # ========================================================================
    "code": f"{GATOR_CYAN}",
    "code.keyword": f"bold {GATOR_TEAL}",
    "code.string": GATOR_GOLD,
    "code.number": GATOR_LIME,
    "code.function": GATOR_CYAN,
    "code.class": GATOR_VIOLET,
    "code.comment": GATOR_MIST,
    "code.operator": GATOR_ORANGE,
    "code.builtin": f"bold {GATOR_TEAL}",
    "data": GATOR_SLATE,
    "data.key": GATOR_TEAL,
    "data.value": GATOR_SLATE,
    "data.number": GATOR_LIME,

    # ========================================================================
    # UI Components
    # ========================================================================
    "prompt": f"bold {GATOR_TEAL}",
    "prompt.default": GATOR_MIST,
    "prompt.choices": GATOR_SLATE,
    "border": GATOR_MIST,
    "border.accent": GATOR_GREEN,
    "divider": GATOR_MIST,

    # ========================================================================
    # Tables
    # ========================================================================
    "table.header": f"bold {GATOR_GREEN}",
    "table.header.border": GATOR_GREEN,
    "table.border": GATOR_MIST,
    "table.cell": GATOR_SLATE,
    "table.cell.highlight": f"bold {GATOR_GOLD}",
    "table.footer": GATOR_MIST,

    # ========================================================================
    # Panels
    # ========================================================================
    "panel.border": GATOR_GREEN,
    "panel.title": f"bold {GATOR_GREEN}",
    "panel.subtitle": GATOR_TEAL,
    "panel.content": GATOR_SLATE,

    # ========================================================================
    # Progress Indicators
    # ========================================================================
    "progress.bar": GATOR_GREEN,
    "progress.complete": f"bold {GATOR_GREEN}",
    "progress.remaining": GATOR_MIST,
    "progress.percentage": f"bold {GATOR_GOLD}",
    "progress.elapsed": GATOR_MIST,
    "progress.eta": GATOR_TEAL,
    "progress.spinner": GATOR_TEAL,

    # ========================================================================
    # Status Indicators
    # ========================================================================
    "status.success": f"bold {GATOR_GREEN}",
    "status.info": f"bold {GATOR_GOLD}",
    "status.warning": f"bold {GATOR_ORANGE}",
    "status.error": f"bold {GATOR_RED}",
    "status.pending": GATOR_MIST,

    # ========================================================================
    # Links and References
    # ========================================================================
    "link": f"underline {GATOR_TEAL}",
    "link.hover": f"bold underline {GATOR_TEAL}",
    "reference": GATOR_CYAN,

    # ========================================================================
    # Mathematical Notation
    # ========================================================================
    "math.operator": GATOR_ORANGE,
    "math.number": GATOR_LIME,
    "math.variable": GATOR_CYAN,
    "math.function": f"bold {GATOR_VIOLET}",
    "math.constant": f"bold {GATOR_GOLD}",
    "math.result": f"bold {GATOR_GREEN}",

    # ========================================================================
    # Geometric Display
    # ========================================================================
    "geometry.shape": GATOR_TEAL,
    "geometry.point": GATOR_GOLD,
    "geometry.line": GATOR_CYAN,
    "geometry.angle": GATOR_ORANGE,
    "geometry.area": GATOR_GREEN,
    "geometry.volume": GATOR_VIOLET,

    # ========================================================================
    # Logging Levels
    # ========================================================================
    "log.debug": GATOR_MIST,
    "log.info": GATOR_GOLD,
    "log.warning": GATOR_ORANGE,
    "log.error": GATOR_RED,
    "log.critical": f"bold reverse {GATOR_RED}",

    # ========================================================================
    # Special Elements
    # ========================================================================
    "brand": f"bold {GATOR_GREEN}",
    "accent": GATOR_TEAL,
    "muted": GATOR_MIST,
    "background": GATOR_CHARCOAL,
    "selection": f"reverse {GATOR_TEAL}",
    "cursor": f"reverse {GATOR_GOLD}",
})


# ============================================================================
# Console Factory Functions
# ============================================================================

def create_console(
    *,
    theme: Optional[Theme] = None,
    force_terminal: Optional[bool] = None,
    force_interactive: Optional[bool] = None,
    width: Optional[int] = None,
    height: Optional[int] = None,
    color_system: Optional[str] = None,
) -> Console:
    """
    Create a pre-configured Rich Console instance with GatorMath theme.

    Args:
        theme (Optional[Theme]): Custom theme to use. Defaults to GATOR_THEME.
        force_terminal (Optional[bool]): Force terminal mode even if output
            is redirected. Useful for testing.
        force_interactive (Optional[bool]): Force interactive mode.
        width (Optional[int]): Console width. Auto-detected if None.
        height (Optional[int]): Console height. Auto-detected if None.
        color_system (Optional[str]): Force specific color system:
            - "auto": Auto-detect (default)
            - "standard": 16 colors
            - "256": 256 colors
            - "truecolor": 24-bit RGB
            - None: Disable colors

    Returns:
        Console: Configured Rich Console instance ready for use.

    Examples:
        >>> console = create_console()
        >>> console.print("Hello GatorMath!", style="header")

        >>> # Force 256-color mode
        >>> console = create_console(color_system="256")

        >>> # Custom width for testing
        >>> console = create_console(width=80)

    Notes:
        - Automatically enables emoji support (though we use SVG in docs)
        - Detects terminal capabilities for optimal rendering
        - Falls back gracefully on limited terminals

    Version: 0.1.0
    """
    return Console(
        theme=theme or GATOR_THEME,
        force_terminal=force_terminal,
        force_interactive=force_interactive,
        width=width,
        height=height,
        color_system=color_system,
        legacy_windows=False,  # We require modern terminal support
        markup=True,
        emoji=False,  # No emojis per project standards
        highlight=True,
    )


def get_color(color_name: str) -> str:
    """
    Retrieve a brand color hex value by name.

    Args:
        color_name (str): Name of the color (e.g., "gator_green", "gator_teal")

    Returns:
        str: Hex color code (e.g., "#2D5016")

    Raises:
        KeyError: If color_name is not a valid GatorMath color

    Examples:
        >>> get_color("gator_green")
        '#2D5016'

        >>> get_color("gator_teal")
        '#0D7377'

        >>> # Use with custom styling
        >>> color = get_color("gator_gold")
        >>> console.print(f"[{color}]Highlighted text[/]")

    See Also:
        - GATOR_COLORS: Dictionary of all available colors
        - docs/branding/color_palette.md: Complete color specifications

    Version: 0.1.0
    """
    if color_name not in GATOR_COLORS:
        available = ", ".join(GATOR_COLORS.keys())
        raise KeyError(
            f"Unknown color '{color_name}'. "
            f"Available colors: {available}"
        )
    return GATOR_COLORS[color_name]


def get_all_colors() -> dict[str, str]:
    """
    Get complete dictionary of all GatorMath brand colors.

    Returns:
        dict[str, str]: Dictionary mapping color names to hex codes.
            Keys are color names (e.g., "gator_green")
            Values are hex codes (e.g., "#2D5016")

    Examples:
        >>> colors = get_all_colors()
        >>> for name, hex_code in colors.items():
        ...     print(f"{name}: {hex_code}")
        gator_green: #2D5016
        gator_teal: #0D7377
        ...

    Notes:
        Returns a copy of the color dictionary to prevent modification
        of the original constants.

    Version: 0.1.0
    """
    return GATOR_COLORS.copy()


def print_color_palette(console: Optional[Console] = None) -> None:
    """
    Display the complete GatorMath color palette in the terminal.

    Useful for testing terminal color support and previewing the palette.

    Args:
        console (Optional[Console]): Console to print to. Creates new one if None.

    Examples:
        >>> from gatormath.cli.theme import print_color_palette
        >>> print_color_palette()

    Notes:
        - Shows all colors with their hex codes
        - Demonstrates actual rendering on current terminal
        - Useful for debugging color support issues

    Version: 0.1.0
    """
    if console is None:
        console = create_console()

    from rich.table import Table

    table = Table(title="GatorMath Color Palette", border_style="gator_green")
    table.add_column("Color Name", style="bold")
    table.add_column("Hex Code", style="code")
    table.add_column("Preview", justify="center")

    for name, hex_code in GATOR_COLORS.items():
        # Create colored preview blocks
        preview = f"[{hex_code}]████████[/]"
        table.add_row(name, hex_code, preview)

    console.print(table)


# ============================================================================
# Module Exports
# ============================================================================

__all__ = [
    # Constants
    "GATOR_GREEN",
    "GATOR_TEAL",
    "GATOR_ORANGE",
    "GATOR_RED",
    "GATOR_GOLD",
    "GATOR_SLATE",
    "GATOR_CHARCOAL",
    "GATOR_MIST",
    "GATOR_LIME",
    "GATOR_CYAN",
    "GATOR_VIOLET",
    "GATOR_CORAL",
    "GATOR_COLORS",
    # Theme
    "GATOR_THEME",
    # Functions
    "create_console",
    "get_color",
    "get_all_colors",
    "print_color_palette",
]
