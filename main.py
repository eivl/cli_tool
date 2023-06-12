from typing import Optional

import typer

from movie import movie_search

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


@app.command()
def movie_rating(movie_name: str):
    """Get the rating for a movie."""
    movie = movie_search(movie_name)
    typer.echo(f"Rating for {movie_name.title()} {movie['vote_average']}")


if __name__ == "__main__":
    app()

