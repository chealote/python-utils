import re
from utils import main

status_filename = f".{__file__.split('/')[-1]}"
displays = [] # need to keep this to turn off all other displays

def list_of_displays():
    with open("/var/log/Xorg.0.log") as f:
        content = f.read()

    for line in re.findall("Output [a-zA-Z0-9-]+ connected", content):
        m = re.match(".*Output ([a-zA-Z0-9-]+).*", line)
        displays.append(m.group(1) )

    if len(displays) == 0 or None in displays:
        raise Exception("Bad array of displays:", displays)

    return displays

def format_xrandr_cmd(new_current_display):
    xrandr_cmd = "xrandr "
    for d in displays:
        if d == new_current_display:
            xrandr_cmd += f"--output {d} --auto --primary "
        else:
            xrandr_cmd += f"--output {d} --off "
    xrandr_cmd_split = xrandr_cmd.split(" ")
    xrandr_cmd_split.remove("")
    return xrandr_cmd_split

main(status_filename, list_of_displays, format_xrandr_cmd)
