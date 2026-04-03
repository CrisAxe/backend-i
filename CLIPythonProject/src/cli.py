from utils import log_problem  # NEW: logging utility
import typer
from logic import get_solution, create_problem
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.progress import track
import psutil
import socket
import time

app = typer.Typer()
console = Console()


@app.command()
def menu():
    """Interactive menu to choose a computer problem."""
    while True:
        console.print("[bold cyan]=== Computer Troubleshooting Menu ===[/bold cyan]")
        console.print("1. Network")
        console.print("2. Freeze")
        console.print("3. Heating")
        console.print("4. Bluescreen")
        console.print("5. OS Slow")
        console.print("0. Exit")

        choice = typer.prompt("Select a problem")

        match choice:
            case "1":
                problem = "network"
            case "2":
                problem = "freeze"
            case "3":
                problem = "heating"
            case "4":
                problem = "bluescreen"
            case "5":
                problem = "osslow"
            case "0":
                console.print("[green]Exiting program...[/green]")
                break
            case _:
                console.print("[red]Invalid choice. Try again.[/red]")
                continue

        steps = get_solution(problem)
        console.print(Panel(f"Problem: [yellow]{problem}[/yellow]", title="🖥️ Selected Problem"))

        table = Table(title="🔧 Troubleshooting Steps")
        table.add_column("Step", justify="center", style="cyan", no_wrap=True)
        table.add_column("Action", style="magenta")

        for i, step in enumerate(steps, start=1):
            table.add_row(str(i), step)

        console.print(table)

        log_problem(f"{problem} selected from menu")


@app.command()
def create(
    network: bool = False,
    freeze: bool = False,
    heating: bool = False,
    bluescreen: bool = False,
    osslow: bool = False
):
    """Create a problem report."""
    problem = create_problem(network, freeze, heating, bluescreen, osslow)
    console.print(Panel(str(problem), title="📝 Problem Report"))


    log_problem(f"Custom problem created: {problem}")


def check_internet() -> bool:
    """Return True if internet connection is available."""
    try:
        socket.create_connection(("8.8.8.8", 53), timeout=2)
        return True
    except OSError:
        return False


@app.command()
def wizard():
    """Guided troubleshooting wizard with real system checks."""
    console.print("[bold green]🧙 System Troubleshooting Wizard[/bold green]\n")

    network_issue = not check_internet()
    cpu_percent = psutil.cpu_percent(interval=1)
    ram_percent = psutil.virtual_memory().percent
    disk_percent = psutil.disk_usage("/").percent
    heating_issue = cpu_percent > 80 or ram_percent > 90
    osslow_issue = ram_percent > 70 or disk_percent > 90

    freeze_issue = typer.confirm("Does your computer freeze frequently?")
    bluescreen_issue = typer.confirm("Do you see a blue screen error?")

    problem = create_problem(network_issue, freeze_issue, heating_issue, bluescreen_issue, osslow_issue)
    console.print(Panel(str(problem), title="📋 Detected Problems"))

    for p_name, has_issue in problem.__dict__.items():
        if has_issue:
            log_problem(f"{p_name} detected")
    log_problem(f"System metrics -> CPU: {cpu_percent}%, RAM: {ram_percent}%, Disk: {disk_percent}%, Internet: {'OK' if not network_issue else 'No Connection'}")

    console.print("\n🔧 Recommended Solutions:")
    for p_name, has_issue in problem.__dict__.items():
        if has_issue:
            steps = get_solution(p_name)
            console.print(f"\n[bold yellow]Problem: {p_name}[/bold yellow]")

            for step in track(steps, description=f"Analyzing {p_name}..."):
                time.sleep(0.5)
                console.print(f"• {step}")

    console.print("\n📊 System Metrics:")
    table = Table(title="System Status")
    table.add_column("Metric", style="cyan")
    table.add_column("Value", style="magenta")
    table.add_row("CPU Usage", f"{cpu_percent}%")
    table.add_row("RAM Usage", f"{ram_percent}%")
    table.add_row("Disk Usage", f"{disk_percent}%")
    table.add_row("Internet Connection", "OK" if not network_issue else "No Connection")
    console.print(table)


@app.command()
def history():
    """View the history of detected problems."""
    console.print("[bold blue]📜 Problem History[/bold blue]\n")

    try:
        with open("problem_history.txt", "r") as f:
            lines = f.readlines()
            if not lines:
                console.print("[green]No history found.[/green]")
                return

            for line in lines[-20:]: 
                console.print(line.strip())
    except FileNotFoundError:
        console.print("[red]No history file found.[/red]")


@app.command()
def clear_history():
    """Clear all logged problem history."""
    with open("problem_history.txt", "w") as f:
        pass
    console.print("[green]History cleared![/green]")


if __name__ == "__main__":
    app()