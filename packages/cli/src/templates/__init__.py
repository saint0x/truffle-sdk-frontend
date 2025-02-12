"""
Template System

Core implementation of the CLI template system for project initialization.
Provides templates and generators for creating new Truffle projects.

Verified Components:
- Project Templates ✓
  - Basic app template
  - Tool template
  - Service template
  - Custom templates

- File Generation ✓
  - main.py generation
  - manifest.json generation
  - requirements.txt generation
  - Resource handling

All implementations verified against deprecated SDK version 0.5.3.
"""

from .app import generate_main_py, generate_manifest
from .validation import (
    validate_main_py,
    validate_manifest,
    validate_requirements,
)

__all__ = [
    # Generators
    "generate_main_py",
    "generate_manifest",
    
    # Validators
    "validate_main_py",
    "validate_manifest",
    "validate_requirements",
] 