import re
import sys
import subprocess

status_filename = f".{__file__.split('/')[-1]}"
status_filepath = f"/tmp/{status_filename}"
set_default_current_display = False
current_display = ""

def list_of_displays():
    with open("/var/log/Xorg.0.log") as f:
        content = f.read()

    displays = []
    for line in re.findall("Output [a-zA-Z0-9-]+ connected", content):
        m = re.match(".*Output ([a-zA-Z0-9-]+).*", line)
        displays.append(m.group(1) )

    if len(displays) == 0 or None in displays:
        raise Exception("Bad array of displays:", displays)

    return displays

def get_next_display(displays):
    current_display = None
    try:
        with open(status_filepath) as f:
            current_display = f.read()
            if not re.match("[a-zA-Z0-9-]+", current_display):
                raise Exception("Current display doesn't match")
    except FileNotFoundError:
        current_display = displays[0]

    if displays[-1] == current_display:
        return displays[0]
    for i, d in enumerate(displays):
        if d == current_display:
            return displays[i+1]
    raise Exception("Couldn't find the new display to make primary")

def format_xrandr_cmd(displays, new_current_display):
    xrandr_cmd = "xrandr "
    for d in displays:
        if d == new_current_display:
            xrandr_cmd += f"--output {d} --auto --primary "
        else:
            xrandr_cmd += f"--output {d} --off "
    xrandr_cmd_split = xrandr_cmd.split(" ")
    xrandr_cmd_split.remove("")
    return xrandr_cmd_split

def main():
    displays = list_of_displays()

    if len(displays) == 1:
        sys.exit(0)

    new_current_display = get_next_display(displays)

    cmd = format_xrandr_cmd(displays, new_current_display)
    try:
        r = subprocess.run(cmd)
        if r.returncode != 0:
            print("Failed to run command:", cmd)
            sys.exit(1)
    except Exception as e:
        print(f"Failed to run command: {e}")
        sys.exit(1)

    with open(status_filepath, "w") as f:
        f.write(new_current_display)

if __name__ == "__main__":
    main()
