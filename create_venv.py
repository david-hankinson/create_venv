import subprocess
import pdb

def create_venv():
    print(locals())
    subprocess.run(["python3", "-m", "venv", ".venv"])

    print("Virtual environment created. Activate it with: source .venv/bin/activate")

create_venv()