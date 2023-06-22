from typing import Optional

import typer

import movie

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
    my_movie = movie.movie_search(movie_name)
    typer.echo(f"Rating for {movie_name.title()} {my_movie['vote_average']}")


@app.command()
def movie_details(movie_name: str):
    """Skal gi en detaljert beskrivelse av en film."""
    film = movie.movie_search(movie_name)
    detail = movie.movie_details(film)
    typer.echo(detail)
    

if __name__ == "__main__":
    app()
