import subprocess
import re
from util import Util

class Volume(Util):
    def __init__(self, direction):
        self._direction = direction
        self._step = 10
        self._options = ["up", "down"]

    # TODO next_state?
    def format_command(self, next_state):
        if self._direction not in self._options:
            return
        sinks = subprocess.check_output(f"pactl list sinks short".split(" ")).decode("utf-8")

        running_sink_id = -1
        try:
            running_sink_id = re.findall(".*RUNNING\n", sinks)[0].split("\t")[0]
        except (KeyError, IndexError):
            print(f"Cannot find current running sink")
            return

        check_vol_cmd = f"pactl get-sink-volume {running_sink_id}"
        current_volume_output = ""
        try:
            current_volume_output = subprocess.check_output(check_vol_cmd.split(" ")).decode("utf-8")
        except Exception:
            print(f"Failed to run: {check_vol_cmd}")
            return

        current_volume_find = re.findall("([0-9]+)%", current_volume_output)
        if len(current_volume_output) < 1:
            print(f"Failed finding the current volume percentage from:\n{current_volume_output}")
            return

        current_volume = int(current_volume_find[0])
        step = self._step
        if self._direction == "down":
            step *= -1
        current_volume += step
        print(current_volume)

        set_vol_cmd = f"pactl set-sink-volume {running_sink_id} {current_volume}%"
        return set_vol_cmd
