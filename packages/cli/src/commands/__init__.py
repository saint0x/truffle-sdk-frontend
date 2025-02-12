"""
CLI Commands Package Initialization

Core implementation of the Truffle CLI commands.
Provides command registration and routing for the CLI application.

Migration Status:
[INCOMPLETE] CLI Commands Setup
- [x] Core commands
- [ ] Asset handling
- [ ] Template system

Core Components (from truffle/truffle_cli.py):
1. Command Structure:
   - [x] init.py - Project initialization
   - [x] build.py - Build command
   - [x] run.py - Run command

2. Asset Integration:
   - [ ] cli_assets/ directory
   - [ ] Template files
   - [ ] Resource management

3. Command Features:
   - [x] Project validation
   - [x] Build process
   - [x] Runtime management
   - [ ] Template handling

Missing Components:
1. CLI Assets:
   - [ ] Icon templates
   - [ ] Project templates
   - [ ] Resource files

2. Template System:
   - [ ] Template rendering
   - [ ] Resource copying
   - [ ] Asset management

Source Files:
- Original: truffle/truffle_cli.py
- Split into:
  - init.py: Project creation
  - build.py: Build process
  - run.py: Runtime management

Dependencies:
- typer
- pathlib
- platform.models
- utils.templates
"""

import typer

from . import init, build, run

# Create the CLI app
app = typer.Typer(
    help="Truffle CLI - Create and manage Truffle applications",
    add_completion=False,
)

# Register commands
app.command()(init.init)
app.command()(build.build)
app.command()(run.run)

def get_app() -> typer.Typer:
    """Get the CLI application instance."""
    return app
