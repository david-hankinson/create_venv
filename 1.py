import subprocess
import os

def create_venv():
    subprocess.run(["python3", "-m", "venv", ".venv"])
    activate = input("Do you want to activate the venv? (Y/n): ") or "Y"
    if activate.lower() == "y":
        os.system("/bin/bash --rcfile .venv/bin/activate")

create_venv()