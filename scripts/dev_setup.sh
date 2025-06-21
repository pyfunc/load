#!/bin/bash
# Development setup script

echo "🛠️ Setting up Load development environment..."

# Install dependencies
poetry install

# Install development dependencies
poetry add --group dev pytest pytest-cov black flake8 mypy

# Install pre-commit hooks
poetry add --group dev pre-commit
poetry run pre-commit install

echo "✅ Development environment ready!"
