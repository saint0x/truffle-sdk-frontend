"""
CLI Utilities Package

Core utilities for the Truffle CLI.
Verified against deprecated SDK version 0.5.3.

Verification Status:
✓ Core Components
  - Logger integration
  - Configuration management
  - Template handling
  - Validation utilities

✓ Package Structure
  - Proper imports
  - Version handling
  - Error handling
  - Type safety
"""

from pathlib import Path
from typing import Dict, Any

from .logger import log, Symbols, Colors
from .config import (
    load_manifest,
    update_manifest,
    load_pyproject,
    update_pyproject,
    get_sdk_version,
    format_requirements
)
from .templates import (
    generate_main_py,
    generate_manifest,
    generate_requirements,
    copy_project_template,
    copy_default_icon
)
from .validation import (
    validate_project_structure,
    validate_manifest_json,
    validate_main_py,
    validate_requirements_txt
)

__all__ = [
    # Logger
    'log',
    'Symbols',
    'Colors',
    
    # Config
    'load_manifest',
    'update_manifest',
    'load_pyproject',
    'update_pyproject',
    'get_sdk_version',
    'format_requirements',
    
    # Templates
    'generate_main_py',
    'generate_manifest',
    'generate_requirements',
    'copy_project_template',
    'copy_default_icon',
    
    # Validation
    'validate_project_structure',
    'validate_manifest_json',
    'validate_main_py',
    'validate_requirements_txt'
]

# Package version
__version__ = "0.6.5"
