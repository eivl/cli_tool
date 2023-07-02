import subprocess
import typer

def check_git():
    typer.echo('Checking if Git is installed...')
    result = subprocess.run(['git', '-v'], capture_output=False, text=True, shell=True)
    if result.returncode == 0:
        return True
    else:
        return False 


def check_command(command):
    result = subprocess.run(command, shell=True)
    if result.returncode == 0:
        return True
    else:
        return False 
