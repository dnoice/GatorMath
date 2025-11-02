/**
 * Metadata:
 *     Project: GatorMath
 *     File Name: utils.js
 *     File Path: gatormath/web/static/js/utils.js
 *     Module: Utility Functions
 *     Created: 2025-11-02
 *     Modified: 2025-11-02
 *     Version: 1.0.0
 *     Author: Dennis 'dnoice' Smaltz
 *     AI Acknowledgement: Claude Code
 *
 * Description:
 *     Shared utility functions used across different canvas modules and
 *     interactive components. Provides canvas setup with retina scaling,
 *     navigation menu toggling, and welcome tooltip management.
 *
 * Exports (Global):
 *     - setupCanvas(canvas): Canvas setup with retina display support
 *     - window.toggleMenu(): Hamburger menu toggle
 *     - window.closeWelcome(): Welcome tooltip dismiss with localStorage
 *
 * Dependencies:
 *     - HTML5 Canvas API
 *     - localStorage API
 *
 * Functions:
 *     - setupCanvas: Configures canvas for high-DPI displays
 *     - toggleMenu: Toggles mobile navigation menu
 *     - closeWelcome: Dismisses welcome tooltip with animation
 */

// ===== UTILITY FUNCTIONS =====
// Shared utility functions used across different modules

// Global canvas setup function
function setupCanvas(canvas) {
    const rect = canvas.getBoundingClientRect();
    const width = rect.width || canvas.offsetWidth || 400;
    const height = rect.height || canvas.offsetHeight || 400;

    // Set display size (css pixels)
    canvas.style.width = width + 'px';
    canvas.style.height = height + 'px';

    // Set actual size in memory (scaled for retina)
    const scale = window.devicePixelRatio || 1;
    canvas.width = width * scale;
    canvas.height = height * scale;

    // Normalize coordinate system
    const ctx = canvas.getContext('2d');
    ctx.scale(scale, scale);

    return { width, height };
}

// Hamburger menu toggle
window.toggleMenu = function() {
    const navLinks = document.getElementById('navLinks');
    const hamburger = document.getElementById('hamburger');
    navLinks.classList.toggle('active');
    hamburger.classList.toggle('active');
};

// Welcome tooltip
window.closeWelcome = function() {
    const tooltip = document.getElementById('welcomeTooltip');
    tooltip.style.animation = 'slideIn 0.3s ease-out reverse';
    setTimeout(() => {
        tooltip.style.display = 'none';
    }, 300);
    localStorage.setItem('gatormath_visited', 'true');
};
