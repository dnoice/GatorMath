// ===== THREE.JS BACKGROUND =====
// Animated 3D grid background with particles

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
