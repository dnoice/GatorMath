"""
Metadata:
    Project: GatorMath
    File Name: __init__.py
    File Path: gatormath/web/__init__.py
    Module: Web Application Package
    Created: 2025-11-02
    Modified: 2025-11-02
    Version: 0.1.0
    Author: Dennis 'dnoice' Smaltz
    AI Acknowledgement: Claude Code

Description:
    Flask web application module providing interactive mathematical
    visualizations, REST API endpoints, and web-based calculators.
    Integrates the GatorMath Python backend with a rich JavaScript frontend.

Usage:
    >>> from gatormath.web.app import create_app
    >>> app = create_app()
    >>> app.run(debug=True)

    Or via CLI:
    $ gatormath serve

Contents:
    Submodules:
        - app: Flask application factory and configuration
        - routes.api: REST API endpoints for math operations
        - routes.pages: Page routes for serving templates

    Structure:
        - static/: Frontend assets (CSS, JavaScript, images)
        - templates/: Jinja2 HTML templates
        - routes/: API and page route handlers

    Exports:
        - create_app: Flask application factory

Dependencies:
    - flask: Web framework
    - flask-cors: CORS support
    - gatormath.core: Math operations backend
    - gatormath.geometry: Geometry operations backend

Features:
    - Interactive math visualizations (vectors, bezier, matrices, triangles)
    - REST API exposing Python math functions
    - Live calculators powered by backend Python
    - 3D animated background with Three.js
    - Responsive design with modular CSS

Notes:
    Development mode uses Flask debug server
    Production deployment requires WSGI server (gunicorn, uwsgi)
"""

from gatormath.web.app import create_app

__all__ = ["create_app"]
