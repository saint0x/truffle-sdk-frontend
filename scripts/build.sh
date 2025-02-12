#!/bin/bash
set -e

# Generate protobuf files
echo "Generating protobuf files..."
python -m grpc_tools.protoc -I./protos --python_out=./packages/sdk/src/platform --grpc_python_out=./packages/sdk/src/platform ./protos/*.proto

# Build packages
echo "Building packages..."
python -m build

# Run tests
echo "Running tests..."
pytest tests/

echo "Build complete!"
