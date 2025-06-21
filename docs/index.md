# Load Documentation

## Installation

```bash
pip install load
```

## Basic Usage

```python
import load

# Load packages
requests_lib = load.requests
numpy_lib = load.np
```

## Advanced Features

### Multiple Registries

- PyPI (default)
- GitHub repositories
- GitLab repositories
- Private registries
- Direct URLs
- Local files

### Auto-print

Load automatically displays results like in Jupyter notebooks.

### Registry Configuration

```python
load.configure_private_registry(
    "company",
    index_url="https://pypi.company.com/simple/"
)
```

## Examples

See `/examples` for complete examples.
