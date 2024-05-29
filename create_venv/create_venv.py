import subprocess
import pyperclip

def create_venv():
    venv_name = input("Enter the name of the virtual environment (default: .venv): ") or ".venv"
    subprocess.run(["python3", "-m", "venv", venv_name])
    print(f"Virtual environment '{venv_name}' created. Activate it with: source {venv_name}/bin/activate")

    copy_to_clipboard = input("Copy 'source {venv_name}/bin/activate' command to clipboard? (default: yes) [yes/no]: ").lower() or "yes"
    if copy_to_clipboard == "yes":
        pyperclip.copy(f"source {venv_name}/bin/activate")
        print("Command copied to clipboard.")