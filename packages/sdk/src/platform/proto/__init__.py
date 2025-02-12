"""
Proto Conversion Package

Core implementation of protobuf message conversion and validation utilities.

Verified Components:
- Type Conversion ✓
  - Python to Proto
  - Proto to Python
  - Type validation
  - Error handling

- Message Handling ✓
  - Request messages
  - Response messages
  - Stream messages
  - Error messages

All implementations verified against deprecated SDK version 0.5.3.
"""

from .converters import (
    to_proto_type,
    from_proto_type,
    to_proto_content,
    from_proto_content,
    to_proto_request,
    from_proto_response,
    to_proto_app_metadata,
    from_proto_app_metadata,
    message_to_dict,
    dict_to_message,
)

from .validation import (
    validate_truffle_type,
    validate_proto_type,
    validate_content_role,
    validate_proto_content,
    validate_tool_metadata,
    validate_tool_request,
    validate_tool_response,
    validate_app_metadata,
    validate_generate_request,
    validate_generate_response,
)

__all__ = [
    # Converters
    "to_proto_type",
    "from_proto_type",
    "to_proto_content",
    "from_proto_content",
    "to_proto_request",
    "from_proto_response",
    "to_proto_app_metadata",
    "from_proto_app_metadata",
    "message_to_dict",
    "dict_to_message",
    
    # Validation
    "validate_truffle_type",
    "validate_proto_type",
    "validate_content_role",
    "validate_proto_content",
    "validate_tool_metadata",
    "validate_tool_request",
    "validate_tool_response",
    "validate_app_metadata",
    "validate_generate_request",
    "validate_generate_response",
] 