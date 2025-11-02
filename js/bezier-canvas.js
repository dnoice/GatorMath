// ===== BEZIER CANVAS =====
// Bezier curve editor with animation

function initBezierCanvas() {
    const bezierCanvas = document.getElementById('bezierCanvas');
    if (!bezierCanvas) return;

    const bctx = bezierCanvas.getContext('2d');
    let bezierPoints = [
        { x: 50, y: 300 },
        { x: 150, y: 50 },
        { x: 300, y: 50 },
        { x: 400, y: 300 }
    ];
    let draggingBezier = null;
    let animT = 0;

    setupCanvas(bezierCanvas);

    function drawBezierCanvas() {
        bctx.clearRect(0, 0, bezierCanvas.width, bezierCanvas.height);

        // Draw control lines
        bctx.strokeStyle = 'rgba(242, 201, 76, 0.3)';
        bctx.lineWidth = 1;
        bctx.setLineDash([5, 5]);
        bctx.beginPath();
        bctx.moveTo(bezierPoints[0].x, bezierPoints[0].y);
        bctx.lineTo(bezierPoints[1].x, bezierPoints[1].y);
        bctx.lineTo(bezierPoints[2].x, bezierPoints[2].y);
        bctx.lineTo(bezierPoints[3].x, bezierPoints[3].y);
        bctx.stroke();
        bctx.setLineDash([]);

        // Draw curve
        bctx.strokeStyle = '#00A676';
        bctx.lineWidth = 3;
        bctx.beginPath();
        bctx.moveTo(bezierPoints[0].x, bezierPoints[0].y);
        bctx.bezierCurveTo(
            bezierPoints[1].x, bezierPoints[1].y,
            bezierPoints[2].x, bezierPoints[2].y,
            bezierPoints[3].x, bezierPoints[3].y
        );
        bctx.stroke();

        // Draw control points
        bezierPoints.forEach((point, index) => {
            bctx.fillStyle = index === 0 || index === 3 ? '#00A676' : '#F2C94C';
            bctx.beginPath();
            bctx.arc(point.x, point.y, 8, 0, Math.PI * 2);
            bctx.fill();
        });

        // Draw animated point
        const t = animT;
        const point = cubicBezier(t, bezierPoints);
        bctx.fillStyle = '#F2C94C';
        bctx.shadowBlur = 20;
        bctx.shadowColor = '#F2C94C';
        bctx.beginPath();
        bctx.arc(point.x, point.y, 10, 0, Math.PI * 2);
        bctx.fill();
        bctx.shadowBlur = 0;
    }

    function cubicBezier(t, points) {
        const t2 = t * t;
        const t3 = t2 * t;
        const mt = 1 - t;
        const mt2 = mt * mt;
        const mt3 = mt2 * mt;

        return {
            x: mt3 * points[0].x + 3 * mt2 * t * points[1].x +
               3 * mt * t2 * points[2].x + t3 * points[3].x,
            y: mt3 * points[0].y + 3 * mt2 * t * points[1].y +
               3 * mt * t2 * points[2].y + t3 * points[3].y
        };
    }

    bezierCanvas.addEventListener('mousedown', (e) => {
        const rect = bezierCanvas.getBoundingClientRect();
        const mouseX = e.clientX - rect.left;
        const mouseY = e.clientY - rect.top;

        bezierPoints.forEach((point, index) => {
            const dist = Math.sqrt((mouseX - point.x) ** 2 + (mouseY - point.y) ** 2);
            if (dist < 20) draggingBezier = index;
        });
    });

    bezierCanvas.addEventListener('mousemove', (e) => {
        if (draggingBezier === null) return;

        const rect = bezierCanvas.getBoundingClientRect();
        bezierPoints[draggingBezier].x = e.clientX - rect.left;
        bezierPoints[draggingBezier].y = e.clientY - rect.top;
        drawBezierCanvas();
    });

    bezierCanvas.addEventListener('mouseup', () => {
        draggingBezier = null;
    });

    // Touch support
    bezierCanvas.addEventListener('touchstart', (e) => {
        e.preventDefault();
        const rect = bezierCanvas.getBoundingClientRect();
        const touch = e.touches[0];
        const mouseX = touch.clientX - rect.left;
        const mouseY = touch.clientY - rect.top;

        bezierPoints.forEach((point, index) => {
            const dist = Math.sqrt((mouseX - point.x) ** 2 + (mouseY - point.y) ** 2);
            if (dist < 30) draggingBezier = index;
        });
    });

    bezierCanvas.addEventListener('touchmove', (e) => {
        e.preventDefault();
        if (draggingBezier === null) return;

        const rect = bezierCanvas.getBoundingClientRect();
        const touch = e.touches[0];
        bezierPoints[draggingBezier].x = touch.clientX - rect.left;
        bezierPoints[draggingBezier].y = touch.clientY - rect.top;
        drawBezierCanvas();
    });

    bezierCanvas.addEventListener('touchend', () => {
        draggingBezier = null;
    });

    const speedSlider = document.getElementById('bezierSpeed');
    if (speedSlider) {
        speedSlider.addEventListener('input', (e) => {
            document.getElementById('speedValue').textContent = e.target.value + 'x';
        });
    }

    window.resetBezier = function() {
        bezierPoints = [
            { x: 50, y: 300 },
            { x: 150, y: 50 },
            { x: 300, y: 50 },
            { x: 400, y: 300 }
        ];
        drawBezierCanvas();
    };

    function animateBezier() {
        const speed = parseFloat(document.getElementById('bezierSpeed')?.value || 1);
        animT += 0.005 * speed;
        if (animT > 1) animT = 0;
        drawBezierCanvas();
        requestAnimationFrame(animateBezier);
    }

    // Initial draw and start animation
    drawBezierCanvas();
    animateBezier();
}
