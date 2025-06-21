#!/bin/bash
# Build script for Load

echo "🔨 Building Load package..."

# Run tests
echo "🧪 Running tests..."
poetry run pytest

# Build package
echo "📦 Building package..."
poetry build

echo "✅ Build completed!"
