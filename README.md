# Truffle SDK

Core SDK and CLI tools.

## Usage

### Creating a New Project

1. Initialize a new project:
   ```bash
   truffle init MyApp
   ```
   This will create a new project with:
   - `main.py` - Your tool implementation
   - `manifest.json` - Project configuration
   - `requirements.txt` - Dependencies
   - `icon.png` - Default app icon

2. Build your project:
   ```bash
   cd MyApp
   truffle build
   ```
   This will create a `.truffle` package ready for distribution.

### Project Structure

```
MyApp/
├── main.py              # Tool implementation
├── manifest.json        # Project configuration
├── requirements.txt     # Dependencies
└── icon.png            # App icon
```

## Repository Structure

```
packages/
├── sdk/                    # Core SDK implementation
│   ├── src/
│   │   ├── client/        # Client implementations (gRPC, base)
│   │   ├── platform/      # Protocol buffer definitions
│   │   ├── tools/         # Tool management utilities
│   │   ├── toproto/       # Proto conversion utilities
│   │   └── types/         # Type definitions and validation
│   └── tests/             # SDK test suite
│
└── cli/                   # CLI implementation
    └── src/
        ├── commands/      # CLI commands (init, build, run)
        ├── utils/         # CLI utilities
        └── assets/        # Static assets
```

## Core Components

- **SDK**: `/packages/sdk/src/`
  - Client Interface & gRPC Implementation
  - Protocol Buffer Integration
  - Tool Management System
  - Type System & Validation
  - Proto Conversion Utilities

- **CLI**: `/packages/cli/src/`
  - Project Management
  - Build System
  - Runtime Environment
  - Configuration Management
  - Logging System

## Documentation

- Refactor Details: `REFACTOR-VERIFY.md`
- API Documentation: `/packages/sdk/docs/`
- CLI Usage: `/packages/cli/docs/`

## Version

Current stable version: 1.0.0

## License

MIT