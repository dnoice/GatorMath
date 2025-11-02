"""
Metadata:
    Project: GatorMath
    File Name: pages.py
    File Path: gatormath/web/routes/pages.py
    Module: Page Routes
    Created: 2025-11-02
    Modified: 2025-11-02
    Version: 0.1.0
    Author: Dennis 'dnoice' Smaltz
    AI Acknowledgement: Claude Code

Description:
    Flask blueprint for serving web pages and templates.
    Handles main application routes for the interactive frontend.

Usage:
    Routes are registered in app.py via:
    >>> app.register_blueprint(pages.bp)

    GET / -> renders index.html
    GET /health -> {"status": "healthy", "version": "0.1.0"}

Contents:
    Routes:
        - GET /: Main application page
        - GET /health: Health check endpoint

    Exports:
        - bp: Flask Blueprint for page routes

Dependencies:
    - flask: Flask framework
    - gatormath: Version info

Notes:
    Templates served from gatormath/web/templates/
    Static assets served from gatormath/web/static/
"""

from flask import Blueprint, render_template

import gatormath

bp = Blueprint("pages", __name__)


@bp.route("/")
def index():
    """
    Serve main application page.

    Returns:
        str: Rendered HTML template

    Template Variables:
        - version: GatorMath version string

    Examples:
        GET / -> renders index.html

    Version: 0.1.0
    """
    return render_template("index.html", version=gatormath.__version__)


@bp.route("/health")
def health():
    """
    Health check endpoint.

    Returns:
        dict: Health status and version info

    Examples:
        GET /health -> {"status": "healthy", "version": "0.1.0"}

    Version: 0.1.0
    """
    return {
        "status": "healthy",
        "version": gatormath.__version__,
        "service": "GatorMath Web"
    }
