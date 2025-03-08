import sys
from layouts import Layouts
from sounds import Sounds
from displays import Displays
from wallpapers import Wallpapers
from states import pick_next_state
from run_command import run_command

_usage = """
TBD: write the usage
"""

def main():
    dry_run = False
    if len(sys.argv) < 2:
        print(_usage)
        sys.exit(1)

    if len(sys.argv) == 3 and sys.argv[2] == "-d":
        dry_run = True

    util_str = sys.argv[1]
    util = None
    if util_str == "layouts":
        util = Layouts()
    elif util_str == "sounds":
        util = Sounds()
    elif util_str == "displays":
        util = Displays()
    elif util_str == "wallpapers":
        util = Wallpapers()
    else:
        print(f"unrecognized util name {util_str}")
        sys.exit(1)

    options = util.list_options()
    next_state = pick_next_state(options, util_str)
    cmd = util.format_command(next_state)
    if not dry_run:
        run_command(cmd)
    else:
        print(f"In dry run mode, here's the next state")
        print(f"  {cmd}")

if __name__ == "__main__":
    main()
