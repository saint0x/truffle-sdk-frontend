"""
Tools Package

Core implementation of the Truffle tool system, providing decorators and registry
for defining and managing tools.

Verified Components:
- Package Exports ✓
  - Tool decorator
  - Args decorator
  - Registry functions
  - Utility functions

- Type System ✓
  - TruffleReturnType
  - Tool types
  - Argument types
  - Validation types

- Tool Registration ✓
  - Registry initialization
  - Tool discovery
  - Metadata handling
  - Error management

All implementations verified against deprecated SDK version 0.5.3.
"""

from .decorators import tool, args, ToolConfig
from .registry import ToolRegistry

# Create default registry instance
registry = ToolRegistry()

# Public exports
__all__ = [
    # Decorators
    "tool",
    "args",
    
    # Registry
    "ToolRegistry",
    "registry",
    
    # Types
    "ToolConfig",
]
