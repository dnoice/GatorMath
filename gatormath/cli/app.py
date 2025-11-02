"""
Module Name: app

Description:
    Main Typer CLI application for GatorMath. Provides commands for
    mathematical calculations, geometry operations, web server management,
    and interactive demos.

Module Path: gatormath/cli/app.py
Package: gatormath.cli

Author: GatorMath Development Team
Created: 2025-11-02
Modified: 2025-11-02
Version: 0.1.0

Dependencies:
    - typer: CLI framework
    - rich: Beautiful terminal output
    - gatormath: Core functionality

Exports:
    - app: Typer application instance
    - main: Main entry point

Commands:
    - serve: Launch Flask web application
    - info: Display package information
    - version: Display version

Examples:
    $ gatormath serve
    $ gatormath serve --port 8000
    $ gatormath info
    $ gatormath version

Notes:
    Entry point defined in pyproject.toml:
    [project.scripts]
    gatormath = "gatormath.cli.app:main"

Version: 0.1.0
"""

import sys

import typer
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

import gatormath

app = typer.Typer(
    name="gatormath",
    help="GatorMath - Mathematical precision with bite 🐊",
    add_completion=False,
)

console = Console()


@app.command()
def serve(
    host: str = typer.Option("0.0.0.0", "--host", "-h", help="Host to bind to"),
    port: int = typer.Option(5000, "--port", "-p", help="Port to bind to"),
    debug: bool = typer.Option(False, "--debug", "-d", help="Enable debug mode"),
) -> None:
    """
    Launch Flask web application.

    Starts the GatorMath web server with interactive mathematical
    visualizations and calculators.

    Args:
        host: Host address to bind to (default: 0.0.0.0)
        port: Port number to bind to (default: 5000)
        debug: Enable Flask debug mode (default: False)

    Examples:
        $ gatormath serve
        $ gatormath serve --port 8000
        $ gatormath serve --debug

    Version: 0.1.0
    """
    console.print()
    console.print(Panel.fit(
        "[bold green]🐊 GatorMath Web Server[/bold green]\n"
        f"[cyan]Starting server on {host}:{port}...[/cyan]",
        border_style="green"
    ))
    console.print()

    try:
        from gatormath.web.app import create_app

        app_instance = create_app(config={"DEBUG": debug})

        console.print(f"[green]✓[/green] Server running at: [bold cyan]http://localhost:{port}[/bold cyan]")
        console.print(f"[green]✓[/green] Press [bold red]Ctrl+C[/bold red] to stop")
        console.print()

        app_instance.run(host=host, port=port, debug=debug)

    except KeyboardInterrupt:
        console.print("\n[yellow]Server stopped[/yellow]")
        sys.exit(0)
    except Exception as e:
        console.print(f"\n[red]Error starting server: {e}[/red]")
        sys.exit(1)


@app.command()
def info() -> None:
    """
    Display package information.

    Shows GatorMath version, description, and available modules.

    Examples:
        $ gatormath info

    Version: 0.1.0
    """
    table = Table(title="GatorMath Package Information", border_style="green")

    table.add_column("Property", style="cyan", no_wrap=True)
    table.add_column("Value", style="white")

    table.add_row("Package", "gatormath")
    table.add_row("Version", gatormath.__version__)
    table.add_row("Description", gatormath.__description__)
    table.add_row("Author", gatormath.__author__)
    table.add_row("License", gatormath.__license__)
    table.add_row("URL", gatormath.__url__)

    console.print()
    console.print(table)
    console.print()

    console.print("[bold green]Available Modules:[/bold green]")
    console.print("  • [cyan]core[/cyan]      - Mathematical operations")
    console.print("  • [cyan]geometry[/cyan]  - Geometric shapes and algorithms")
    console.print("  • [cyan]precision[/cyan] - Floating-point precision handling")
    console.print("  • [cyan]web[/cyan]       - Flask web application")
    console.print("  • [cyan]cli[/cyan]       - Command-line interface")
    console.print()


@app.command()
def version() -> None:
    """
    Display version information.

    Examples:
        $ gatormath version

    Version: 0.1.0
    """
    console.print(f"\n[bold green]GatorMath[/bold green] version [cyan]{gatormath.__version__}[/cyan]\n")


def main() -> None:
    """
    Main CLI entry point.

    Called when running `gatormath` command.

    Examples:
        $ gatormath --help

    Version: 0.1.0
    """
    app()


if __name__ == "__main__":
    main()
