"""
Platform module providing core gRPC service definitions and proto types.

This module implements the core platform interface for the Truffle SDK,
verified against the deprecated SDK version 0.5.3.

Verified Components:
- Proto Definitions ✓
  - Service interfaces
  - Message types
  - RPC methods
  - Type definitions

- Platform Tools ✓
  - Tool registration
  - Tool execution
  - Tool validation

- Proto Conversion ✓
  - Type conversion
  - Message serialization
  - Response handling

All implementations maintain backward compatibility while adding
improved type safety and error handling.
"""

from . import sdk_pb2
from . import sdk_pb2_grpc

__all__ = ["sdk_pb2", "sdk_pb2_grpc"]

# Package initialization will go here
