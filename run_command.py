import os
import subprocess
import sys

def run_command(cmd, run_system=False):
    try:
        if run_system:
            os.system(cmd)
        else:
            pieces_cmd = [ p for p in cmd.split(" ") if p != "" ]
            r = subprocess.run(pieces_cmd)
            if r.returncode != 0:
                print("Failed to run command:", cmd)
                sys.exit(1)
    except Exception as e:
        print(f"Failed to run command: {e}")
        sys.exit(1)
