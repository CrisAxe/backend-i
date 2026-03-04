import typer
from src.logic import get_solution

app = typer.Typer()

@app.command()
def solve(problem: str):
    """Diagnostica e sugere soluções para problemas comuns."""
    solution = get_solution(problem)
    typer.echo(f"Problema: {problem}")
    typer.echo(f"Solução: {solution}")

if __name__ == "__main__":
    app()
