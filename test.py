#!/usr/bin/env python3
"""
Skrypt weryfikacji projektu Load
Sprawdza czy wszystkie pliki zostały utworzone i czy projekt jest gotowy
"""

import os
import sys
import subprocess
from pathlib import Path
from typing import List, Tuple


class Colors:
    """ANSI color codes"""
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    BOLD = '\033[1m'
    END = '\033[0m'


def print_colored(text: str, color: str = Colors.WHITE):
    """Print colored text"""
    print(f"{color}{text}{Colors.END}")


def print_header(text: str):
    """Print section header"""
    print_colored(f"\n🔥 {text}", Colors.BOLD + Colors.CYAN)
    print_colored("=" * (len(text) + 4), Colors.CYAN)


def check_file_exists(file_path: str) -> bool:
    """Check if file exists"""
    return Path(file_path).exists()


def check_directory_exists(dir_path: str) -> bool:
    """Check if directory exists"""
    return Path(dir_path).is_dir()


def run_command(command: List[str], capture_output: bool = True) -> Tuple[bool, str]:
    """Run shell command and return success status and output"""
    try:
        result = subprocess.run(
            command,
            capture_output=capture_output,
            text=True,
            timeout=30
        )
        return result.returncode == 0, result.stdout if capture_output else ""
    except (subprocess.TimeoutExpired, FileNotFoundError):
        return False, ""


def check_project_structure():
    """Check project structure"""
    print_header("STRUKTURA PROJEKTU")

    # Required directories
    directories = [
        "src",
        "src/load",
        "tests",
        "docs",
        "examples",
        "scripts"
    ]

    # Required files
    files = [
        # Root files
        "pyproject.toml",
        "README.md",
        "LICENSE",
        "CHANGELOG.md",
        "CONTRIBUTING.md",
        "Makefile",
        ".gitignore",
        ".pre-commit-config.yaml",

        # Source files
        "src/load/__init__.py",
        "src/load/core.py",
        "src/load/registry.py",
        "src/load/shortcuts.py",
        "src/load/utils.py",
        "src/load/magic.py",

        # Tests
        "tests/__init__.py",
        "tests/test_core.py",
        "tests/test_registry.py",
        "tests/test_shortcuts.py",

        # Documentation
        "docs/index.md",

        # Examples
        "examples/basic_usage.py",
        "examples/registry_examples.py",
        "examples/auto_print_examples.py",

        # Scripts
        "scripts/build.sh",
        "scripts/publish.sh",
        "scripts/dev_setup.sh"
    ]

    # Check directories
    missing_dirs = []
    for directory in directories:
        if check_directory_exists(directory):
            print_colored(f"✅ {directory}/", Colors.GREEN)
        else:
            print_colored(f"❌ {directory}/ - BRAK!", Colors.RED)
            missing_dirs.append(directory)

    # Check files
    missing_files = []
    for file in files:
        if check_file_exists(file):
            print_colored(f"✅ {file}", Colors.GREEN)
        else:
            print_colored(f"❌ {file} - BRAK!", Colors.RED)
            missing_files.append(file)

    return len(missing_dirs) == 0 and len(missing_files) == 0, missing_dirs, missing_files


def check_poetry():
    """Check Poetry installation and configuration"""
    print_header("POETRY")

    # Check if Poetry is installed
    success, _ = run_command(["poetry", "--version"])
    if not success:
        print_colored("❌ Poetry nie jest zainstalowany!", Colors.RED)
        print_colored("   Zainstaluj: curl -sSL https://install.python-poetry.org | python3 -", Colors.YELLOW)
        return False

    print_colored("✅ Poetry zainstalowany", Colors.GREEN)

    # Check pyproject.toml
    if not check_file_exists("pyproject.toml"):
        print_colored("❌ pyproject.toml nie istnieje!", Colors.RED)
        return False

    # Validate Poetry config
    success, output = run_command(["poetry", "check"])
    if success:
        print_colored("✅ Konfiguracja Poetry poprawna", Colors.GREEN)
    else:
        print_colored("❌ Błąd konfiguracji Poetry", Colors.RED)
        print_colored(f"   {output}", Colors.YELLOW)

    return success


def check_python_syntax():
    """Check Python syntax of all source files"""
    print_header("SKŁADNIA PYTHON")

    python_files = []

    # Find all Python files
    for root, dirs, files in os.walk("src"):
        for file in files:
            if file.endswith(".py"):
                python_files.append(os.path.join(root, file))

    for root, dirs, files in os.walk("tests"):
        for file in files:
            if file.endswith(".py"):
                python_files.append(os.path.join(root, file))

    for root, dirs, files in os.walk("examples"):
        for file in files:
            if file.endswith(".py"):
                python_files.append(os.path.join(root, file))

    syntax_errors = []
    for file in python_files:
        success, output = run_command(["python3", "-m", "py_compile", file])
        if success:
            print_colored(f"✅ {file}", Colors.GREEN)
        else:
            print_colored(f"❌ {file} - błąd składni!", Colors.RED)
            syntax_errors.append(file)

    return len(syntax_errors) == 0, syntax_errors


def check_imports():
    """Check if Load can be imported"""
    print_header("IMPORTY")

    # Add src to Python path
    sys.path.insert(0, str(Path("src").absolute()))

    try:
        import load
        print_colored("✅ import load - sukces", Colors.GREEN)

        # Test basic functionality
        json_lib = load.load('json', silent=True)
        if hasattr(json_lib, 'loads'):
            print_colored("✅ load.load('json') - sukces", Colors.GREEN)
        else:
            print_colored("❌ load.load('json') - błąd funkcjonalności", Colors.RED)
            return False

        # Test magic import
        try:
            json_lib2 = load.json
            print_colored("✅ load.json (magic import) - sukces", Colors.GREEN)
        except Exception as e:
            print_colored(f"❌ load.json (magic import) - błąd: {e}", Colors.RED)
            return False

        return True

    except Exception as e:
        print_colored(f"❌ import load - błąd: {e}", Colors.RED)
        return False


def check_tests():
    """Check if tests can run"""
    print_header("TESTY")

    if not check_file_exists("tests/test_core.py"):
        print_colored("❌ Brak plików testowych", Colors.RED)
        return False

    # Try to run tests
    success, output = run_command(["python3", "-m", "pytest", "tests/", "-v"])
    if success:
        print_colored("✅ Testy przeszły pomyślnie", Colors.GREEN)
    else:
        print_colored("❌ Testy nie przeszły", Colors.RED)
        print_colored("   Sprawdź czy pytest jest zainstalowany: pip install pytest", Colors.YELLOW)

    return success


def check_examples():
    """Check if examples work"""
    print_header("PRZYKŁADY")

    examples = [
        "examples/basic_usage.py",
        "examples/registry_examples.py",
        "examples/auto_print_examples.py"
    ]

    working_examples = 0
    for example in examples:
        if check_file_exists(example):
            success, output = run_command(["python3", example])
            if success:
                print_colored(f"✅ {example}", Colors.GREEN)
                working_examples += 1
            else:
                print_colored(f"❌ {example} - błąd wykonania", Colors.RED)
        else:
            print_colored(f"❌ {example} - brak pliku", Colors.RED)

    return working_examples == len(examples)


def check_scripts():
    """Check if scripts are executable"""
    print_header("SKRYPTY")

    scripts = [
        "scripts/build.sh",
        "scripts/publish.sh",
        "scripts/dev_setup.sh"
    ]

    executable_scripts = 0
    for script in scripts:
        if check_file_exists(script):
            if os.access(script, os.X_OK):
                print_colored(f"✅ {script} - wykonywalny", Colors.GREEN)
                executable_scripts += 1
            else:
                print_colored(f"⚠️  {script} - nie wykonywalny", Colors.YELLOW)
                print_colored(f"   Uruchom: chmod +x {script}", Colors.YELLOW)
        else:
            print_colored(f"❌ {script} - brak pliku", Colors.RED)

    return executable_scripts >= len(scripts) - 1  # Allow one script to be non-executable


def print_summary(results: dict):
    """Print verification summary"""
    print_header("PODSUMOWANIE")

    total_checks = len(results)
    passed_checks = sum(1 for result in results.values() if result)

    print_colored(f"📊 Wyniki weryfikacji: {passed_checks}/{total_checks}", Colors.BOLD)

    for check_name, result in results.items():
        status = "✅ PASS" if result else "❌ FAIL"
        color = Colors.GREEN if result else Colors.RED
        print_colored(f"   {check_name}: {status}", color)

    if passed_checks == total_checks:
        print_colored("\n🎉 PROJEKT LOAD JEST GOTOWY!", Colors.BOLD + Colors.GREEN)
        print_colored("\n🚀 Następne kroki:", Colors.BOLD)
        print_colored("1. cd load", Colors.CYAN)
        print_colored("2. poetry install", Colors.CYAN)
        print_colored("3. poetry run pytest", Colors.CYAN)
        print_colored("4. poetry build", Colors.CYAN)
    else:
        print_colored(f"\n⚠️  PROJEKT WYMAGA POPRAWEK ({total_checks - passed_checks} błędów)",
                      Colors.BOLD + Colors.YELLOW)
        print_colored("\n🔧 Sprawdź błędy powyżej i popraw", Colors.YELLOW)


def main():
    """Main verification function"""
    print_colored("🔥 Load Project Verification", Colors.BOLD + Colors.PURPLE)
    print_colored("Sprawdzam projekt Load...\n", Colors.PURPLE)

    # Change to project directory if it exists
    if check_directory_exists("load"):
        os.chdir("load")
        print_colored("📁 Przełączam do katalogu load", Colors.CYAN)

    # Run all checks
    results = {}

    structure_ok, missing_dirs, missing_files = check_project_structure()
    results["Struktura projektu"] = structure_ok

    results["Poetry"] = check_poetry()

    syntax_ok, syntax_errors = check_python_syntax()
    results["Składnia Python"] = syntax_ok

    results["Importy Load"] = check_imports()
    results["Testy"] = check_tests()
    results["Przykłady"] = check_examples()
    results["Skrypty"] = check_scripts()

    # Print detailed errors if any
    if missing_dirs or missing_files:
        print_colored("\n📋 Brakujące elementy:", Colors.YELLOW)
        for dir_name in missing_dirs:
            print_colored(f"   📁 {dir_name}/", Colors.RED)
        for file_name in missing_files:
            print_colored(f"   📄 {file_name}", Colors.RED)

    if syntax_errors:
        print_colored("\n🐍 Błędy składni:", Colors.YELLOW)
        for file_name in syntax_errors:
            print_colored(f"   📄 {file_name}", Colors.RED)

    # Print summary
    print_summary(results)


if __name__ == "__main__":
    main()