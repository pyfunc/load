# 🔥 Load - Modern Python Import Alternative

Load is a modern alternative to Python's `import` system, inspired by the simplicity of Go and Groovy. It provides automatic package installation, intelligent caching, and magic import syntax.

## 📚 Documentation Overview

> **Table of Contents**
> - [🚀 Installation](./installation.md)
> - [💪 Basic Usage](./usage.md)
> - [📦 Features](./features.md)
> - [🧠 How It Works](./internals.md)
> - [🔧 API Reference](./api.md)
> - [🎯 Examples](./examples.md)
> - [🔧 Development](./development.md)
> - [🔒 Security](./security.md)
> - [📄 License](./license.md)

## 🚀 Quick Start

```bash
# Install with Poetry
poetry add load

# Or install from PyPI
pip install load
```

## 💪 Usage Example

```python
import load

# Magic import - everything through dot notation
json_lib = load.json
os_lib = load.os
sys_lib = load.sys

# Auto-install external packages
requests_lib = load.requests  # Automatically installs requests
pandas_lib = load.pd          # Automatically installs pandas
```

## 📚 Detailed Documentation

For detailed documentation, please refer to the individual sections in the sidebar.

## 🔗 Related Resources

- [GitHub Repository](https://github.com/pyfunc/load)
- [PyPI Package](https://pypi.org/project/load)
- [Examples](https://github.com/pyfunc/load/tree/main/examples)
- [Development Guide](./development.md)
- [API Reference](./api.md)
- [Security Considerations](./security.md)
