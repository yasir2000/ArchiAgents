"""
Utility functions for formatting CLI output
"""
import json
from typing import Any, Dict, List, Optional
from datetime import datetime
import yaml


class OutputFormatter:
    """Format output for different CLI output modes"""
    
    @staticmethod
    def format_table(headers: List[str], rows: List[List[Any]], title: Optional[str] = None) -> str:
        """Format data as ASCII table"""
        if not rows:
            return "No data to display"
        
        # Calculate column widths
        col_widths = [len(h) for h in headers]
        for row in rows:
            for i, cell in enumerate(row):
                col_widths[i] = max(col_widths[i], len(str(cell)))
        
        # Create separator
        separator = "+" + "+".join("-" * (w + 2) for w in col_widths) + "+"
        
        # Build table
        lines = []
        if title:
            lines.append(f"\n{title}")
            lines.append("=" * len(title))
        
        lines.append(separator)
        
        # Header
        header_row = "|" + "|".join(f" {headers[i]:<{col_widths[i]}} " for i in range(len(headers))) + "|"
        lines.append(header_row)
        lines.append(separator)
        
        # Rows
        for row in rows:
            data_row = "|" + "|".join(f" {str(row[i]):<{col_widths[i]}} " for i in range(len(row))) + "|"
            lines.append(data_row)
        
        lines.append(separator)
        
        return "\n".join(lines)
    
    @staticmethod
    def format_json(data: Any, pretty: bool = True) -> str:
        """Format data as JSON"""
        if pretty:
            return json.dumps(data, indent=2, default=str)
        return json.dumps(data, default=str)
    
    @staticmethod
    def format_yaml(data: Any) -> str:
        """Format data as YAML"""
        return yaml.dump(data, default_flow_style=False, sort_keys=False)
    
    @staticmethod
    def format_tree(data: Dict[str, Any], indent: int = 0, prefix: str = "") -> str:
        """Format data as tree structure"""
        lines = []
        items = list(data.items())
        
        for i, (key, value) in enumerate(items):
            is_last = i == len(items) - 1
            current_prefix = "└── " if is_last else "├── "
            
            if isinstance(value, dict):
                lines.append(f"{prefix}{current_prefix}{key}")
                next_prefix = prefix + ("    " if is_last else "│   ")
                lines.append(OutputFormatter.format_tree(value, indent + 1, next_prefix))
            elif isinstance(value, list):
                lines.append(f"{prefix}{current_prefix}{key} ({len(value)} items)")
                next_prefix = prefix + ("    " if is_last else "│   ")
                for j, item in enumerate(value):
                    item_last = j == len(value) - 1
                    item_prefix = "└── " if item_last else "├── "
                    if isinstance(item, dict):
                        lines.append(f"{next_prefix}{item_prefix}{item.get('name', f'Item {j+1}')}")
                    else:
                        lines.append(f"{next_prefix}{item_prefix}{item}")
            else:
                lines.append(f"{prefix}{current_prefix}{key}: {value}")
        
        return "\n".join(lines)
    
    @staticmethod
    def format_list(items: List[str], bullet: str = "•") -> str:
        """Format data as bullet list"""
        return "\n".join(f"{bullet} {item}" for item in items)
    
    @staticmethod
    def format_status(status: str, message: str) -> str:
        """Format status message with color indicators"""
        indicators = {
            "success": "✅",
            "error": "❌",
            "warning": "⚠️",
            "info": "ℹ️",
            "running": "🔄",
            "pending": "⏳"
        }
        
        indicator = indicators.get(status.lower(), "•")
        return f"{indicator} {message}"
    
    @staticmethod
    def format_progress(current: int, total: int, width: int = 40) -> str:
        """Format progress bar"""
        if total == 0:
            percent = 0
        else:
            percent = int((current / total) * 100)
        
        filled = int((current / total) * width) if total > 0 else 0
        bar = "█" * filled + "░" * (width - filled)
        
        return f"[{bar}] {percent}% ({current}/{total})"
    
    @staticmethod
    def format_timestamp(dt: Optional[datetime] = None) -> str:
        """Format timestamp"""
        if dt is None:
            dt = datetime.now()
        return dt.strftime("%Y-%m-%d %H:%M:%S")
    
    @staticmethod
    def format_duration(seconds: float) -> str:
        """Format duration in human-readable format"""
        if seconds < 60:
            return f"{seconds:.1f}s"
        elif seconds < 3600:
            minutes = seconds / 60
            return f"{minutes:.1f}m"
        else:
            hours = seconds / 3600
            return f"{hours:.1f}h"
    
    @staticmethod
    def format_size(bytes: int) -> str:
        """Format file size in human-readable format"""
        for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
            if bytes < 1024.0:
                return f"{bytes:.1f}{unit}"
            bytes /= 1024.0
        return f"{bytes:.1f}PB"


class ConsoleColors:
    """ANSI color codes for console output"""
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'
    
    @staticmethod
    def colorize(text: str, color: str) -> str:
        """Add color to text"""
        color_code = getattr(ConsoleColors, color.upper(), '')
        return f"{color_code}{text}{ConsoleColors.END}"
    
    @staticmethod
    def success(text: str) -> str:
        """Format success message"""
        return ConsoleColors.colorize(text, 'green')
    
    @staticmethod
    def error(text: str) -> str:
        """Format error message"""
        return ConsoleColors.colorize(text, 'red')
    
    @staticmethod
    def warning(text: str) -> str:
        """Format warning message"""
        return ConsoleColors.colorize(text, 'yellow')
    
    @staticmethod
    def info(text: str) -> str:
        """Format info message"""
        return ConsoleColors.colorize(text, 'cyan')
    
    @staticmethod
    def header(text: str) -> str:
        """Format header"""
        return ConsoleColors.colorize(text, 'header')


def format_output(data: Any, format_type: str = "table", **kwargs) -> str:
    """
    Format data based on specified format type
    
    Args:
        data: Data to format
        format_type: Output format (table, json, yaml, tree, list)
        **kwargs: Additional formatting options
    
    Returns:
        Formatted string
    """
    formatter = OutputFormatter()
    
    if format_type == "json":
        return formatter.format_json(data, kwargs.get("pretty", True))
    elif format_type == "yaml":
        return formatter.format_yaml(data)
    elif format_type == "tree":
        if isinstance(data, dict):
            return formatter.format_tree(data)
        return str(data)
    elif format_type == "list":
        if isinstance(data, list):
            return formatter.format_list(data, kwargs.get("bullet", "•"))
        return str(data)
    elif format_type == "table":
        if isinstance(data, dict) and "headers" in data and "rows" in data:
            return formatter.format_table(
                data["headers"],
                data["rows"],
                data.get("title")
            )
        return str(data)
    else:
        return str(data)
