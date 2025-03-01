import sys
import subprocess

# TODO add an argument that is random, so for example a list of wallpapers
def get_next_state(util_name, states, default_index=0):
    current_filepath = f"/tmp/{util_name}"
    try:
        with open(current_filepath) as f:
            current_state = f.read()
    except FileNotFoundError:
        current_state = states[default_index]

    if current_state == "":
        current_satue = states[default_index]

    next_state = ""
    if current_state == states[-1]:
        next_state = states[0]
    else:
        for i, l in enumerate(states):
            if l == current_state:
                next_state = states[i+1]

    if next_state == "":
        next_state = states[default_index]

    with open(current_filepath, "w") as f:
        f.write(next_state)

    return next_state

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
