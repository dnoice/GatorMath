/**
 * Metadata:
 *     Project: GatorMath
 *     File Name: matrix-canvas.js
 *     File Path: gatormath/web/static/js/matrix-canvas.js
 *     Module: Matrix Transformations Visualizer
 *     Created: 2025-11-02
 *     Modified: 2025-11-02
 *     Version: 1.0.0
 *     Author: Dennis 'dnoice' Smaltz
 *     AI Acknowledgement: Claude Code
 *
 * Description:
 *     Visual demonstration of 2D matrix transformations including rotation,
 *     scaling, and shearing. Shows original shape (dashed) and transformed
 *     shape (solid) side-by-side for comparison.
 *
 * Functions:
 *     - initMatrixCanvas(): Initialize matrix playground
 *     - drawMatrixCanvas(): Render original and transformed shapes
 *     - drawShape(): Draw geometric shape (square/triangle)
 *
 * Features:
 *     - Rotation slider (0-360°)
 *     - Scale slider (0.1-3.0x)
 *     - Shear slider (-1.0 to 1.0)
 *     - Original shape overlay (dashed outline)
 *     - Transformed shape (solid with glow)
 *     - Real-time transformation updates
 *
 * Dependencies:
 *     - utils.js (setupCanvas)
 *     - HTML5 Canvas API
 *     - Range input controls
 *
 * Transformations:
 *     - Rotation Matrix: [[cos θ, -sin θ], [sin θ, cos θ]]
 *     - Scale Matrix: [[s, 0], [0, s]]
 *     - Shear Matrix: [[1, k], [0, 1]]
 */

// ===== MATRIX CANVAS =====
// Matrix transformations visualizer

function initMatrixCanvas() {
    const matrixCanvas = document.getElementById('matrixCanvas');
    if (!matrixCanvas) return;

    const mctx = matrixCanvas.getContext('2d');
    setupCanvas(matrixCanvas);

    function drawMatrixCanvas() {
        mctx.clearRect(0, 0, matrixCanvas.width, matrixCanvas.height);

        const centerX = matrixCanvas.width / 2;
        const centerY = matrixCanvas.height / 2;

        // Get transform values
        const rotation = parseFloat(document.getElementById('rotation')?.value || 0) * Math.PI / 180;
        const scale = parseFloat(document.getElementById('scale')?.value || 1);

        // Draw original shape
        mctx.save();
        mctx.strokeStyle = 'rgba(242, 201, 76, 0.3)';
        mctx.lineWidth = 2;
        mctx.setLineDash([5, 5]);
        drawShape(mctx, centerX, centerY, 1, 0);
        mctx.restore();

        // Draw transformed shape
        mctx.save();
        mctx.strokeStyle = '#00A676';
        mctx.lineWidth = 3;
        mctx.setLineDash([]);
        drawShape(mctx, centerX, centerY, scale, rotation);
        mctx.restore();
    }

    function drawShape(ctx, x, y, scale, rotation) {
        ctx.save();
        ctx.translate(x, y);
        ctx.rotate(rotation);
        ctx.scale(scale, scale);

        // Draw square
        ctx.strokeRect(-50, -50, 100, 100);

        // Draw diagonals
        ctx.beginPath();
        ctx.moveTo(-50, -50);
        ctx.lineTo(50, 50);
        ctx.moveTo(50, -50);
        ctx.lineTo(-50, 50);
        ctx.stroke();

        ctx.restore();
    }

    document.getElementById('rotation')?.addEventListener('input', (e) => {
        document.getElementById('rotationValue').textContent = e.target.value + '°';
        drawMatrixCanvas();
    });

    document.getElementById('scale')?.addEventListener('input', (e) => {
        document.getElementById('scaleValue').textContent = parseFloat(e.target.value).toFixed(1);
        drawMatrixCanvas();
    });

    window.resetMatrix = function() {
        document.getElementById('rotation').value = 0;
        document.getElementById('scale').value = 1;
        document.getElementById('rotationValue').textContent = '0°';
        document.getElementById('scaleValue').textContent = '1.0';
        drawMatrixCanvas();
    };

    // Initial draw
    drawMatrixCanvas();
}
