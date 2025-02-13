"""
Project Initialization Command

Handles creation of new Truffle projects.
Verified against deprecated SDK version 0.5.3.

Verification Status:
✓ Command Structure
  - Arguments and options match deprecated version
  - Help text and documentation
  - Error handling patterns
  - Return types

✓ Project Creation
  - Directory structure
  - File generation
  - Template rendering
  - Manifest creation

✓ Logging Output
  - Progress indicators
  - File operations
  - Success/error states
  - User prompts
"""

import typer
from pathlib import Path
import json
import shutil
import uuid
from typing import Optional, List

from ..utils.logger import log, Symbols
from ..templates.app import (
    generate_main_py,
    generate_manifest,
    write_app_files
)

def init(
    project_name: str = typer.Argument(..., help="Name of the project to create"),
    description: Optional[str] = typer.Option(
        None,
        "--description", "-d",
        help="Description of the project"
    ),
    num_examples: int = typer.Option(
        5,
        "--examples", "-e",
        help="Number of example prompts to collect"
    )
) -> None:
    """Initialize a new Truffle project."""
    with log.group("Initializing new Truffle project", emoji=Symbols.PACKAGE):
        log.info("Creating new Truffle project", version="0.6.5")
        
        # Validate and format project name
        if project_name == ".":
            project_name = Path(project_name).absolute().name
            if not typer.confirm(f"Project Name: {project_name}", default=True):
                project_name = typer.prompt("Enter Project Name")
        
        # Capitalize first letter
        project_name = str(project_name)[0].upper() + str(project_name)[1:]
        proj_path = Path(project_name)
        
        # Check if project exists
        if proj_path.exists():
            log.error("Project already exists", {
                "name": project_name,
                "path": str(proj_path)
            })
            raise typer.Exit(1)

        # Get project details
        log.prompt("Project Name", project_name)
        if not description:
            description = typer.prompt("Description")
        
        # Collect example prompts
        with log.group("Input sample prompts", emoji=Symbols.PENCIL):
            example_prompts = []
            for i in range(num_examples):
                prompt = typer.prompt(f"Enter example prompt {i + 1}/{num_examples}")
                example_prompts.append(prompt)
                log.detail(f"{i + 1}. \"{prompt}\"")

        # Generate manifest
        manifest_data = {
            "name": project_name.lower(),
            "description": description,
            "example_prompts": example_prompts,
            "packages": [],
            "manifest_version": 1,
            "app_bundle_id": str(uuid.uuid4())
        }
        
        # Create project structure
        with log.group("Creating project structure", emoji=Symbols.SPARKLES):
            proj_path.mkdir()
            
            # Log file creation before actually creating them
            for file in ["main.py", "manifest.json", "requirements.txt", "icon.png"]:
                log.created_file(file)
            
            # Create files
            write_app_files(proj_path, project_name, manifest_data, "0.6.5")
            
            # Copy icon
            icon_src = Path(__file__).parent.parent / "assets" / "default_app.png"
            shutil.copy(icon_src, proj_path / "icon.png")
            
            # Success message
            log.success("Project initialized successfully!")
            log.detail(f"{Symbols.FOLDER} Location: ./{project_name}")
            log.detail(f"{Symbols.WRENCH} Run 'truffle build' to package your app")
