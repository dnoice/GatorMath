"""
Module Name: app

Description:
    Flask application factory and configuration. Creates and configures
    the Flask application instance with routes, CORS, and error handlers.

Module Path: gatormath/web/app.py
Package: gatormath.web

Author: Dennis 'dnoice' Smaltz
AI Acknowledgement: Claude Code
Created: 2025-11-02
Modified: 2025-11-02
Version: 0.1.0

Dependencies:
    - flask: Flask web framework
    - flask_cors: CORS support for API endpoints
    - os: Path operations

Exports:
    - create_app: Flask application factory function

Examples:
    >>> from gatormath.web.app import create_app
    >>> app = create_app()
    >>> app.run(host='0.0.0.0', port=5000, debug=True)

Notes:
    Uses application factory pattern for flexibility
    CORS enabled for API routes to support external clients
    Static files served from gatormath/web/static/
    Templates loaded from gatormath/web/templates/

Configuration:
    - DEBUG: Set via environment or parameter
    - SECRET_KEY: Generated or provided
    - CORS: Enabled for /api/* routes
"""

import os
from typing import Optional

from flask import Flask
from flask_cors import CORS


def create_app(config: Optional[dict] = None) -> Flask:
    """
    Create and configure Flask application instance.

    Application Factory Pattern:
        Creates Flask app with proper configuration, registers blueprints,
        sets up CORS, and configures static/template paths.

    Args:
        config (dict, optional): Configuration dictionary
            - DEBUG: Enable debug mode (default: False)
            - SECRET_KEY: Flask secret key (default: generated)

    Returns:
        Flask: Configured Flask application instance

    Configuration:
        - Static folder: gatormath/web/static/
        - Template folder: gatormath/web/templates/
        - CORS: Enabled for /api/* routes
        - JSON: Compact formatting

    Examples:
        >>> app = create_app()
        >>> app.run(debug=True)

        >>> app = create_app(config={'DEBUG': True})
        >>> app.run()

    Notes:
        Call this function to create the app, then run with app.run()
        or deploy with WSGI server

    Version: 0.1.0
    """
    # Determine paths
    instance_path = os.path.dirname(os.path.abspath(__file__))
    static_folder = os.path.join(instance_path, "static")
    template_folder = os.path.join(instance_path, "templates")

    # Create Flask app
    app = Flask(
        __name__,
        static_folder=static_folder,
        template_folder=template_folder,
        static_url_path="/static"
    )

    # Default configuration
    app.config.update(
        DEBUG=os.environ.get("FLASK_DEBUG", "False").lower() == "true",
        SECRET_KEY=os.environ.get("SECRET_KEY", os.urandom(24).hex()),
        JSON_SORT_KEYS=False,
    )

    # Override with provided config
    if config:
        app.config.update(config)

    # Enable CORS for API routes
    CORS(app, resources={r"/api/*": {"origins": "*"}})

    # Register blueprints
    from gatormath.web.routes import api, pages

    app.register_blueprint(pages.bp)
    app.register_blueprint(api.bp, url_prefix="/api")

    # Error handlers
    @app.errorhandler(404)
    def not_found(error):
        return {"error": "Not found"}, 404

    @app.errorhandler(500)
    def internal_error(error):
        return {"error": "Internal server error"}, 500

    return app


def main() -> None:
    """
    Main entry point for running Flask app directly.

    Examples:
        >>> python -m gatormath.web.app

    Notes:
        For development only. Use gatormath CLI or WSGI server for production.

    Version: 0.1.0
    """
    app = create_app(config={"DEBUG": True})
    print("🐊 GatorMath Web Server")
    print("=" * 50)
    print("Server running at: http://localhost:5000")
    print("Press Ctrl+C to stop")
    print("=" * 50)
    app.run(host="0.0.0.0", port=5000, debug=True)


if __name__ == "__main__":
    main()
