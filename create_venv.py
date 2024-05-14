import subprocess
import pdb

def create_venv():
    print(locals())
    subprocess.run(["python3", "-m", "venv", ".venv"])
    activate = input("Do you want to activate the venv? (Y/n): ") or "Y"
    if activate.lower() == "y":
        print(locals())
        shell = subprocess.Popen("/bin/bash", stdin=subprocess.PIPE)
        shell.communicate("source .venv/bin/activate\n".encode())
        print(locals())

create_venv()