import subprocess

def create_venv():
    venv_name = input("Enter the name of the virtual environment (default: .venv): ") or ".venv"
    subprocess.run(["python3", "-m", "venv", venv_name])
    print(f"Virtual environment '{venv_name}' created. Activate it with: source {venv_name}/bin/activate")

create_venv()