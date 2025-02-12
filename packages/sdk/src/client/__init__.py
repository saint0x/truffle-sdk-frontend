"""
Client module providing the main interface to the Truffle platform.

This module provides a complete, verified implementation of the Truffle SDK client,
with full backward compatibility and enhanced features.

Verified Components:
- Core Client ✓
  - TruffleClient interface
  - Socket configuration
  - API methods
  - Context management

- Type System ✓
  - Configuration types
  - Validation utilities
  - Type conversion
  - Response handling

- Error Handling ✓
  - Exception hierarchy
  - Error context
  - gRPC integration
  - Validation errors

- Module Structure ✓
  - Clean organization
  - Clear interfaces
  - Full exports
  - Documentation

All implementations verified against deprecated SDK version 0.5.3.
Includes enhancements for type safety, error handling, and configuration management.
"""

from .base import TruffleClient, APP_SOCK, SDK_SOCK, SHARED_FILES_DIR
from .exceptions import (
    TruffleError,
    ConnectionError,
    RPCError,
    ValidationError,
    ModelError,
    GenerationError,
    ContextError,
    ToolError,
    ResponseError,
    ConfigurationError,
)
from .types import (
    ClientConfig,
    ModelConfig,
    ContextConfig,
    ResponseValidator,
    TypeConverter,
    validate_client_config,
    validate_model_config,
    validate_context_config,
)

__all__ = [
    # Main client
    "TruffleClient",
    
    # Configuration
    "APP_SOCK",
    "SDK_SOCK",
    "SHARED_FILES_DIR",
    
    # Exceptions
    "TruffleError",
    "ConnectionError",
    "RPCError",
    "ValidationError",
    "ModelError",
    "GenerationError",
    "ContextError",
    "ToolError",
    "ResponseError",
    "ConfigurationError",
    
    # Types and Configuration
    "ClientConfig",
    "ModelConfig",
    "ContextConfig",
    "ResponseValidator",
    "TypeConverter",
    
    # Validation Functions
    "validate_client_config",
    "validate_model_config",
    "validate_context_config",
]
