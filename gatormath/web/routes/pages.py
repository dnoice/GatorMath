"""
File Name: pages.py
File Path: gatormath/web/routes/pages.py
Module Name: pages

Description:
    Flask blueprint for serving web pages and templates.
    Handles main application routes for the interactive frontend.

Module Path: gatormath/web/routes/pages.py
Package: gatormath.web.routes

Author: Dennis 'dnoice' Smaltz
AI Acknowledgement: Claude Code
Created: 2025-11-02
Modified: 2025-11-02
Version: 0.1.0

Dependencies:
    - flask: Flask framework
    - gatormath: Version info

Exports:
    - bp: Flask Blueprint for page routes

Routes:
    - GET /: Main application page
    - GET /health: Health check endpoint

Examples:
    Routes are registered in app.py via:
    >>> app.register_blueprint(pages.bp)

Notes:
    Templates served from gatormath/web/templates/
    Static assets served from gatormath/web/static/

Version: 0.1.0
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
