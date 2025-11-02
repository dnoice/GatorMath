// ===== TRIANGLE CANVAS =====
// Triangle calculator with area, perimeter, and angles

function initTriangleCanvas() {
    const triangleCanvas = document.getElementById('triangleCanvas');
    if (!triangleCanvas) return;

    const tctx = triangleCanvas.getContext('2d');
    let trianglePoints = [
        { x: 200, y: 50 },
        { x: 350, y: 300 },
        { x: 50, y: 300 }
    ];
    let draggingTriangle = null;

    setupCanvas(triangleCanvas);

    function drawTriangleCanvas() {
        tctx.clearRect(0, 0, triangleCanvas.width, triangleCanvas.height);

        // Draw triangle
        tctx.strokeStyle = '#00A676';
        tctx.fillStyle = 'rgba(0, 166, 118, 0.1)';
        tctx.lineWidth = 3;
        tctx.beginPath();
        tctx.moveTo(trianglePoints[0].x, trianglePoints[0].y);
        tctx.lineTo(trianglePoints[1].x, trianglePoints[1].y);
        tctx.lineTo(trianglePoints[2].x, trianglePoints[2].y);
        tctx.closePath();
        tctx.fill();
        tctx.stroke();

        // Draw vertices
        trianglePoints.forEach(point => {
            tctx.fillStyle = '#F2C94C';
            tctx.beginPath();
            tctx.arc(point.x, point.y, 8, 0, Math.PI * 2);
            tctx.fill();
        });

        updateTriangleCalculations();
    }

    function updateTriangleCalculations() {
        const [p1, p2, p3] = trianglePoints;

        // Calculate area using cross product
        const area = Math.abs(
            (p1.x * (p2.y - p3.y) + p2.x * (p3.y - p1.y) + p3.x * (p1.y - p2.y)) / 2
        );

        // Calculate perimeter
        const side1 = Math.sqrt((p2.x - p1.x) ** 2 + (p2.y - p1.y) ** 2);
        const side2 = Math.sqrt((p3.x - p2.x) ** 2 + (p3.y - p2.y) ** 2);
        const side3 = Math.sqrt((p1.x - p3.x) ** 2 + (p1.y - p3.y) ** 2);
        const perimeter = side1 + side2 + side3;

        // Calculate angles using law of cosines
        const angle1 = Math.acos((side1**2 + side3**2 - side2**2) / (2 * side1 * side3)) * 180 / Math.PI;
        const angle2 = Math.acos((side1**2 + side2**2 - side3**2) / (2 * side1 * side2)) * 180 / Math.PI;
        const angle3 = 180 - angle1 - angle2;

        document.getElementById('triangleArea').textContent = area.toFixed(2);
        document.getElementById('trianglePerimeter').textContent = perimeter.toFixed(2);
        document.getElementById('triangleAngles').textContent =
            `${angle1.toFixed(1)}°, ${angle2.toFixed(1)}°, ${angle3.toFixed(1)}°`;
    }

    triangleCanvas.addEventListener('mousedown', (e) => {
        const rect = triangleCanvas.getBoundingClientRect();
        const mouseX = e.clientX - rect.left;
        const mouseY = e.clientY - rect.top;

        trianglePoints.forEach((point, index) => {
            const dist = Math.sqrt((mouseX - point.x) ** 2 + (mouseY - point.y) ** 2);
            if (dist < 20) draggingTriangle = index;
        });
    });

    triangleCanvas.addEventListener('mousemove', (e) => {
        if (draggingTriangle === null) return;

        const rect = triangleCanvas.getBoundingClientRect();
        trianglePoints[draggingTriangle].x = e.clientX - rect.left;
        trianglePoints[draggingTriangle].y = e.clientY - rect.top;
        drawTriangleCanvas();
    });

    triangleCanvas.addEventListener('mouseup', () => {
        draggingTriangle = null;
    });

    // Touch support
    triangleCanvas.addEventListener('touchstart', (e) => {
        e.preventDefault();
        const rect = triangleCanvas.getBoundingClientRect();
        const touch = e.touches[0];
        const mouseX = touch.clientX - rect.left;
        const mouseY = touch.clientY - rect.top;

        trianglePoints.forEach((point, index) => {
            const dist = Math.sqrt((mouseX - point.x) ** 2 + (mouseY - point.y) ** 2);
            if (dist < 30) draggingTriangle = index;
        });
    });

    triangleCanvas.addEventListener('touchmove', (e) => {
        e.preventDefault();
        if (draggingTriangle === null) return;

        const rect = triangleCanvas.getBoundingClientRect();
        const touch = e.touches[0];
        trianglePoints[draggingTriangle].x = touch.clientX - rect.left;
        trianglePoints[draggingTriangle].y = touch.clientY - rect.top;
        drawTriangleCanvas();
    });

    triangleCanvas.addEventListener('touchend', () => {
        draggingTriangle = null;
    });

    // Initial draw
    drawTriangleCanvas();
}
