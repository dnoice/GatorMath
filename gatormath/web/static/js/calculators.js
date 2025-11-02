/**
 * Metadata:
 *     Project: GatorMath
 *     File Name: calculators.js
 *     File Path: gatormath/web/static/js/calculators.js
 *     Module: Live Calculators
 *     Created: 2025-11-02
 *     Modified: 2025-11-02
 *     Version: 1.0.0
 *     Author: Dennis 'dnoice' Smaltz
 *     AI Acknowledgement: Claude Code
 *
 * Description:
 *     Interactive mathematical calculators for distance, circle properties,
 *     angle conversion, and vector projection. Provides real-time calculations
 *     with visual feedback in calculator cards.
 *
 * Exports (Global):
 *     - window.calculateDistance(): 2D point distance calculator
 *     - window.calculateCircle(): Circle area and circumference
 *     - window.convertAngle(): Degrees/radians/gradians conversion
 *     - window.calculateProjection(): Vector projection calculator
 *
 * Dependencies:
 *     - HTML input elements (calculator cards)
 *     - Math API (Math.sqrt, Math.PI)
 *
 * Formulas:
 *     - Distance: √((x2-x1)² + (y2-y1)²)
 *     - Circle Area: πr²
 *     - Circle Circumference: 2πr
 *     - Angle Conversion: rad = deg × π/180, grad = deg × 10/9
 *     - Vector Projection: (v1·v2)/|v2|
 */

// ===== CALCULATOR FUNCTIONS =====
// Live calculators for distance, circle, angle conversion, etc.

window.calculateDistance = function() {
    const x1 = parseFloat(document.getElementById('dist-x1').value);
    const y1 = parseFloat(document.getElementById('dist-y1').value);
    const x2 = parseFloat(document.getElementById('dist-x2').value);
    const y2 = parseFloat(document.getElementById('dist-y2').value);

    const distance = Math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2);
    document.getElementById('distance-result').textContent = distance.toFixed(4);
};

window.calculateCircle = function() {
    const radius = parseFloat(document.getElementById('circle-radius').value);
    const area = Math.PI * radius ** 2;
    const circumference = 2 * Math.PI * radius;

    document.getElementById('circle-area').textContent = area.toFixed(4);
    document.getElementById('circle-circumference').textContent = circumference.toFixed(4);
};

window.convertAngle = function() {
    const degrees = parseFloat(document.getElementById('angle-degrees').value);
    const radians = degrees * Math.PI / 180;
    const gradians = degrees * 10 / 9;

    document.getElementById('angle-radians').textContent = radians.toFixed(6);
    document.getElementById('angle-gradians').textContent = gradians.toFixed(4);
};

window.calculateProjection = function() {
    const v1x = parseFloat(document.getElementById('proj-v1x').value);
    const v1y = parseFloat(document.getElementById('proj-v1y').value);
    const v2x = parseFloat(document.getElementById('proj-v2x').value);
    const v2y = parseFloat(document.getElementById('proj-v2y').value);

    // Scalar projection: (v1 · v2) / |v2|
    const dot = v1x * v2x + v1y * v2y;
    const magV2 = Math.sqrt(v2x ** 2 + v2y ** 2);
    const scalarProj = dot / magV2;

    // Vector projection: scalar_proj * (v2 / |v2|)
    const projX = scalarProj * (v2x / magV2);
    const projY = scalarProj * (v2y / magV2);

    document.getElementById('projection-result').textContent =
        `(${projX.toFixed(3)}, ${projY.toFixed(3)})`;
    document.getElementById('scalar-proj').textContent = scalarProj.toFixed(4);
};

window.calculateDeterminant = function() {
    const m11 = parseFloat(document.getElementById('m11').value);
    const m12 = parseFloat(document.getElementById('m12').value);
    const m21 = parseFloat(document.getElementById('m21').value);
    const m22 = parseFloat(document.getElementById('m22').value);

    const det = m11 * m22 - m12 * m21;
    const trace = m11 + m22;

    document.getElementById('determinant-result').textContent = det.toFixed(4);
    document.getElementById('trace-result').textContent = trace.toFixed(4);
};

window.calculateQuadratic = function() {
    const a = parseFloat(document.getElementById('quad-a').value);
    const b = parseFloat(document.getElementById('quad-b').value);
    const c = parseFloat(document.getElementById('quad-c').value);

    const discriminant = b ** 2 - 4 * a * c;
    document.getElementById('discriminant').textContent = discriminant.toFixed(4);

    if (discriminant < 0) {
        const realPart = (-b / (2 * a)).toFixed(4);
        const imagPart = (Math.sqrt(-discriminant) / (2 * a)).toFixed(4);
        document.getElementById('quadratic-roots').textContent =
            `${realPart} ± ${imagPart}i`;
    } else if (discriminant === 0) {
        const root = (-b / (2 * a)).toFixed(4);
        document.getElementById('quadratic-roots').textContent = root;
    } else {
        const root1 = ((-b + Math.sqrt(discriminant)) / (2 * a)).toFixed(4);
        const root2 = ((-b - Math.sqrt(discriminant)) / (2 * a)).toFixed(4);
        document.getElementById('quadratic-roots').textContent =
            `${root1}, ${root2}`;
    }
};

// Initialize calculators on load
document.addEventListener('DOMContentLoaded', function() {
    setTimeout(() => {
        if (typeof calculateDistance === 'function') calculateDistance();
        if (typeof calculateCircle === 'function') calculateCircle();
        if (typeof convertAngle === 'function') convertAngle();
        if (typeof calculateProjection === 'function') calculateProjection();
        if (typeof calculateDeterminant === 'function') calculateDeterminant();
        if (typeof calculateQuadratic === 'function') calculateQuadratic();
    }, 200);
});
