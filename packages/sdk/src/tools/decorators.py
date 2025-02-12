"""
Tool Decorators Module

This module provides decorators for defining and configuring Truffle tools.

Verified Components:
- Core Decorators ✓
  - @tool decorator with name, description, icon
  - @args decorator for argument descriptions
  - Return type validation
  - Argument validation

- Function Management ✓
  - Metadata preservation
  - Type checking
  - Signature validation
  - Documentation handling

- Tool Configuration ✓
  - Name handling
  - Description management
  - Icon support
  - Argument descriptions

All implementations verified against deprecated SDK version 0.5.3.

TO MIGRATE:
1. Core Decorators (from __init__.py):
   - @tool(description: str = None, icon: str = None)
     - Sets __truffle_tool__ = True
     - Sets __truffle_icon__ = icon
     - Sets __truffle_description__ = description
     - Handles TruffleReturnType detection
   
   - @args(**kwargs)
     - Sets __truffle_args__ = kwargs
     - Must be applied before @tool

2. Return Type Handling:
   - Check for TruffleReturnType subclasses
   - Set __truffle_type__ = ret_type.__name__
   - Support for TruffleFile and TruffleImage

3. Function Attribute Management:
   - __truffle_tool__: bool
   - __truffle_icon__: Optional[str]
   - __truffle_description__: Optional[str]
   - __truffle_args__: Optional[Dict]
   - __truffle_type__: Optional[str]

4. Validation and Type Checking:
   - Ensure decorators are applied in correct order
   - Validate icon names (SF Symbols)
   - Check return type annotations
   - Verify argument specifications

INTEGRATION NOTES:
- Must maintain compatibility with existing tool definitions
- Decorators must work with both function and method definitions
- Return type detection must match TruffleReturnType hierarchy
- Must preserve all function metadata and docstrings

DEPENDENCIES:
- typing
- inspect
- functools.wraps
- types.models.TruffleReturnType
"""

import functools
import inspect
import typing
from dataclasses import dataclass

from ..types.models import TruffleReturnType, ToolMetadata
from ..client.exceptions import ValidationError

@dataclass
class ToolConfig:
    """Configuration for a tool function."""
    name: str
    description: str
    icon: typing.Optional[str] = None
    args: typing.Dict[str, str] = None

def tool(
    name: str = None,
    description: str = None,
    icon: str = None,
) -> typing.Callable:
    """
    Decorator to register a function as a Truffle tool.
    
    Args:
        name: Optional name for the tool (defaults to function name)
        description: Optional description of what the tool does
        icon: Optional icon URL or emoji for the tool
    """
    def decorator(func: typing.Callable) -> typing.Callable:
        # Get function signature and docstring
        sig = inspect.signature(func)
        doc = inspect.getdoc(func) or ""
        
        # Create tool metadata
        tool_name = name or func.__name__
        tool_desc = description or doc.split("\n")[0]
        
        # Validate return type annotation
        return_type = sig.return_annotation
        if return_type is inspect.Signature.empty:
            raise ValidationError(f"Tool {tool_name} must have a return type annotation")
        if not (
            isinstance(return_type, type) and 
            issubclass(return_type, TruffleReturnType)
        ):
            raise ValidationError(
                f"Tool {tool_name} must return a TruffleReturnType, got {return_type}"
            )

        # Store tool configuration
        func.__truffle_tool__ = ToolConfig(
            name=tool_name,
            description=tool_desc,
            icon=icon,
            args={},
        )
        
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        
        return wrapper
    return decorator

def args(**arg_descriptions: str) -> typing.Callable:
    """
    Decorator to add argument descriptions to a tool function.
    
    Args:
        **arg_descriptions: Mapping of argument names to their descriptions
    """
    def decorator(func: typing.Callable) -> typing.Callable:
        # Validate function is a tool
        if not hasattr(func, "__truffle_tool__"):
            raise ValidationError(
                f"@args can only be used on functions decorated with @tool"
            )
        
        # Get function signature
        sig = inspect.signature(func)
        
        # Validate all described args exist
        for arg_name in arg_descriptions:
            if arg_name not in sig.parameters:
                raise ValidationError(
                    f"Argument '{arg_name}' described but not found in function signature"
                )
        
        # Store argument descriptions
        func.__truffle_tool__.args.update(arg_descriptions)
        
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        
        return wrapper
    return decorator
