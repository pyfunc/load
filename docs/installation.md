# 🚀 Installation

Load can be installed using several methods:

## 📦 Using Poetry

```bash
poetry add load
```

## 📦 Using pip

```bash
pip install load
```

## 📦 Development Installation

For development purposes, clone the repository and install in development mode:

```bash
git clone https://github.com/pyfunc/load.git
cd load
poetry install
```

## 🔄 System Requirements

- Python 3.8+
- pip
- Poetry (recommended for development)

## 📝 Environment Variables

Load supports several environment variables for configuration:

- `LOAD_CACHE_SIZE`: Maximum cache size in bytes
- `LOAD_AUTO_PRINT`: Enable/disable auto-print globally (1/0)
- `LOAD_PRINT_LIMIT`: Character limit for auto-print
- `LOAD_NO_INSTALL`: Disable automatic package installation (1/0)

## 🔄 Updating Load

To update Load to the latest version:

```bash
poetry add load@latest  # If using Poetry
pip install --upgrade load  # If using pip
```

## 🔗 Related Resources

- [Main Documentation](./index.md)
- [Usage Examples](./usage.md)
- [API Reference](./api.md)
- [Development Guide](./development.md)
- [GitHub Repository](https://github.com/pyfunc/load)
- [PyPI Package](https://pypi.org/project/load)
