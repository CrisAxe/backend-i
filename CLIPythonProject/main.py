import typer
from src.data import Problem
cli=typer.Typer()

@cli.command()
def create(
    network:str,
    freeze:str,
    heating:str,
    bluescreen:str,
    osslow:str



)->None:
    Problem.create(network,freeze,heating,bluescreen,osslow)

if __name__ == "__main__":
    cli()
