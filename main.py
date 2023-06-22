import os
import subprocess
import sys
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
    typer.echo(f"Rating for {movie_name.title()} {my_movie['vote_average']:.2f}")


@app.command()
def movie_details(movie_name: str):
    """Skal gi en detaljert beskrivelse av en film."""
    film = movie.movie_search(movie_name)
    detail = movie.movie_details(film)
    typer.echo(detail)


def check_powershell():
    my_path = os.getenv('PSModulePath')
    my_split_path = my_path.split(os.pathsep)
    if len(my_split_path) >= 3:
        return True
    else:
        return False


def install_powershell():
    typer.echo('Installing powershell')
    result = subprocess.run(
        'winget install --id=Microsoft.PowerShell -e',
        shell=True,
        capture_output=True,
    )
    winget_result = result.stdout.decode()

    if 'package already installed' in winget_result:
        typer.echo('Powershell already installed, please use it instead.')
        return True
    elif 'Successfully installed' in winget_result:
        typer.echo('Powershell installed, restart into powershell to use it.')
        return True
    elif not winget_result:
        typer.echo('Winget error, PowerShell not installed')
        return False
    else:
        return False


if __name__ == "__main__":
    if check_powershell():
        app()
    else:
        typer.echo("You are not running this in powershell")
        pws_result = install_powershell()
        if not pws_result:
            typer.echo('https://github.com/microsoft/winget-cli/releases')
