import typer

def main():
    ending = typer.style("Olá", fg=typer.colors.GREEN, bold=True)
    message = ending
    typer.echo(message)
 


if __name__ == "__main__":
    typer.run(main)
    
