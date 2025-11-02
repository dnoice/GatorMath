"""
Module Name: gatormath.web

Description:
    Flask web application module providing interactive mathematical
    visualizations, REST API endpoints, and web-based calculators.
    Integrates the GatorMath Python backend with a rich JavaScript frontend.

Module Path: gatormath/web/__init__.py
Package: gatormath.web

Author: Dennis 'dnoice' Smaltz
AI Acknowledgement: Claude Code
Created: 2025-11-02
Modified: 2025-11-02
Version: 0.1.0

Submodules:
    - app: Flask application factory and configuration
    - routes.api: REST API endpoints for math operations
    - routes.pages: Page routes for serving templates

Structure:
    - static/: Frontend assets (CSS, JavaScript, images)
    - templates/: Jinja2 HTML templates
    - routes/: API and page route handlers

Features:
    - Interactive math visualizations (vectors, bezier, matrices, triangles)
    - REST API exposing Python math functions
    - Live calculators powered by backend Python
    - 3D animated background with Three.js
    - Responsive design with modular CSS

Usage:
    >>> from gatormath.web.app import create_app
    >>> app = create_app()
    >>> app.run(debug=True)

    Or via CLI:
    $ gatormath serve

Notes:
    Requires Flask and flask-cors packages
    Development mode uses Flask debug server
    Production deployment requires WSGI server (gunicorn, uwsgi)
"""

from gatormath.web.app import create_app

__all__ = ["create_app"]
