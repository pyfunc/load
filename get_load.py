#!/usr/bin/env python
"""
Install load via curl/Invoke-WebRequest.

Usage:
    curl -sSL https://load.pyfunc.com | python3 -
    curl -sSL https://load.pyfunc.com | python2 -
    (Invoke-WebRequest -Uri https://load.pyfunc.com -UseBasicParsing).Content | py -
"""

import sys
import os
import re
import subprocess
import tempfile
import urllib.request
import platform
import json
from pathlib import Path


# Python version compatibility
if sys.version_info < (2, 7):
    print("Error: Python 2.7 or higher is required")
    sys.exit(1)


def get_latest_version():
    """Get the latest version from PyPI."""
    try:
        response = urllib.request.urlopen('https://pypi.org/pypi/load/json')
        data = json.loads(response.read())
        return data['info']['version']
    except Exception as e:
        print(f"Error fetching latest version: {e}")
        return None


def get_pip_command():
    """Get the pip command based on Python version."""
    if sys.version_info >= (3, 0):
        return 'pip3' if platform.system() != 'Windows' else 'pip3'
    return 'pip' if platform.system() != 'Windows' else 'pip'


def install_load():
    """Install load using pip."""
    pip_cmd = get_pip_command()
    try:
        subprocess.check_call([pip_cmd, 'install', '--upgrade', 'load'])
        print("\n✅ load has been successfully installed!")
        print("You can now use it by importing or using the load command.")
    except subprocess.CalledProcessError as e:
        print(f"\n❌ Error installing load: {e}")
        sys.exit(1)


def check_pip():
    """Check if pip is installed."""
    pip_cmd = get_pip_command()
    try:
        subprocess.check_call([pip_cmd, '--version'])
        return True
    except subprocess.CalledProcessError:
        print("❌ Error: pip is not installed. Please install pip first.")
        return False


def main():
    print("\n🐍 Installing load...")
    
    # Check Python version
    print(f"✅ Python {sys.version.split()[0]} detected")
    
    # Check pip
    if not check_pip():
        sys.exit(1)
    
    # Get latest version
    latest_version = get_latest_version()
    if latest_version:
        print(f"✅ Latest version: {latest_version}")
    
    # Install load
    install_load()


if __name__ == '__main__':
    main()
