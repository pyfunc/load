# Contributing to Load

🎉 Thanks for your interest in contributing to Load!

## Development Setup

1. Clone the repository
2. Install Poetry: `curl -sSL https://install.python-poetry.org | python3 -`
3. Setup development environment: `make dev-setup`
4. Run tests: `make test`

## Development Workflow

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Make your changes
4. Run tests: `make test`
5. Run linting: `make lint`
6. Format code: `make format`
7. Commit changes: `git commit -m 'Add amazing feature'`
8. Push to branch: `git push origin feature/amazing-feature`
9. Open a Pull Request

## Code Style

- Use Black for formatting
- Follow PEP 8 guidelines
- Add type hints where appropriate
- Write tests for new features
- Update documentation

## Testing

```bash
# Run all tests
make test

# Run specific test
poetry run pytest tests/test_core.py::TestLoad::test_load_stdlib_module

# Run with coverage
poetry run pytest --cov=src/load --cov-report=html
```

## Documentation

- Update docstrings for new functions
- Add examples for new features
- Update README.md if needed

## Questions?

Open an issue or start a discussion on GitHub!
