import sys
from layouts import Layouts
from sounds import Sounds
from displays import Displays
from wallpapers import Wallpapers
from volume import Volume
from states import pick_next_state
from run_command import run_command

_usage = """
TBD: write the usage
"""

# next state is a step increment
_utils_map_step = {
    "volume": Volume,
    "backlight": None,
}

# next state is given by an array of possible states
_utils_map_state = {
    "layouts": Layouts,
    "sounds": Sounds,
    "displays": Displays,
    "wallpapers": Wallpapers,
}

_utils_run_as_system = [ "layouts" ]

def _process_util_state(util_str):
    if util_str not in _utils_map_state:
        return

    util = _utils_map_state[util_str]
    if util is None:
        print(f"Util not implemented...")
        return

    u = util()
    options = u.list_options()
    next_state = pick_next_state(options, util_str)

    return u.format_command(next_state)

def _process_util_step(util_str, step_direction):
    if util_str not in _utils_map_step:
        return

    util = _utils_map_step[util_str]
    if util is None:
        print(f"Util not implemented...")
        return

    u = util(step_direction)
    return u.format_command(step_direction)

def main():
    cmd = None
    dry_run = "-d" in sys.argv
    args = [ a for a in sys.argv[1:] if a not in [ "-d" ] ]

    if len(args) < 1:
        print(_usage)
        sys.exit(1)

    util_str = args.pop(0)

    if util_str in _utils_map_state:
        cmd = _process_util_state(util_str)
    elif util_str in _utils_map_step:
        # these need a direction to know where to step to
        if len(args) == 0:
            print("missing arguments")
            sys.exit(1)
        print("args:", args[0])
        cmd = _process_util_step(util_str, args[0])
    else:
        print(f"unrecognized util name {util_str}")
        sys.exit(1)

    if cmd == None:
        print(f"no command returned?")
        sys.exit(1)

    print(f"Running the command: {cmd}")

    if not dry_run:
        if util_str in _utils_run_as_system:
            run_command(cmd, True)
        else:
            run_command(cmd)
    else:
        print(f"In dry run mode, here's the next state")
        print(f"  {cmd}")

if __name__ == "__main__":
    main()
