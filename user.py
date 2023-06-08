import typer


app = typer.Typer(help='Awsome CLI user management tool.')


@app.command()
def create(username: str):
    """
    Create a new user with USERNAME.
    """
    typer.echo(f'Creating user: {username}')


@app.command()
def delete(username: str,
           force: bool = typer.Option(
               ...,
               prompt='Are you sure you want to delete the user?',
               help='Fore deletion without confirmation.',
           ),
           ):
    """
    Delete a user with USERNAME.

    If --force is not used, will ask for confirmation.
    """

    if force:
        typer.echo(f'Deleting user: {username}')
    else:
        typer.echo('Deletion canceled')


@app.command()
def delete_all(
        force: bool = typer.Option(
            ...,
            prompt='Are you sure you want to delete ALL users?',
            help='Fore deletion without confirmation.',
        ),
    ):
    """
    Delete ALL user with USERNAME.

    If --force is not used, will ask for confirmation.
    """

    if force:
        typer.echo('Deleting ALL users:')
    else:
        typer.echo('Deletion canceled')


@app.command()
def init():
    """
    Initialize the user database.
    """
    typer.echo('Initializing user database')


if __name__ == '__main__':
    app()
