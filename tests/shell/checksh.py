import subprocess

def check_shell():
    result = subprocess.run("echo $SHELL", shell=True, capture_output=True, text=True)
    shell_path = result.stdout.strip()
    return shell_path


