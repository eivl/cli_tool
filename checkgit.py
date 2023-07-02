import subprocess
import typer

def check_git():
    typer.echo('Checking if Git is installed...')
    result = subprocess.run(['git', '-v'], capture_output=False, text=True, shell=True)
    if result.returncode == 0:
        return True
    else:
        return False 

if check_git():
    print("Git is installed.")    
else:
    print("Git is not installed.")
   
def check_command(command):
    result = subprocess.run(command, shell=True)
    if result.returncode == 0:
        return True
    else:
        return False 

print(check_command('git -v'))

