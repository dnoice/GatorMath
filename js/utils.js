// ===== UTILITY FUNCTIONS =====
// Shared utility functions used across different modules

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

// Hamburger menu toggle
window.toggleMenu = function() {
    const navLinks = document.getElementById('navLinks');
    const hamburger = document.getElementById('hamburger');
    navLinks.classList.toggle('active');
    hamburger.classList.toggle('active');
};

// Welcome tooltip
window.closeWelcome = function() {
    const tooltip = document.getElementById('welcomeTooltip');
    tooltip.style.animation = 'slideIn 0.3s ease-out reverse';
    setTimeout(() => {
        tooltip.style.display = 'none';
    }, 300);
    localStorage.setItem('gatormath_visited', 'true');
};
