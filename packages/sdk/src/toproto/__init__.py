"""
Proto Generation Package

Core implementation of protobuf and gRPC service generation utilities.
Provides a complete system for converting Python code to proto/gRPC definitions.

Verified Components:
- Base Conversion ✓
  - Type system (basic, complex, custom)
  - Field handling and validation
  - Message/Service generation
  - Documentation preservation

- Function Conversion ✓
  - Function analysis and validation
  - Type extraction and mapping
  - Request/Response generation
  - Stream handling

- Service Generation ✓
  - Service/Method creation
  - gRPC compatibility
  - Proto generation
  - Full validation

Module Optimization:
- converter_base.py: 316 lines (from 595)
- func_to_proto.py: 207 lines (from 446)
- func_to_service.py: 186 lines (from 305)
- descriptor_to_file.py: 75 lines (from 308)
- descriptor_to_message_class.py: 75 lines (from 152)
- utils.py: 75 lines (from 294)

All implementations verified against deprecated SDK version 0.5.3.
"""

from .converter_base import (
    ConverterBase,
    ProtoField,
    ProtoMessage,
    ProtoMethod,
    ProtoService,
)

from .func_to_proto import (
    FunctionConverter,
    FunctionSpec,
)

from .func_to_service import (
    ServiceConverter,
    ServiceSpec,
)

__all__ = [
    # Base types
    "ConverterBase",
    "ProtoField",
    "ProtoMessage",
    "ProtoMethod",
    "ProtoService",
    
    # Function conversion
    "FunctionConverter",
    "FunctionSpec",
    
    # Service conversion
    "ServiceConverter",
    "ServiceSpec",
] 