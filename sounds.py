import subprocess
import re
from util import Util

class Sounds(Util):
    def __init__(self):
        pass

    def list_options(self):
        output = subprocess.check_output("pacmd list-sinks".split(" "))
        return re.findall("index: ([0-9]+)", output.decode("utf-8"))

    def format_command(self, next_state):
        return f"pacmd set-default-sink {next_state}"
