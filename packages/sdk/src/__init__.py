"""
Truffle SDK

A Python SDK for interacting with Truffle's AI platform.
Based on deprecated SDK version 0.5.3.
"""

from .client.grpc import GRPCClient
from .tools.utils import validate_tool_args
from .types.requests import (
    GenerateRequest,
    GetModelsRequest,
    SystemToolRequest,
    ToolUpdateRequest,
    UserRequest,
    EmbedRequest
)
from .types.responses import (
    GenerateResponse,
    GetModelsResponse,
    SystemToolResponse,
    SDKResponse,
    UserResponse,
    EmbedResponse
)

__version__ = "0.5.3"

__all__ = [
    # Client
    "GRPCClient",
    
    # Tools
    "validate_tool_args",
    
    # Request Types
    "GenerateRequest",
    "GetModelsRequest",
    "SystemToolRequest",
    "ToolUpdateRequest",
    "UserRequest",
    "EmbedRequest",
    
    # Response Types
    "GenerateResponse",
    "GetModelsResponse",
    "SystemToolResponse",
    "SDKResponse",
    "UserResponse",
    "EmbedResponse",
]
