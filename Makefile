.PHONY: help install test lint format build publish clean dev-setup examples

help:
	@echo "🔥 Load - Make commands"
	@echo ""
	@echo "📦 Package commands:"
	@echo "  install     Install dependencies"
	@echo "  build       Build package"
	@echo "  publish     Publish to PyPI"
	@echo ""
	@echo "🧪 Development commands:"
	@echo "  test        Run tests"
	@echo "  lint        Run linting"
	@echo "  format      Format code"
	@echo "  dev-setup   Setup development environment"
	@echo ""
	@echo "🧹 Utility commands:"
	@echo "  clean       Clean build artifacts"
	@echo "  examples    Run all example scripts"

install:
	poetry install

test:
	poetry run pytest

lint:
	poetry run flake8 src tests
	poetry run mypy src

format:
	poetry run black src tests examples

build:
	poetry version patch
	poetry build

publish: build
	poetry publish

clean:
	rm -rf dist/
	rm -rf build/
	rm -rf *.egg-info/
	rm -rf .pytest_cache/
	rm -rf htmlcov/
	find . -type d -name __pycache__ -delete
	find . -type f -name "*.pyc" -delete

dev-setup:
	./scripts/dev_setup.sh

examples:
	@echo "🚀 Running all examples..."
	@echo ""
	@echo "1. Running basic_usage.py..."
	@poetry run python examples/basic_usage.py
	@echo ""
	@echo "2. Running auto_print_examples.py..."
	@poetry run python examples/auto_print_examples.py
	@echo ""
	@echo "3. Running decorator_example.py..."
	@poetry run python examples/decorator_example.py
	@echo ""
	@echo "4. Running plot_example.py..."
	@poetry run python examples/plot_example.py
	@echo ""
	@echo "5. Running registry_examples.py..."
	@poetry run python examples/registry_examples.py
	@echo ""
	@echo "🎉 All examples completed successfully!"
