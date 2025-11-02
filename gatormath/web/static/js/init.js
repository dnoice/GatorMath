/**
 * Metadata:
 *     Project: GatorMath
 *     File Name: init.js
 *     File Path: gatormath/web/static/js/init.js
 *     Module: Application Initialization
 *     Created: 2025-11-02
 *     Modified: 2025-11-02
 *     Version: 1.0.0
 *     Author: Dennis 'dnoice' Smaltz
 *     AI Acknowledgement: Claude Code
 *
 * Description:
 *     Main initialization logic that orchestrates all interactive components.
 *     Waits for DOM to be fully loaded and initializes all canvas-based
 *     playgrounds (vector, Bezier, matrix, triangle).
 *
 * Functions:
 *     - initializePlaygrounds(): Initialize all interactive canvases
 *
 * Dependencies:
 *     - vector-canvas.js (initVectorCanvas)
 *     - bezier-canvas.js (initBezierCanvas)
 *     - matrix-canvas.js (initMatrixCanvas)
 *     - triangle-canvas.js (initTriangleCanvas)
 *
 * Events:
 *     - DOMContentLoaded: Triggers playground initialization
 */

// ===== INITIALIZATION =====
// Main initialization logic that ties everything together

// Wait for DOM to be fully loaded
document.addEventListener('DOMContentLoaded', function() {
    initializePlaygrounds();
});

function initializePlaygrounds() {
    // Initialize all canvases
    initVectorCanvas();
    initBezierCanvas();
    initMatrixCanvas();
    initTriangleCanvas();
}
