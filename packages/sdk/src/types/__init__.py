"""
Type system module providing core types and type utilities.

Components:
- Return Types (TruffleReturnType, TruffleFile, TruffleImage)
- Tool Types (ToolMetadata, ToolRegistry)
- Application Types (AppMetadata)
- Type Utilities (validation, conversion)

All implementations verified against deprecated SDK version 0.5.3.
"""

from .models import (
    TruffleReturnType,
    TruffleFile,
    TruffleImage,
    ToolMetadata,
    ToolRegistry,
    AppMetadata,
    is_truffle_type,
    is_file_type,
    is_image_type,
    validate_type,
    to_proto_type,
    from_proto_type,
)

__all__ = [
    "TruffleReturnType",
    "TruffleFile",
    "TruffleImage",
    "ToolMetadata",
    "ToolRegistry",
    "AppMetadata",
    "is_truffle_type",
    "is_file_type",
    "is_image_type",
    "validate_type",
    "to_proto_type",
    "from_proto_type",
]
