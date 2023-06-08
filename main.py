from typing import Optional

import typer


app = typer.Typer()


@app.command()
def hello(name: Optional[str] = None):
    """Say hello to NAME, or hello world if NAME is not given."""
    if name:
        typer.echo(f"Hello {name}.")
    else:
        typer.echo(f"Hello World.")


@app.command()
def bye():
    typer.echo("Bye bye!")



if __name__ == "__main__":
    app()

