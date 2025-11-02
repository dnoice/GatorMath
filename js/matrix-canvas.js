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
