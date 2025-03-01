import sys
import subprocess
from next_state import get_next_state

def run_command(cmd):
    try:
        r = subprocess.run(cmd)
        if r.returncode != 0:
            print("Failed to run command:", cmd)
            sys.exit(1)
    except Exception as e:
        print(f"Failed to run command: {e}")
        sys.exit(1)

def main(util_name, get_list_sates, format_cmd_set_state):
    states = get_list_sates()

    if len(states) == 1:
        sys.exit(0)

    next_state = get_next_state(util_name, states, 0)

    # in case to format needs all states
    cmd = format_cmd_set_state(next_state)

    run_command(cmd)
