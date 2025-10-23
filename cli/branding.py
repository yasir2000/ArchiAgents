"""
ArchiAgents CLI Branding Module
Provides branded welcome messages, ASCII art, and styled output for the CLI
"""

from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.table import Table
from rich import box

console = Console()

# Brand colors (using Rich's color names closest to our brand)
BRAND_PRIMARY = "cyan"
BRAND_SECONDARY = "blue"
BRAND_SUCCESS = "green"
BRAND_WARNING = "yellow"
BRAND_ERROR = "red"
BRAND_AI = "magenta"

ASCII_LOGO = """
╔═══════════════════════════════════════════════════════════════════╗
║                                                                   ║
║     █████╗ ██████╗  ██████╗██╗  ██╗██╗                           ║
║    ██╔══██╗██╔══██╗██╔════╝██║  ██║██║                           ║
║    ███████║██████╔╝██║     ███████║██║                           ║
║    ██╔══██║██╔══██╗██║     ██╔══██║██║                           ║
║    ██║  ██║██║  ██║╚██████╗██║  ██║██║                           ║
║    ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚═╝                           ║
║                                                                   ║
║         █████╗  ██████╗ ███████╗███╗   ██╗████████╗███████╗      ║
║        ██╔══██╗██╔════╝ ██╔════╝████╗  ██║╚══██╔══╝██╔════╝      ║
║        ███████║██║  ███╗█████╗  ██╔██╗ ██║   ██║   ███████╗      ║
║        ██╔══██║██║   ██║██╔══╝  ██║╚██╗██║   ██║   ╚════██║      ║
║        ██║  ██║╚██████╔╝███████╗██║ ╚████║   ██║   ███████║      ║
║        ╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚═╝  ╚═══╝   ╚═╝   ╚══════╝      ║
║                                                                   ║
║              Enterprise Architecture Platform                    ║
║                  Powered by AI • TOGAF 10 • ArchiMate 3.2        ║
║                                                                   ║
╚═══════════════════════════════════════════════════════════════════╝
"""

ICON_LOGO = """
    ╔══╗ ╔══╗  🧠
    ║██║ ║██║  │
    ╚══╝ ╠══╣  ├─ AI
    ╔══╗ ║██║  │
    ║██║ ╚══╝  ●
    ╚══╝
"""


def print_welcome():
    """Display the branded welcome message"""
    console.print(ASCII_LOGO, style=f"bold {BRAND_PRIMARY}")
    
    welcome_text = Text()
    welcome_text.append("Welcome to ", style="white")
    welcome_text.append("ArchiAgents", style=f"bold {BRAND_PRIMARY}")
    welcome_text.append(" - Transform your enterprise architecture with ", style="white")
    welcome_text.append("AI-powered automation", style=f"bold {BRAND_AI}")
    
    console.print(Panel(
        welcome_text,
        border_style=BRAND_PRIMARY,
        box=box.ROUNDED,
        padding=(1, 2)
    ))
    console.print()


def print_version_info(version: str = "1.0.0"):
    """Display version and framework information"""
    table = Table(show_header=False, box=None, padding=(0, 2))
    table.add_column(style=f"bold {BRAND_SECONDARY}")
    table.add_column(style="white")
    
    table.add_row("Version", version)
    table.add_row("Framework", "TOGAF 10 ADM")
    table.add_row("Modeling", "ArchiMate 3.2")
    table.add_row("AI Engine", "Multi-Provider (OpenAI, Claude, Gemini, Ollama)")
    table.add_row("Compliance", "Saudi NORA, ISO 27001, SOC 2")
    
    console.print(Panel(
        table,
        title="[bold cyan]Platform Information[/bold cyan]",
        border_style=BRAND_SECONDARY,
        box=box.ROUNDED
    ))
    console.print()


def print_quick_start():
    """Display quick start commands"""
    commands = [
        ("archi project init", "Initialize a new architecture project"),
        ("archi ai configure", "Configure AI provider (OpenAI, Claude, Ollama, etc.)"),
        ("archi model generate", "Generate ArchiMate/BPMN/UML models"),
        ("archi phase run", "Execute TOGAF ADM phases"),
        ("archi --help", "View all available commands"),
    ]
    
    table = Table(box=box.SIMPLE, padding=(0, 2), show_header=False)
    table.add_column(style=f"bold {BRAND_PRIMARY}")
    table.add_column(style="white")
    
    for cmd, desc in commands:
        table.add_row(cmd, desc)
    
    console.print(Panel(
        table,
        title="[bold green]🚀 Quick Start Commands[/bold green]",
        border_style=BRAND_SUCCESS,
        box=box.ROUNDED
    ))
    console.print()


def print_feature_highlights():
    """Display key features"""
    features = Text()
    features.append("✨ ", style="yellow")
    features.append("AI-Powered Automation", style=f"bold {BRAND_AI}")
    features.append(" - 20+ specialized AI agents\n", style="white")
    
    features.append("🏗️  ", style="blue")
    features.append("TOGAF 10 ADM", style=f"bold {BRAND_PRIMARY}")
    features.append(" - Complete 8-phase implementation\n", style="white")
    
    features.append("🎯 ", style="cyan")
    features.append("ArchiMate 3.2", style=f"bold {BRAND_PRIMARY}")
    features.append(" - 21 model types, 6 export formats\n", style="white")
    
    features.append("🌐 ", style="green")
    features.append("Web Platform", style=f"bold {BRAND_SUCCESS}")
    features.append(" - Visual modeling, real-time collaboration\n", style="white")
    
    features.append("🇸🇦 ", style="magenta")
    features.append("NORA Compliance", style=f"bold {BRAND_AI}")
    features.append(" - Saudi Digital Government standards", style="white")
    
    console.print(Panel(
        features,
        title="[bold yellow]Key Features[/bold yellow]",
        border_style=BRAND_WARNING,
        box=box.ROUNDED
    ))
    console.print()


def print_success(message: str):
    """Print a success message"""
    console.print(f"✓ {message}", style=f"bold {BRAND_SUCCESS}")


def print_error(message: str):
    """Print an error message"""
    console.print(f"✗ {message}", style=f"bold {BRAND_ERROR}")


def print_warning(message: str):
    """Print a warning message"""
    console.print(f"⚠ {message}", style=f"bold {BRAND_WARNING}")


def print_info(message: str):
    """Print an info message"""
    console.print(f"→ {message}", style=f"{BRAND_PRIMARY}")


def print_ai_message(message: str):
    """Print an AI-related message"""
    console.print(f"🤖 {message}", style=f"bold {BRAND_AI}")


def print_progress(message: str):
    """Print a progress message"""
    console.print(f"⏳ {message}", style=f"{BRAND_PRIMARY}")


def print_complete():
    """Print completion message"""
    console.print()
    console.print("=" * 70, style=BRAND_SUCCESS)
    console.print("Operation completed successfully! ✓", style=f"bold {BRAND_SUCCESS}", justify="center")
    console.print("=" * 70, style=BRAND_SUCCESS)
    console.print()


def print_separator():
    """Print a visual separator"""
    console.print("─" * 70, style=BRAND_PRIMARY)


if __name__ == "__main__":
    # Demo the branding
    print_welcome()
    print_version_info()
    print_feature_highlights()
    print_quick_start()
    
    console.print()
    print_info("For more information, visit: https://github.com/yasir2000/ArchiAgents")
    print_ai_message("Ready to transform your enterprise architecture!")
