import typer

from app.core.errors import ValidationError
from app.services.meeting_service import create_meeting, list_meetings

app = typer.Typer()


@app.command("create-meeting")
def create_meeting_cmd(
    title: str = typer.Option(..., "--title"),
    date: str = typer.Option(..., "--date"),
    owner: str = typer.Option(..., "--owner"),
) -> None:
    try:
        meeting = create_meeting(title=title, date=date, owner=owner)
    except ValidationError as exc:
        typer.echo(f"Validation error: {exc}")
        raise typer.Exit(code=2)

    typer.echo(f"Created: {meeting.id}")


@app.command("list-meetings")
def list_meetings_cmd() -> None:
    items = list_meetings()
    if not items:
        typer.echo("No meetings found.")
        raise typer.Exit()

    for m in items:
        typer.echo(f"{m.id} | {m.date} | {m.title} | owner={m.owner}")


if __name__ == "__main__":
    app()
