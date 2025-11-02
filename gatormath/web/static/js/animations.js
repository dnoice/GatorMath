/**
 * Metadata:
 *     Project: GatorMath
 *     File Name: animations.js
 *     File Path: gatormath/web/static/js/animations.js
 *     Module: GSAP Animations
 *     Created: 2025-11-02
 *     Modified: 2025-11-02
 *     Version: 1.0.0
 *     Author: Dennis 'dnoice' Smaltz
 *     AI Acknowledgement: Claude Code
 *
 * Description:
 *     Scroll-triggered animations and transitions using GSAP (GreenSock Animation Platform)
 *     with ScrollTrigger plugin. Provides smooth fade-in effects, parallax scrolling,
 *     and entrance animations for sections and components.
 *
 * Animations:
 *     - Fade-in elements on scroll (opacity 0→1, y: 50→0)
 *     - Hero section entrance (title, tagline stagger)
 *     - Terminal demo slide-in
 *     - Feature cards stagger animation
 *     - Section headers fade-in with scroll trigger
 *
 * Dependencies:
 *     - GSAP library (gsap.min.js)
 *     - ScrollTrigger plugin (ScrollTrigger.min.js)
 *
 * Configuration:
 *     - Duration: 0.8-1s
 *     - Easing: power2.out, power3.out
 *     - Trigger point: top 80%
 *     - Toggle actions: play none none reverse
 */

// ===== GSAP ANIMATIONS =====
// Scroll-triggered animations and transitions

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
