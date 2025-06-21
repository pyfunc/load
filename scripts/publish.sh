#!/bin/bash
# Publish script for Load

echo "🚀 Publishing Load package..."

# Build first
./scripts/build.sh

# Publish to PyPI
echo "📤 Publishing to PyPI..."
poetry publish

echo "✅ Published!"
