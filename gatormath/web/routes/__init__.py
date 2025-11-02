"""
Metadata:
    Project: GatorMath
    File Name: __init__.py
    File Path: gatormath/web/routes/__init__.py
    Module: Routes Package
    Created: 2025-11-02
    Modified: 2025-11-02
    Version: 0.1.0
    Author: Dennis 'dnoice' Smaltz
    AI Acknowledgement: Claude Code

Description:
    Flask route handlers for web pages and REST API endpoints.

Usage:
    Routes are registered in app.py via:
    >>> from gatormath.web.routes import api, pages
    >>> app.register_blueprint(pages.bp)
    >>> app.register_blueprint(api.bp, url_prefix="/api")

Contents:
    Submodules:
        - pages: Page routes serving HTML templates
        - api: REST API endpoints for math operations

    Exports:
        - api: API routes module
        - pages: Page routes module

Dependencies:
    - flask: Blueprint support

Notes:
    Routes are organized as Flask blueprints for modularity
"""

__all__ = ["api", "pages"]
