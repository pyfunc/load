# 🛠️ Development Guide

This guide provides information for developers who want to contribute to the `load` module.

## Table of Contents
- [Getting Started](#getting-started)
- [Development Setup](#development-setup)
- [Code Style](#code-style)
- [Testing](#testing)
- [Documentation](#documentation)
- [Pull Request Process](#pull-request-process)
- [Release Process](#release-process)

## Getting Started

### Prerequisites
- Python 3.8+
- Git
- pip

### Repository Structure

```
load/
├── src/                    # Source code
│   └── load/              # Main package
├── tests/                  # Test files
├── examples/               # Example scripts
├── docs/                   # Documentation
└── setup.py               # Package configuration
```

## Development Setup

1. **Fork and clone** the repository:
   ```bash
   git clone https://github.com/yourusername/load.git
   cd load
   ```

2. **Set up a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install development dependencies**:
   ```bash
   pip install -e .[dev]
   ```

4. **Run tests** to verify your setup:
   ```bash
   pytest
   ```

## Code Style

We use the following tools to maintain code quality:

- **Black** for code formatting
- **isort** for import sorting
- **Flake8** for linting
- **Mypy** for type checking

Run the formatting and linting checks:

```bash
black src tests
iSort src tests
flake8 src tests
mypy src
```

## Testing

### Running Tests

```bash
# Run all tests
pytest

# Run a specific test file
pytest tests/test_core.py

# Run with coverage report
pytest --cov=load tests/
```

### Writing Tests

- Put test files in the `tests/` directory
- Name test files with `test_` prefix (e.g., `test_core.py`)
- Use descriptive test function names starting with `test_`
- Follow the Arrange-Act-Assert pattern

Example test:

```python
def test_load_module():
    # Arrange
    module_name = "json"
    
    # Act
    result = load(module_name)
    
    # Assert
    assert result is not None
    assert hasattr(result, 'dumps')
```

## Documentation

### Building Documentation

We use Markdown for documentation. To build the documentation locally:

1. Install documentation dependencies:
   ```bash
   pip install -e .[docs]
   ```

2. Build the documentation:
   ```bash
   mkdocs build
   ```

3. Serve the documentation locally:
   ```bash
   mkdocs serve
   ```

### Documentation Guidelines

- Keep documentation clear and concise
- Use consistent formatting
- Include code examples
- Update documentation when making API changes
- Use Mermaid.js for diagrams (see [diagrams.md](diagrams.md))

## Pull Request Process

1. Create a new branch for your feature/fix:
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. Make your changes and commit them:
   ```bash
   git commit -m "Add your commit message"
   ```

3. Push to your fork:
   ```bash
   git push origin feature/your-feature-name
   ```

4. Open a pull request against the `main` branch

## Release Process

1. Update the version in `src/load/__init__.py`
2. Update the changelog in `CHANGELOG.md`
3. Create a release tag:
   ```bash
   git tag -a v1.0.0 -m "Version 1.0.0"
   git push origin v1.0.0
   ```
4. Create a GitHub release with release notes

## Getting Help

If you need help or have questions:

- Open an issue on GitHub
- Join our community chat (if applicable)
- Check the [FAQ](faq.md)

## Code of Conduct

Please note that this project is governed by the [Contributor Covenant Code of Conduct](CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code.
