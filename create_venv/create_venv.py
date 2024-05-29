import subprocess
import pyperclip
import sys
import os

def create_venv():
    venv_dir = ".venv"
    if os.path.exists(venv_dir):
        print("A virtual environment is currently present.")
        print("Please remove the existing virtual environment before creating a new one.")
        remove_venv = input("Remove existing venv using this program? (default: yes) [yes/no]: ").lower() or "yes"
        if remove_venv == "yes":
            subprocess.run(["rm", "-rf", venv_dir])
            print("Existing virtual environment removed.")
        else:
            print("Please remove the existing virtual environment before creating a new one.")
        print('Exiting create_venv...')
    else:
        print("No virtual environment is currently present")


    venv_name = input("Enter the name of the virtual environment (default: .venv): ") or ".venv"
    subprocess.run(["python3", "-m", "venv", venv_name])
    print(f"Virtual environment '{venv_name}' created. Activate it with: source {venv_name}/bin/activate")
    copy_to_clipboard = input("Copy 'source {venv_name}/bin/activate' command to clipboard? (default: yes) [yes/no]: ").lower() or "yes"
    if copy_to_clipboard == "yes":
        pyperclip.copy(f"source {venv_name}/bin/activate")
        print("Command copied to clipboard.")
        print('Exiting create_venv...')
    else : 
        print("Command not copied to the clipboard.")
        print('Exiting create_venv...')