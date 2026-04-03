import typer

from app.core.errors import ValidationError, NotFoundError
from app.services.meeting_service import (
    create_meeting,
    list_meetings,
    get_meeting,
    delete_meeting,
)
from app.services.report_service import summary

app = typer.Typer()


@app.command("create-meeting")
def create_meeting_cmd(
    title: str = typer.Option(...),
    date: str = typer.Option(...),
    owner: str = typer.Option(...),
) -> None:
    try:
        meeting = create_meeting(title, date, owner)
        typer.echo(f"Created: {meeting.id}")
    except ValidationError as exc:
        typer.echo(f"Validation error: {exc}")
        raise typer.Exit(code=2)


@app.command("list-meetings")
def list_meetings_cmd() -> None:
    items = list_meetings()
    if not items:
        typer.echo("No meetings found.")
        raise typer.Exit()

    for m in items:
        typer.echo(f"{m.id} | {m.date} | {m.title}")


@app.command("show-meeting")
def show_meeting_cmd(id: str = typer.Option(...)) -> None:
    try:
        m = get_meeting(id)
    except NotFoundError as exc:
        typer.echo(str(exc))
        raise typer.Exit(code=1)

    typer.echo(f"ID: {m.id}")
    typer.echo(f"Title: {m.title}")
    typer.echo(f"Date: {m.date}")
    typer.echo(f"Owner: {m.owner}")
    typer.echo(f"Participants: {m.participants}")
    typer.echo(f"Action Items: {len(m.action_items)}")


@app.command("delete-meeting")
def delete_meeting_cmd(id: str = typer.Option(...)) -> None:
    try:
        delete_meeting(id)
        typer.echo(f"Deleted: {id}")
    except NotFoundError as exc:
        typer.echo(str(exc))
        raise typer.Exit(code=1)


@app.command("summary")
def summary_cmd() -> None:
    data = list_meetings()
    report = summary(data)
    typer.echo(report)

if __name__ == "__main__":
    app()
