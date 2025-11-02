// Three.js Grid Background
        window.addEventListener('load', function() {
            initThreeJS();
        });
        
        function initThreeJS() {
            const canvas = document.getElementById('canvas-bg');
            if (!canvas) return;
            
            const scene = new THREE.Scene();
            const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
            const renderer = new THREE.WebGLRenderer({ 
                canvas: canvas,
                alpha: true,
                antialias: true
            });
            
            renderer.setSize(window.innerWidth, window.innerHeight);
            camera.position.z = 50;
            
            // Create grid
            const gridSize = 100;
            const gridDivisions = 20;
            const gridHelper = new THREE.GridHelper(gridSize, gridDivisions, 0x00A676, 0x00A676);
            gridHelper.rotation.x = Math.PI / 2;
            scene.add(gridHelper);
            
            // Add particles
            const particlesGeometry = new THREE.BufferGeometry();
            const particlesCount = 200;
            const positions = new Float32Array(particlesCount * 3);
            const initialPositions = new Float32Array(particlesCount * 3);
            
            for(let i = 0; i < particlesCount * 3; i++) {
                positions[i] = (Math.random() - 0.5) * 100;
                initialPositions[i] = positions[i];
            }
            
            particlesGeometry.setAttribute('position', new THREE.BufferAttribute(positions, 3));
            
            const particlesMaterial = new THREE.PointsMaterial({
                color: 0x00A676,
                size: 0.5,
                transparent: true,
                opacity: 0.6
            });
            
            const particles = new THREE.Points(particlesGeometry, particlesMaterial);
            scene.add(particles);
            
            // Add ambient light
            const ambientLight = new THREE.AmbientLight(0xffffff, 0.5);
            scene.add(ambientLight);
            
            // Mouse tracking
            let mouseX = 0;
            let mouseY = 0;
            let targetRotationX = 0;
            let targetRotationY = 0;
            
            document.addEventListener('mousemove', (event) => {
                mouseX = (event.clientX / window.innerWidth) * 2 - 1;
                mouseY = -(event.clientY / window.innerHeight) * 2 + 1;
                targetRotationX = mouseY * 0.3;
                targetRotationY = mouseX * 0.3;
            });
            
            // Animation
            function animate() {
                requestAnimationFrame(animate);
                
                // Smooth rotation based on mouse
                gridHelper.rotation.z += 0.001;
                gridHelper.rotation.x += (targetRotationX - gridHelper.rotation.x) * 0.05;
                
                particles.rotation.y += 0.0005;
                particles.rotation.x += 0.0003;
                
                // Animate particles based on mouse
                const positions = particles.geometry.attributes.position.array;
                for(let i = 0; i < particlesCount; i++) {
                    const i3 = i * 3;
                    
                    // Create wave effect based on mouse position
                    const distance = Math.sqrt(
                        Math.pow(positions[i3] - mouseX * 50, 2) + 
                        Math.pow(positions[i3 + 1] - mouseY * 50, 2)
                    );
                    
                    const influence = Math.max(0, 1 - distance / 30);
                    positions[i3 + 2] = initialPositions[i3 + 2] + Math.sin(Date.now() * 0.001 + i) * influence * 10;
                }
                particles.geometry.attributes.position.needsUpdate = true;
                
                renderer.render(scene, camera);
            }
            
            animate();
            
            // Handle resize
            window.addEventListener('resize', () => {
                camera.aspect = window.innerWidth / window.innerHeight;
                camera.updateProjectionMatrix();
                renderer.setSize(window.innerWidth, window.innerHeight);
                
                // Re-initialize all playgrounds on resize
                setTimeout(() => {
                    initializePlaygrounds();
                }, 100);
            });
        }
        
        // GSAP Animations
        gsap.registerPlugin(ScrollTrigger);
        
        // Fade in elements on scroll
        gsap.utils.toArray('.fade-in').forEach(element => {
            gsap.from(element, {
                scrollTrigger: {
                    trigger: element,
                    start: 'top 80%',
                    end: 'top 50%',
                    toggleActions: 'play none none reverse'
                },
                opacity: 0,
                y: 50,
                duration: 0.8,
                ease: 'power2.out'
            });
        });
        
        // Hero animation
        gsap.from('.hero h1', {
            opacity: 0,
            y: 30,
            duration: 1,
            delay: 0.3,
            ease: 'power3.out'
        });
        
        gsap.from('.hero .tagline', {
            opacity: 0,
            y: 20,
            duration: 1,
            delay: 0.6,
            ease: 'power3.out'
        });
        
        gsap.from('.terminal-demo', {
            opacity: 0,
            scale: 0.95,
            duration: 1,
            delay: 0.9,
            ease: 'power3.out'
        });
        
        gsap.from('.cta-buttons', {
            opacity: 0,
            y: 20,
            duration: 1,
            delay: 1.2,
            ease: 'power3.out'
        });
        
        // Smooth scroll for nav links
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {
            anchor.addEventListener('click', function (e) {
                e.preventDefault();
                const target = document.querySelector(this.getAttribute('href'));
                if (target) {
                    target.scrollIntoView({
                        behavior: 'smooth',
                        block: 'start'
                    });
                    
                    // Close mobile menu if open
                    const navLinks = document.getElementById('navLinks');
                    const hamburger = document.getElementById('hamburger');
                    if (navLinks && navLinks.classList.contains('active')) {
                        navLinks.classList.remove('active');
                        hamburger.classList.remove('active');
                    }
                }
            });
        });
        
        // Hamburger menu toggle
        window.toggleMenu = function() {
            const navLinks = document.getElementById('navLinks');
            const hamburger = document.getElementById('hamburger');
            navLinks.classList.toggle('active');
            hamburger.classList.toggle('active');
        };
        
        // Terminal typing effect
        const terminalLines = document.querySelectorAll('.terminal-line');
        terminalLines.forEach((line, index) => {
            gsap.from(line, {
                opacity: 0,
                x: -20,
                duration: 0.5,
                delay: 1.2 + (index * 0.1),
                ease: 'power2.out'
            });
        });
        
        // ===== INTERACTIVE PLAYGROUND FUNCTIONS =====
        
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
        
        // Vector Canvas
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
        
        // Bezier Canvas
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
        
        // Matrix Canvas
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
        
        // Triangle Canvas
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
        
        // Calculator Functions
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
        
        // Code Playground
        window.runCode = function() {
            const code = document.getElementById('codeEditor').value;
            const output = document.getElementById('codeOutput');
            output.innerHTML = '';
            
            const originalLog = console.log;
            const originalError = console.error;
            
            console.log = (...args) => {
                const div = document.createElement('div');
                div.className = 'log';
                div.textContent = args.map(arg => 
                    typeof arg === 'object' ? JSON.stringify(arg, null, 2) : String(arg)
                ).join(' ');
                output.appendChild(div);
            };
            
            console.error = (...args) => {
                const div = document.createElement('div');
                div.className = 'error';
                div.textContent = args.join(' ');
                output.appendChild(div);
            };
            
            try {
                eval(code);
            } catch (error) {
                const div = document.createElement('div');
                div.className = 'error';
                div.textContent = 'Error: ' + error.message;
                output.appendChild(div);
            }
            
            console.log = originalLog;
            console.error = originalError;
        };
        
        // Add keyboard shortcut for code editor
        const codeEditor = document.getElementById('codeEditor');
        if (codeEditor) {
            codeEditor.addEventListener('keydown', (e) => {
                // Ctrl+Enter or Cmd+Enter to run code
                if ((e.ctrlKey || e.metaKey) && e.key === 'Enter') {
                    e.preventDefault();
                    runCode();
                }
                
                // Tab key for indentation
                if (e.key === 'Tab') {
                    e.preventDefault();
                    const start = codeEditor.selectionStart;
                    const end = codeEditor.selectionEnd;
                    codeEditor.value = codeEditor.value.substring(0, start) + '  ' + codeEditor.value.substring(end);
                    codeEditor.selectionStart = codeEditor.selectionEnd = start + 2;
                }
            });
        }
        
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
        
        // Parallax effect on sections
        gsap.utils.toArray('section').forEach((section, index) => {
            if (index > 0) { // Skip hero
                gsap.to(section, {
                    scrollTrigger: {
                        trigger: section,
                        start: 'top bottom',
                        end: 'bottom top',
                        scrub: 1
                    },
                    y: -30,
                    ease: 'none'
                });
            }
        });
        
        // Add nav highlight on scroll
        const sections = document.querySelectorAll('section[id]');
        const navLinks = document.querySelectorAll('.nav-links a[href^="#"]');
        
        window.addEventListener('scroll', () => {
            let current = '';
            sections.forEach(section => {
                const sectionTop = section.offsetTop;
                const sectionHeight = section.clientHeight;
                if (window.pageYOffset >= sectionTop - 200) {
                    current = section.getAttribute('id');
                }
            });
            
            navLinks.forEach(link => {
                link.style.color = '';
                if (link.getAttribute('href') === '#' + current) {
                    link.style.color = '#00A676';
                }
            });
        });
        
        // Welcome tooltip
        window.closeWelcome = function() {
            const tooltip = document.getElementById('welcomeTooltip');
            tooltip.style.animation = 'slideIn 0.3s ease-out reverse';
            setTimeout(() => {
                tooltip.style.display = 'none';
            }, 300);
            localStorage.setItem('gatormath_visited', 'true');
        };
        
        // Show welcome tooltip if first visit
        setTimeout(() => {
            if (!localStorage.getItem('gatormath_visited')) {
                document.getElementById('welcomeTooltip').style.display = 'block';
                
                // Auto-hide after 8 seconds
                setTimeout(() => {
                    if (document.getElementById('welcomeTooltip').style.display !== 'none') {
                        closeWelcome();
                    }
                }, 8000);
            }
        }, 2000);
