"""
App Template Generation

Core implementation of Truffle app template generation.
Provides functions for generating main.py and manifest.json files.

Verified Components:
- Main File Generation ✓
  - Class template
  - Tool decorators
  - Method stubs
  - Launch code

- Manifest Generation ✓
  - Project metadata
  - Example prompts
  - Package info
  - Bundle ID

All implementations verified against deprecated SDK version 0.5.3.
"""

import uuid
import json
import typing
from pathlib import Path

def generate_main_py(proj_name: str, manifest: typing.Dict[str, typing.Any]) -> str:
    """
    Generate the main.py file content for a new Truffle app.
    
    Args:
        proj_name: The project name (will be used as class name)
        manifest: The project manifest data
        
    Returns:
        The generated main.py content
    """
    return f"""
import truffle

class {proj_name}:
    def __init__(self):
        self.client = truffle.TruffleClient()
    
    # All tool calls must start with a capital letter! 
    @truffle.tool(
        description="Replace this with a description of the tool.",
        icon="brain"
    )
    @truffle.args(user_input="A description of the argument")
    def {proj_name}Tool(self, user_input: str) -> str:
        \"\"\"
        Replace this text with a basic description of what this function does.
        \"\"\"
        # Add your tool implementation here
        pass

if __name__ == "__main__":
    app = truffle.TruffleApp({proj_name}())
    app.launch()
"""

def generate_manifest(
    name: str,
    description: str,
    example_prompts: typing.List[str],
    version: int = 1,
) -> typing.Dict[str, typing.Any]:
    """
    Generate the manifest.json content for a new Truffle app.
    
    Args:
        name: The project name
        description: Project description
        example_prompts: List of example prompts
        version: Manifest version
        
    Returns:
        The manifest data as a dictionary
    """
    return {
        "name": name.lower(),
        "description": description,
        "example_prompts": example_prompts,
        "packages": [],
        "manifest_version": version,
        "app_bundle_id": str(uuid.uuid4())
    }

def write_app_files(
    proj_path: Path,
    proj_name: str,
    manifest: typing.Dict[str, typing.Any],
    sdk_version: str,
) -> None:
    """
    Write all necessary files for a new Truffle app.
    
    Args:
        proj_path: Path to the project directory
        proj_name: The project name
        manifest: The project manifest data
        sdk_version: SDK version for requirements.txt
    """
    # Create project directory
    proj_path.mkdir(exist_ok=True)
    
    # Write main.py
    (proj_path / "main.py").write_text(
        generate_main_py(proj_name, manifest)
    )
    
    # Write manifest.json
    (proj_path / "manifest.json").write_text(
        json.dumps(manifest, indent=4, sort_keys=True, ensure_ascii=False)
    )
    
    # Write requirements.txt
    (proj_path / "requirements.txt").write_text(
        f"truffle=={sdk_version}"
    ) 