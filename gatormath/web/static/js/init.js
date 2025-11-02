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
