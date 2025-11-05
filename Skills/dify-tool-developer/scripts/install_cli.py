#!/usr/bin/env python3
"""
Dify CLI Installer Helper Script

Automatically downloads, installs, and configures the Dify plugin CLI
for the current operating system and architecture.

Usage:
    python scripts/install_cli.py [--version VERSION] [--path PATH]
"""

import os
import sys
import platform
import urllib.request
import json
import stat
from typing import Tuple

def detect_platform() -> Tuple[str, str]:
    """
    Detect current OS and architecture.

    Returns:
        Tuple of (os_name, arch) compatible with Dify release naming
    """
    system = platform.system().lower()
    machine = platform.machine().lower()

    # Map OS names
    os_map = {
        'darwin': 'darwin',
        'linux': 'linux',
        'windows': 'windows'
    }

    # Map architectures
    arch_map = {
        'x86_64': 'amd64',
        'amd64': 'amd64',
        'arm64': 'arm64',
        'aarch64': 'arm64',
    }

    os_name = os_map.get(system)
    arch = arch_map.get(machine)

    if not os_name or not arch:
        raise Exception(f"Unsupported platform: {system} {machine}")

    return os_name, arch


def get_latest_release_version() -> str:
    """
    Fetch the latest release version from GitHub API.

    Returns:
        Version string (e.g., "0.4.0")
    """
    api_url = "https://api.github.com/repos/langgenius/dify-plugin-daemon/releases/latest"

    try:
        with urllib.request.urlopen(api_url, timeout=10) as response:
            data = json.loads(response.read().decode())
            version = data['tag_name']
            return version.lstrip('v')
    except Exception as e:
        print(f"Warning: Could not fetch latest version: {e}")
        print("Using default version: 0.4.0")
        return "0.4.0"


def download_cli(version: str, os_name: str, arch: str, target_dir: str = ".") -> str:
    """
    Download Dify CLI binary.

    Args:
        version: Release version
        os_name: Operating system
        arch: Architecture
        target_dir: Target directory

    Returns:
        Path to downloaded binary
    """
    binary_name = f"dify-plugin-{os_name}-{arch}"
    if os_name == 'windows':
        binary_name += '.exe'

    base_url = "https://github.com/langgenius/dify-plugin-daemon/releases/download"
    download_url = f"{base_url}/{version}/{binary_name}"

    target_path = os.path.join(target_dir, "dify" if os_name != 'windows' else "dify.exe")

    print(f"Downloading Dify CLI v{version} for {os_name}-{arch}...")
    print(f"URL: {download_url}")

    try:
        def show_progress(block_num, block_size, total_size):
            downloaded = block_num * block_size
            percent = min(100, downloaded * 100 / total_size) if total_size > 0 else 0
            print(f"\rProgress: {percent:.1f}%", end='')

        urllib.request.urlretrieve(download_url, target_path, show_progress)
        print()

        return target_path

    except Exception as e:
        raise Exception(f"Download failed: {str(e)}")


def make_executable(file_path: str):
    """Make the binary executable."""
    if platform.system() != 'Windows':
        current_permissions = os.stat(file_path).st_mode
        os.chmod(file_path, current_permissions | stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)
        print(f"Made executable: {file_path}")


def verify_installation(binary_path: str) -> bool:
    """Verify CLI installation."""
    import subprocess

    print("\nVerifying installation...")

    try:
        result = subprocess.run(
            [binary_path, "version"],
            capture_output=True,
            text=True,
            timeout=5
        )

        if result.returncode == 0:
            version = result.stdout.strip()
            print(f"SUCCESS: Dify CLI installed!")
            print(f"Version: {version}")
            return True
        else:
            print(f"Verification failed: {result.stderr}")
            return False

    except Exception as e:
        print(f"Verification failed: {str(e)}")
        return False


def add_to_path_instructions(binary_path: str):
    """Print PATH instructions."""
    abs_path = os.path.abspath(binary_path)
    dir_path = os.path.dirname(abs_path)

    print(f"\nTo use 'dify' from anywhere, add to PATH:")

    if platform.system() == 'Windows':
        print(f"Add to PATH: {dir_path}")
    else:
        shell = os.environ.get('SHELL', '/bin/bash')
        rc_file = '~/.zshrc' if 'zsh' in shell else '~/.bashrc'

        print(f"\nAdd to {rc_file}:")
        print(f'export PATH="$PATH:{dir_path}"')
        print(f"\nThen: source {rc_file}")


def main():
    """Main installation function."""
    import argparse

    parser = argparse.ArgumentParser(description='Install Dify Plugin CLI')
    parser.add_argument('--version', help='Specific version to install (default: latest)')
    parser.add_argument('--path', default='.', help='Installation directory (default: current)')

    args = parser.parse_args()

    print("="*70)
    print("DIFY CLI INSTALLER")
    print("="*70)

    try:
        print("\nDetecting platform...")
        os_name, arch = detect_platform()
        print(f"Platform: {os_name}-{arch}")

        if args.version:
            version = args.version.lstrip('v')
        else:
            version = get_latest_release_version()
        print(f"Version: {version}\n")

        target_dir = os.path.expanduser(args.path)
        os.makedirs(target_dir, exist_ok=True)

        binary_path = download_cli(version, os_name, arch, target_dir)
        print(f"Downloaded to: {binary_path}\n")

        make_executable(binary_path)

        if verify_installation(binary_path):
            add_to_path_instructions(binary_path)

            print("\n" + "="*70)
            print("INSTALLATION COMPLETE!")
            print("="*70)
            print(f"Binary: {os.path.abspath(binary_path)}")
            print(f"Run: {binary_path} --help")

            return 0
        else:
            print("\nInstallation completed but verification failed.")
            return 1

    except Exception as e:
        print(f"\nInstallation failed: {str(e)}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
