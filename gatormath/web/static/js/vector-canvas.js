/**
 * Metadata:
 *     Project: GatorMath
 *     File Name: vector-canvas.js
 *     File Path: gatormath/web/static/js/vector-canvas.js
 *     Module: Vector Operations Canvas
 *     Created: 2025-11-02
 *     Modified: 2025-11-02
 *     Version: 1.0.0
 *     Author: Dennis 'dnoice' Smaltz
 *     AI Acknowledgement: Claude Code
 *
 * Description:
 *     Interactive vector operations playground with draggable vectors.
 *     Visualizes addition, subtraction, dot product, cross product, and
 *     magnitude calculations in real-time on HTML5 canvas.
 *
 * Functions:
 *     - initVectorCanvas(): Initialize vector playground
 *     - drawVectorCanvas(): Render vectors and grid
 *     - drawVector(): Draw arrow from origin to point
 *     - getVectorMagnitude(): Calculate vector length
 *
 * Features:
 *     - Draggable vector endpoints
 *     - Grid background (50px spacing)
 *     - Operation buttons (add, subtract, dot, cross, magnitude)
 *     - Real-time result visualization
 *     - Mouse/touch interaction support
 *
 * Dependencies:
 *     - utils.js (setupCanvas)
 *     - HTML5 Canvas API
 *
 * Operations:
 *     - Addition: v1 + v2
 *     - Subtraction: v1 - v2
 *     - Dot Product: v1 · v2
 *     - Cross Product: v1 × v2 (2D cross product)
 *     - Magnitude: |v|
 */

// ===== VECTOR CANVAS =====
// Vector operations interactive playground

function initVectorCanvas() {
    const vectorCanvas = document.getElementById('vectorCanvas');
    if (!vectorCanvas) return;

    const vctx = vectorCanvas.getContext('2d');
    let vectorA = { x: 100, y: 100 };
    let vectorB = { x: 250, y: 150 };
    let draggingVector = null;
    let resultVector = null;
    let currentOperation = null;

    const dims = setupCanvas(vectorCanvas);

    function drawVectorCanvas() {
        const width = vectorCanvas.width / (window.devicePixelRatio || 1);
        const height = vectorCanvas.height / (window.devicePixelRatio || 1);

        vctx.clearRect(0, 0, width, height);

        // Draw grid
        vctx.strokeStyle = 'rgba(0, 166, 118, 0.1)';
        vctx.lineWidth = 1;
        for (let i = 0; i < width; i += 50) {
            vctx.beginPath();
            vctx.moveTo(i, 0);
            vctx.lineTo(i, height);
            vctx.stroke();
        }
        for (let i = 0; i < height; i += 50) {
            vctx.beginPath();
            vctx.moveTo(0, i);
            vctx.lineTo(width, i);
            vctx.stroke();
        }

        // Draw origin
        const originX = width / 2;
        const originY = height / 2;

        vctx.fillStyle = '#F2C94C';
        vctx.beginPath();
        vctx.arc(originX, originY, 5, 0, Math.PI * 2);
        vctx.fill();

        // Draw result vector if exists
        if (resultVector) {
            drawVector(vctx, originX, originY, resultVector.x, resultVector.y, '#F2C94C', 'R', true);
        }

        // Draw vectors
        drawVector(vctx, originX, originY, vectorA.x, vectorA.y, '#00A676', 'A');
        drawVector(vctx, originX, originY, vectorB.x, vectorB.y, '#50fa7b', 'B');

        // Update calculations
        updateVectorCalculations();
    }

    function drawVector(ctx, startX, startY, endX, endY, color, label, dashed = false) {
        ctx.strokeStyle = color;
        ctx.fillStyle = color;
        ctx.lineWidth = 3;

        if (dashed) {
            ctx.setLineDash([10, 5]);
        }

        // Arrow line
        ctx.beginPath();
        ctx.moveTo(startX, startY);
        ctx.lineTo(startX + endX, startY + endY);
        ctx.stroke();

        if (dashed) {
            ctx.setLineDash([]);
        }

        // Arrowhead
        const angle = Math.atan2(endY, endX);
        const headlen = 15;
        ctx.beginPath();
        ctx.moveTo(startX + endX, startY + endY);
        ctx.lineTo(
            startX + endX - headlen * Math.cos(angle - Math.PI / 6),
            startY + endY - headlen * Math.sin(angle - Math.PI / 6)
        );
        ctx.lineTo(
            startX + endX - headlen * Math.cos(angle + Math.PI / 6),
            startY + endY - headlen * Math.sin(angle + Math.PI / 6)
        );
        ctx.closePath();
        ctx.fill();

        // Control point (only for A and B, not result)
        if (!dashed) {
            ctx.beginPath();
            ctx.arc(startX + endX, startY + endY, 8, 0, Math.PI * 2);
            ctx.fill();
        }

        // Label
        ctx.font = 'bold 16px Inter';
        ctx.fillText(label, startX + endX + 15, startY + endY - 10);
    }

    function updateVectorCalculations() {
        document.getElementById('vectorA').textContent =
            `(${vectorA.x.toFixed(0)}, ${vectorA.y.toFixed(0)})`;
        document.getElementById('vectorB').textContent =
            `(${vectorB.x.toFixed(0)}, ${vectorB.y.toFixed(0)})`;

        const magA = Math.sqrt(vectorA.x ** 2 + vectorA.y ** 2);
        const magB = Math.sqrt(vectorB.x ** 2 + vectorB.y ** 2);

        document.getElementById('magA').textContent = magA.toFixed(2);
        document.getElementById('magB').textContent = magB.toFixed(2);

        const dot = vectorA.x * vectorB.x + vectorA.y * vectorB.y;
        document.getElementById('dotProduct').textContent = dot.toFixed(2);

        const angleRad = Math.acos(dot / (magA * magB));
        const angleDeg = (angleRad * 180 / Math.PI) || 0;
        document.getElementById('angle').textContent = angleDeg.toFixed(1) + '°';
    }

    window.vectorOperation = function(operation) {
        currentOperation = operation;
        const resultDisplay = document.getElementById('operationResult');

        // Clear previous active buttons
        document.querySelectorAll('.op-btn').forEach(btn => btn.classList.remove('active'));
        event.target.classList.add('active');

        switch(operation) {
            case 'add':
                resultVector = {
                    x: vectorA.x + vectorB.x,
                    y: vectorA.y + vectorB.y
                };
                resultDisplay.innerHTML = `<span>Result (A + B):</span> (${resultVector.x.toFixed(0)}, ${resultVector.y.toFixed(0)})`;
                break;

            case 'subtract':
                resultVector = {
                    x: vectorA.x - vectorB.x,
                    y: vectorA.y - vectorB.y
                };
                resultDisplay.innerHTML = `<span>Result (A - B):</span> (${resultVector.x.toFixed(0)}, ${resultVector.y.toFixed(0)})`;
                break;

            case 'dot':
                const dot = vectorA.x * vectorB.x + vectorA.y * vectorB.y;
                resultVector = null;
                resultDisplay.innerHTML = `<span>Dot Product:</span> ${dot.toFixed(2)}`;
                break;

            case 'cross':
                // For 2D, cross product gives scalar (z-component)
                const cross = vectorA.x * vectorB.y - vectorA.y * vectorB.x;
                resultVector = null;
                resultDisplay.innerHTML = `<span>Cross Product (z):</span> ${cross.toFixed(2)}`;
                break;

            case 'normalize':
                const magA = Math.sqrt(vectorA.x ** 2 + vectorA.y ** 2);
                if (magA > 0) {
                    resultVector = {
                        x: (vectorA.x / magA) * 100, // Scale for visibility
                        y: (vectorA.y / magA) * 100
                    };
                    resultDisplay.innerHTML = `<span>Normalized A:</span> (${(vectorA.x/magA).toFixed(3)}, ${(vectorA.y/magA).toFixed(3)})`;
                }
                break;

            case 'scale':
                resultVector = {
                    x: vectorA.x * 2,
                    y: vectorA.y * 2
                };
                resultDisplay.innerHTML = `<span>Scaled A (2×):</span> (${resultVector.x.toFixed(0)}, ${resultVector.y.toFixed(0)})`;
                break;
        }

        drawVectorCanvas();
    };

    vectorCanvas.addEventListener('mousedown', (e) => {
        const rect = vectorCanvas.getBoundingClientRect();
        const width = vectorCanvas.width / (window.devicePixelRatio || 1);
        const height = vectorCanvas.height / (window.devicePixelRatio || 1);
        const mouseX = e.clientX - rect.left - width / 2;
        const mouseY = e.clientY - rect.top - height / 2;

        const distA = Math.sqrt((mouseX - vectorA.x) ** 2 + (mouseY - vectorA.y) ** 2);
        const distB = Math.sqrt((mouseX - vectorB.x) ** 2 + (mouseY - vectorB.y) ** 2);

        if (distA < 20) draggingVector = 'A';
        else if (distB < 20) draggingVector = 'B';
    });

    vectorCanvas.addEventListener('mousemove', (e) => {
        if (!draggingVector) return;

        const rect = vectorCanvas.getBoundingClientRect();
        const width = vectorCanvas.width / (window.devicePixelRatio || 1);
        const height = vectorCanvas.height / (window.devicePixelRatio || 1);
        const mouseX = e.clientX - rect.left - width / 2;
        const mouseY = e.clientY - rect.top - height / 2;

        if (draggingVector === 'A') {
            vectorA.x = mouseX;
            vectorA.y = mouseY;
        } else if (draggingVector === 'B') {
            vectorB.x = mouseX;
            vectorB.y = mouseY;
        }

        // Recalculate operation if one is active
        if (currentOperation) {
            const activeBtn = document.querySelector('.op-btn.active');
            if (activeBtn) {
                vectorOperation(currentOperation);
            }
        }

        drawVectorCanvas();
    });

    vectorCanvas.addEventListener('mouseup', () => {
        draggingVector = null;
    });

    vectorCanvas.addEventListener('mouseleave', () => {
        draggingVector = null;
    });

    // Touch support for mobile
    vectorCanvas.addEventListener('touchstart', (e) => {
        e.preventDefault();
        const rect = vectorCanvas.getBoundingClientRect();
        const width = vectorCanvas.width / (window.devicePixelRatio || 1);
        const height = vectorCanvas.height / (window.devicePixelRatio || 1);
        const touch = e.touches[0];
        const mouseX = touch.clientX - rect.left - width / 2;
        const mouseY = touch.clientY - rect.top - height / 2;

        const distA = Math.sqrt((mouseX - vectorA.x) ** 2 + (mouseY - vectorA.y) ** 2);
        const distB = Math.sqrt((mouseX - vectorB.x) ** 2 + (mouseY - vectorB.y) ** 2);

        if (distA < 30) draggingVector = 'A';
        else if (distB < 30) draggingVector = 'B';
    });

    vectorCanvas.addEventListener('touchmove', (e) => {
        e.preventDefault();
        if (!draggingVector) return;

        const rect = vectorCanvas.getBoundingClientRect();
        const width = vectorCanvas.width / (window.devicePixelRatio || 1);
        const height = vectorCanvas.height / (window.devicePixelRatio || 1);
        const touch = e.touches[0];
        const mouseX = touch.clientX - rect.left - width / 2;
        const mouseY = touch.clientY - rect.top - height / 2;

        if (draggingVector === 'A') {
            vectorA.x = mouseX;
            vectorA.y = mouseY;
        } else if (draggingVector === 'B') {
            vectorB.x = mouseX;
            vectorB.y = mouseY;
        }

        if (currentOperation) {
            vectorOperation(currentOperation);
        }

        drawVectorCanvas();
    });

    vectorCanvas.addEventListener('touchend', () => {
        draggingVector = null;
    });

    window.resetVectors = function() {
        vectorA = { x: 100, y: 100 };
        vectorB = { x: 250, y: 150 };
        resultVector = null;
        currentOperation = null;
        document.querySelectorAll('.op-btn').forEach(btn => btn.classList.remove('active'));
        document.getElementById('operationResult').innerHTML = '';
        drawVectorCanvas();
    };

    // Initial draw
    drawVectorCanvas();
}
