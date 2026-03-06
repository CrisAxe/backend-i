import typer
from logic import get_solution, create_problem

app = typer.Typer()

@app.command()
def menu():
    """Interactive menu to choose a computer problem."""

    typer.echo("=== Computer Troubleshooting Menu ===")
    typer.echo("1. Network")
    typer.echo("2. Freeze")
    typer.echo("3. Heating")
    typer.echo("4. Bluescreen")
    typer.echo("5. OS Slow")

    choice = typer.prompt("Select a problem by number", type=int)

    match choice:
        case 1:
            problem = "network"
        case 2:
            problem = "freeze"
        case 3:
            problem = "heating"
        case 4:
            problem = "bluescreen"
        case 5:
            problem = "osslow"
        case _:
            typer.secho("Invalid choice. Exiting.", fg=typer.colors.RED)
            raise typer.Exit(code=1)

    solution = get_solution(problem)

    typer.echo(f"\nProblem: {problem}")
    typer.echo(f"Solution: {solution}")

@app.command()
def create(
    network:bool = False,
    freeze: bool = False,
    heating: bool = False,
    bluescreen: bool = False,
    osslow: bool = False
):
    """Create a problem report."""

    problem = create_problem(network, freeze, heating, bluescreen, osslow)

    typer.echo("Problem Report Created:")
    typer.echo(problem)


if __name__ == "__main__":
    app()

