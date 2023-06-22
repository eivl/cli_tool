import os
import subprocess

import typer


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


def check_command(command: str):
    result = subprocess.run(
        f'pwsh -Command "Get-Command -ErrorAction SilentlyContinue {command}"',
        shell=True,
        capture_output=True,
    )
    if result.returncode == 0:
        return True
    else:
        return False
