#!/usr/bin/env python
"""
ArchiAgents CLI entry point

This script provides the main entry point for the ArchiAgents command-line interface.
"""
import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from cli.main import cli

if __name__ == '__main__':
    cli()
