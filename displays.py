import subprocess
import re
from util import Util

class Displays(Util):
    def __init__(self):
        self._displays = None

    def list_options(self):
        displays = []
        content = subprocess.check_output("xrandr")
        for line in re.findall("[a-zA-Z0-9-]+ connected", content.decode("utf-8")):
            m = re.match("([a-zA-Z0-9-]+) connected.*", line)
            displays.append(m.group(1) )

        displays = [ d for d in displays if d != None ]

        self._displays = displays

        return displays

    def format_command(self, new_current_display):
        if self._displays == None:
            return ""

        xrandr_cmd = "xrandr "
        for d in self._displays:
            if d == new_current_display:
                xrandr_cmd += f"--output {d} --auto --primary "
            else:
                xrandr_cmd += f"--output {d} --off "
        return xrandr_cmd
