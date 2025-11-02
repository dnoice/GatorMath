# GatorMath CLI Documentation

**Version:** 0.1.0
**Last Updated:** 2025-11-02
**Document Path:** `/docs/CLI_DOCS.md`

---

## Table of Contents

1. [Overview](#overview)
2. [Installation](#installation)
3. [Commands](#commands)
   - [serve](#serve)
   - [info](#info)
   - [version](#version)
4. [Configuration](#configuration)
5. [Examples](#examples)
6. [Troubleshooting](#troubleshooting)

---

## Overview

The GatorMath CLI provides a command-line interface for:

- **Web Server Management**: Launch the interactive Flask web application
- **Package Information**: Display version and module details
- **Quick Access**: Fast terminal-based access to GatorMath functionality

Built with **Typer** for CLI framework and **Rich** for beautiful terminal output.

**Entry Point:** `gatormath` command (installed via pip)

---

## Installation

### Prerequisites

- Python 3.9 or higher
- pip package manager

### Install GatorMath

```bash
# Install from source
pip install -e .

# Or install from PyPI (when published)
pip install gatormath
```

### Verify Installation

```bash
gatormath --help
gatormath version
```

**Expected Output:**
```
GatorMath version 0.1.0
```

---

## Commands

### serve

Launch the Flask web application with interactive mathematical visualizations.

**Syntax:**
```bash
gatormath serve [OPTIONS]
```

**Options:**

| Option | Short | Type | Default | Description |
|--------|-------|------|---------|-------------|
| `--host` | `-h` | str | `0.0.0.0` | Host address to bind to |
| `--port` | `-p` | int | `5000` | Port number to bind to |
| `--debug` | `-d` | bool | `False` | Enable Flask debug mode |

**Examples:**

```bash
# Start server on default port 5000
gatormath serve

# Start on custom port
gatormath serve --port 8000

# Start with debug mode enabled
gatormath serve --debug

# Bind to localhost only
gatormath serve --host 127.0.0.1

# All options together
gatormath serve --host 0.0.0.0 --port 3000 --debug
```

**Output:**

```
╭─────────────────────────────────╮
│ 🐊 GatorMath Web Server         │
│ Starting server on 0.0.0.0:5000 │
╰─────────────────────────────────╯

✓ Server running at: http://localhost:5000
✓ Press Ctrl+C to stop
```

**Access the Application:**

Open your browser to `http://localhost:5000` (or your custom port)

**Stop the Server:**

Press `Ctrl+C` in the terminal

---

### info

Display comprehensive package information including version, modules, and metadata.

**Syntax:**
```bash
gatormath info
```

**Options:** None

**Examples:**

```bash
gatormath info
```

**Output:**

```
      GatorMath Package Information
┏━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Property    ┃ Value                             ┃
┡━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ Package     │ gatormath                         │
│ Version     │ 0.1.0                             │
│ Description │ Mathematical precision with bite  │
│ Author      │ GatorMath Development Team        │
│ License     │ MIT                               │
│ URL         │ https://github.com/dnoice/...     │
└─────────────┴───────────────────────────────────┘

Available Modules:
  • core      - Mathematical operations
  • geometry  - Geometric shapes and algorithms
  • precision - Floating-point precision handling
  • web       - Flask web application
  • cli       - Command-line interface
```

**Use Cases:**
- Check installed version
- Verify package metadata
- List available modules
- Troubleshooting installation issues

---

### version

Display version information in a concise format.

**Syntax:**
```bash
gatormath version
```

**Options:** None

**Examples:**

```bash
gatormath version
```

**Output:**

```
GatorMath version 0.1.0
```

**Use Cases:**
- Quick version check
- Script integration
- CI/CD pipelines

---

## Configuration

### Environment Variables

The CLI respects the following environment variables:

**FLASK_DEBUG**
```bash
export FLASK_DEBUG=true
gatormath serve
```
- **Type**: boolean (`true` or `false`)
- **Default**: `false`
- **Description**: Enables Flask debug mode and auto-reload

**FLASK_HOST**
```bash
export FLASK_HOST=127.0.0.1
gatormath serve
```
- **Type**: string (IP address)
- **Default**: `0.0.0.0`
- **Description**: Default host binding

**FLASK_PORT**
```bash
export FLASK_PORT=8080
gatormath serve
```
- **Type**: integer
- **Default**: `5000`
- **Description**: Default port number

### Configuration File

GatorMath does not currently use a configuration file. All settings are passed via command-line options or environment variables.

---

## Examples

### Development Workflow

```bash
# Install in development mode
pip install -e .

# Start server with debug mode
gatormath serve --debug

# In another terminal, check info
gatormath info
```

### Production Deployment

```bash
# Install production dependencies
pip install gatormath

# Start server on port 80 (requires sudo)
sudo gatormath serve --port 80 --host 0.0.0.0

# Or use a reverse proxy (recommended)
gatormath serve --host 127.0.0.1 --port 5000
```

### Docker Container

```dockerfile
FROM python:3.11-slim

WORKDIR /app
COPY . .

RUN pip install -e .

EXPOSE 5000

CMD ["gatormath", "serve", "--host", "0.0.0.0"]
```

```bash
docker build -t gatormath .
docker run -p 5000:5000 gatormath
```

### CI/CD Version Check

```yaml
# .github/workflows/version-check.yml
- name: Check GatorMath version
  run: |
    VERSION=$(gatormath version | grep -oP '\d+\.\d+\.\d+')
    echo "GatorMath version: $VERSION"
```

### Shell Script Integration

```bash
#!/bin/bash

# Start GatorMath server in background
gatormath serve --port 5000 &
SERVER_PID=$!

# Wait for server to start
sleep 2

# Run tests against server
curl http://localhost:5000/health

# Stop server
kill $SERVER_PID
```

---

## Troubleshooting

### Port Already in Use

**Error:**
```
OSError: [Errno 48] Address already in use
```

**Solution:**
```bash
# Find process using port 5000
lsof -i :5000

# Kill the process
kill -9 <PID>

# Or use a different port
gatormath serve --port 8000
```

### Permission Denied on Port 80

**Error:**
```
PermissionError: [Errno 13] Permission denied
```

**Solution:**
```bash
# Use sudo (not recommended)
sudo gatormath serve --port 80

# Or use port > 1024
gatormath serve --port 8080

# Or configure reverse proxy (recommended)
```

### Command Not Found

**Error:**
```
bash: gatormath: command not found
```

**Solution:**
```bash
# Ensure package is installed
pip install -e .

# Or add to PATH
export PATH="$PATH:$HOME/.local/bin"

# Verify installation
which gatormath
pip show gatormath
```

### Import Errors

**Error:**
```
ModuleNotFoundError: No module named 'gatormath'
```

**Solution:**
```bash
# Reinstall package
pip uninstall gatormath
pip install -e .

# Or check Python path
python -c "import sys; print('\n'.join(sys.path))"

# Verify installation
python -c "import gatormath; print(gatormath.__version__)"
```

### Flask Debug Mode Not Working

**Issue:** Changes to code not reflected without restart

**Solution:**
```bash
# Ensure debug mode is enabled
gatormath serve --debug

# Or use environment variable
export FLASK_DEBUG=true
gatormath serve

# Verify debug mode
# Look for "WARNING: This is a development server"
```

### Rich Output Not Displaying

**Issue:** No colors or formatting in terminal

**Solution:**
```bash
# Enable color support
export FORCE_COLOR=1

# Or use different terminal
# Rich requires terminal with ANSI support

# Test Rich support
python -c "from rich.console import Console; Console().print('[bold green]Test[/bold green]')"
```

---

**Version:** 0.1.0
**See Also:** [API Docs](API_DOCS.md) | [Development Guide](DEVELOPMENT.md) | [Standards](STANDARDS.md)
