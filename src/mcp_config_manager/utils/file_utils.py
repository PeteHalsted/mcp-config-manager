"""
File and path utilities
"""

from pathlib import Path
import os


def get_claude_config_path() -> Path:
    """Get the Claude configuration file path."""
    return Path.home() / '.claude.json'


def get_gemini_config_path() -> Path:
    """Get the Gemini configuration file path."""
    return Path.home() / '.gemini' / 'settings.json'


def get_presets_path() -> Path:
    """Get the MCP presets file path."""
    return Path.home() / '.mcp_presets.json'


def get_disabled_servers_path() -> Path:
    """Get the disabled servers storage path."""
    # Store disabled servers in the user's home directory for consistency
    # This ensures it works both in development and when bundled as an app
    return Path.home() / '.mcp_disabled_servers.json'


def get_project_backups_dir() -> Path:
    """Get the project backups directory path.

    Returns a user-specific directory that persists across app updates.
    Uses ~/Documents/MCP Config Manager/backups/ for better accessibility.
    """
    # Use Documents folder for better user accessibility
    backups_dir = Path.home() / 'Documents' / 'MCP Config Manager' / 'backups'
    return backups_dir


def ensure_gemini_config_exists() -> None:
    """Ensure Gemini config directory and file exist."""
    gemini_path = get_gemini_config_path()
    gemini_dir = gemini_path.parent
    
    if not gemini_dir.exists():
        gemini_dir.mkdir(parents=True, exist_ok=True)
        print(f"📁 Created Gemini config directory: {gemini_dir}")
    
    if not gemini_path.exists():
        default_config = {"mcpServers": {}}
        with open(gemini_path, 'w') as f:
            import json
            json.dump(default_config, f, indent=2)
        print(f"📝 Created Gemini config file: {gemini_path}")


def ensure_config_directories() -> None:
    """Ensure all required configuration directories exist."""
    ensure_gemini_config_exists()
    
    # Ensure presets file parent directory exists
    presets_path = get_presets_path()
    presets_path.parent.mkdir(parents=True, exist_ok=True)
    
    # Ensure disabled servers directory exists
    disabled_path = get_disabled_servers_path()
    disabled_path.parent.mkdir(parents=True, exist_ok=True)
    
    # Ensure backups directory exists
    backups_dir = get_project_backups_dir()
    backups_dir.mkdir(parents=True, exist_ok=True)
