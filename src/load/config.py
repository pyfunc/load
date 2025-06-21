"""
Configuration variables for Load
"""

from typing import Dict, Any

# Cache modułów w pamięci
_module_cache: Dict[str, Any] = {}

# Konfiguracja auto-print
AUTO_PRINT = True
PRINT_LIMIT = 1000
PRINT_TYPES = (str, int, float, list, dict, tuple)
