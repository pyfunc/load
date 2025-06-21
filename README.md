# 🔥 Load - Import z wieloma rejestrami
# README.md

```markdown
# 🔥 Load - Modern Python Import Alternative

Load is a modern alternative to Python's `import` system, inspired by the simplicity of Go and Groovy. It provides automatic package installation, intelligent caching, and magic import syntax.

## 🎯 Purpose

Load simplifies Python imports by:
- Reducing boilerplate code
- Automating package installation
- Improving developer productivity
- Making imports more intuitive

## 🚀 Quick Start

```bash
# Install with Poetry
poetry add load

# Or install from PyPI
pip install load
```

## 💡 Key Benefits

- 🚀 **Simpler imports**: Replace multiple `import` statements with a single `load` statement
- 🎯 **Smart package management**: Automatically installs missing packages
- 💾 **Faster development**: Built-in caching for faster repeated imports
- 📊 **Better feedback**: Shows loading status and errors clearly

## 📚 Documentation

For detailed documentation, please refer to:

- [📚 Installation Guide](https://github.com/pyfunc/load/blob/main/docs/installation.md)
- [💪 Usage Examples](https://github.com/pyfunc/load/blob/main/docs/usage.md)
- [📦 Features List](https://github.com/pyfunc/load/blob/main/docs/features.md)
- [🔧 API Reference](https://github.com/pyfunc/load/blob/main/docs/api.md)
- [🎯 Examples](https://github.com/pyfunc/load/tree/main/examples)

## 🤝 Contributing

We welcome contributions! Please see [CONTRIBUTING.md](https://github.com/pyfunc/load/blob/main/CONTRIBUTING.md) for guidelines.

## 📄 License

MIT License - see LICENSE file for details.

## 🔗 Links

- [GitHub Repository](https://github.com/pyfunc/load)
- [PyPI Package](https://pypi.org/project/load)
- [Examples](https://github.com/pyfunc/load/tree/main/examples)
- [Issues](https://github.com/pyfunc/load/issues)
- [PyPI](https://pypi.org/project/load/)

---

**Load - because imports should be simple!** 🚀
```

**Nie kombinuj z pip!** Load automatycznie wykrywa i instaluje z różnych źródeł - PyPI, GitHub, GitLab, prywatne rejestry, URL, lokalne pliki.

## 🚀 Instalacja

Skopiuj `load.py` do projektu. Zero konfiguracji.

## 💪 Podstawowe użycie

```python
from load import *

# PyPI (domyślnie)
http = requests()           # Auto-instaluje requests z PyPI
data = pd()                # pandas z PyPI

# GitHub  
awesome = load("user/awesome-lib")     # GitHub repo
ortools = load("google/or-tools")      # Google OR-Tools

# Lokalne
utils = load("./utils.py")             # Lokalny plik
config = load("../config.py")          # Względna ścieżka

# URL
remote = load("https://example.com/lib.py")  # Bezpośrednio z URL
```

## 🔧 Rejestry Python

### 📦 Publiczne rejestry

| Rejestr | Szacowana liczba pakietów | Przykład użycia |
|---------|---------------------------|-----------------|
| **PyPI** | ~500,000 pakietów | `load("requests")` |
| **GitHub** | ~miliony repozytoriów | `load("user/repo")` |
| **GitLab** | ~setki tysięcy | `load("gitlab.com/user/proj")` |
| **SourceForge** | ~starsze projekty | `load("url...")` |
| **Bitbucket** | ~tysiące | `load("url...")` |

### 🔒 Prywatne rejestry

```python
# Prywatny PyPI firmy
configure_private_registry(
    name="company",
    index_url="https://pypi.company.com/simple/"
)

# Prywatny GitLab z tokenem  
configure_private_registry(
    name="internal", 
    base_url="https://gitlab.company.com/",
    token="your-token"  # lub GITLAB_TOKEN env var
)

# Użyj
company_lib = load("internal-package", registry="company")
secret_tool = load("team/secret-sauce", registry="internal")
```

## 🎯 Smart Loading - automatyczne wykrywanie

Load automatycznie wykrywa skąd ładować:

```python
load("json")                    # → stdlib (nie instaluje)
load("requests")                # → PyPI  
load("user/repo")               # → GitHub
load("gitlab.com/user/proj")    # → GitLab
load("./file.py")               # → Lokalny plik
load("https://example.com/x.py") # → URL
```

## 🏢 Przykłady dla firm

### Startup z GitHub
```python
# Najnowsze z GitHub zamiast PyPI
ml_lib = load("huggingface/transformers")
selenium = load("SeleniumHQ/selenium/py") 
playwright = load("microsoft/playwright-python")
```

### Korporacja z prywatnymi rejestrami
```python
# Skonfiguruj rejestry firmy
configure_private_registry("nexus", 
    index_url="https://nexus.company.com/pypi/simple/")

configure_private_registry("artifactory",
    index_url="https://company.jfrog.io/pypi/simple/")

# Używaj
auth_lib = load("company-auth", registry="nexus")
internal_api = load("team-api-client", registry="artifactory")
```

### Projekt z mieszanymi źródłami
```python
def setup_project():
    return {
        # PyPI - stabilne wersje
        'web': load("fastapi"),
        'db': load("sqlalchemy"),
        
        # GitHub - najnowsze funkcje  
        'ai': load("openai/openai-python"),
        'scraping': load("microsoft/playwright-python"),
        
        # Prywatne - firmowe narzędzia
        'auth': load("auth-service", registry="company"),
        'monitoring': load("team/observability", registry="internal"),
        
        # Lokalne - logika biznesowa
        'models': load("./models.py"),
        'utils': load("./utils.py")
    }
```

## 🔧 Zarządzanie rejestrami

```python
# Lista dostępnych rejestrów
list_registries()

# Dodaj własny rejestr
add_registry("custom", {
    'index_url': 'https://pypi.custom.com/simple/',
    'install_cmd': [sys.executable, "-m", "pip", "install", "--index-url"],
    'description': 'Custom PyPI mirror'
})

# Szybka konfiguracja
configure_private_registry("maven-central", 
    index_url="https://maven.central.com/pypi/")
```

## 🚀 Przykłady projektów

### Data Science
```python
def setup_ds():
    return {
        'pd': load("pandas", "pd"),                    # PyPI
        'np': load("numpy", "np"),                     # PyPI  
        'latest_sklearn': load("scikit-learn/scikit-learn"), # GitHub
        'utils': load("./ds_utils.py")                 # Local
    }
```

### Web Development  
```python
def setup_web():
    return {
        'api': load("fastapi"),                        # PyPI
        'auth': load("company-sso", registry="nexus"), # Private
        'monitoring': load("team/apm-client", registry="gitlab"), # GitLab
        'models': load("./models.py")                  # Local
    }
```

### AI/ML Pipeline
```python
def setup_ai():
    return {
        'torch': load("pytorch/pytorch"),              # GitHub latest
        'transformers': load("huggingface/transformers"), # GitHub
        'custom_models': load("team/ml-models", registry="company"), # Private
        'preprocessing': load("./preprocess.py")        # Local
    }
```

## 📊 Popularne rejestry w praktyce

### Dla startupów
- **PyPI** - podstawowe biblioteki
- **GitHub** - najnowsze wersje, eksperymenty
- **Lokalne pliki** - własna logika

### Dla korporacji
- **PyPI** - sprawdzone, stable biblioteki
- **Prywatny PyPI** - firmowe pakiety
- **GitLab Enterprise** - internal repos
- **Artifactory/Nexus** - cache i security scanning

### Dla research
- **GitHub** - cutting-edge research code
- **PyPI** - etablowane biblioteki naukowe
- **URL** - papers with code, direct downloads

## 🔒 Bezpieczeństwo

```python
# Kontroluj źródła
ALLOWED_REGISTRIES = ['pypi', 'company', 'github-trusted']

def secure_load(name, registry=None):
    if registry not in ALLOWED_REGISTRIES:
        raise SecurityError(f"Registry {registry} not allowed")
    return load(name, registry=registry)
```

## 🎉 Dlaczego Load?

| Problem | Tradycyjnie | Z Load |
|---------|-------------|--------|
| Instalacja | `pip install pkg` | `load("pkg")` |
| GitHub repo | Clone, setup.py, pip install | `load("user/repo")` |
| Prywatny rejestr | Konfiguruj pip.conf | `load("pkg", registry="company")` |
| Różne źródła | Różne komendy | `load()` dla wszystkiego |
| Najnowsza wersja | Czekaj na PyPI | `load("user/repo")` z GitHub |

**Load - jeden interfejs do wszystkich rejestrów Python!** 🚀

---

**Skopiuj `load.py`, napisz `from load import *` i ładuj skąd chcesz!**

## 🔥 Podsumowanie - Load z rejestrami

Load z obsługą wszystkich głównych rejestrów Python:

### 📦 **Obsługiwane rejestry:**

1. **PyPI** (~500k pakietów) - `load("requests")`
2. **GitHub** (~miliony repozytoriów) - `load("user/repo")`  
3. **GitLab** (~setki tysięcy) - `load("gitlab.com/user/proj")`
4. **Prywatne PyPI** - `load("pkg", registry="company")`
5. **URL** - `load("https://example.com/lib.py")`
6. **Lokalne pliki** - `load("./utils.py")`

### 🚀 **Kluczowe funkcje:**

- **Smart detection** - automatycznie wykrywa skąd ładować
- **Auto-install** - instaluje co brakuje
- **Cache w RAM** - szybkie powtórne ładowanie
- **Prywatne rejestry** - obsługa firmowych PyPI/GitLab z tokenami
- **Zero config** - działa od razu

### 💪 **Użycie:**

```python
from load import *

# Podstawowe
http = requests()                           # PyPI
data = pd()                                # PyPI + alias

# GitHub (najnowsze wersje)
ai = load("openai/openai-python")          # GitHub
ml = load("huggingface/transformers")      # GitHub

# Prywatne firmy
auth = load("company-auth", registry="nexus")
api = load("team/api", registry="gitlab")

# Lokalne
utils = load("./utils.py")
```

### 🏢 **Dla firm:**

```python
# Skonfiguruj raz
configure_private_registry("company", 
    index_url="https://pypi.company.com/simple/")

# Używaj wszędzie
internal_lib = load("secret-package", registry="company")
```

### 🎯 **Główne zalety:**

1. **Jeden interfejs** do wszystkich źródeł
2. **Automatyczne wykrywanie** - nie musisz pamiętać skąd co
3. **Obsługa tokenów** dla prywatnych repozytoriów
4. **Szybkie** dzięki cache w RAM
5. **Proste jak w Go** - jedna funkcja `load()`

**Rezultat:** Zamiast kombinować z `pip install`, `git clone`, konfiguracją pip.conf - po prostu `load()` i działa! 🚀