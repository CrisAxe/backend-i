import typer
from datetime import datetime
from typing import Annotated


app = typer.Typer()

@app.command()
def create_meeting(title: str, date: str, owner: str) -> None:
    typer.echo(f"Hello from Typer!!!")

@app.command()
def main(
    launch_date: Annotated[
        datetime,
        typer.Argument(
            formats=["%Y-%m-%d", "%Y-%m-%dT%H:%M:%S", "%Y-%m-%d %H:%M:%S", "%m/%d/%Y"]
        ),
    ],
):
    print(f"Launch will be at: {launch_date}")

if __name__ == "__main__":
    app()