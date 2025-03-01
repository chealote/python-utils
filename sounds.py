import subprocess
import re
from utils import main

status_filename = f".{__file__.split('/')[-1]}"

def list_sinks():
    output = subprocess.check_output("pacmd list-sinks".split(" "))
    return re.findall("index: ([0-9]+)", output.decode("utf-8"))

def format_cmd(next_state):
    return f"pacmd set-default-sink {next_state}".split(" ")

main(status_filename, list_sinks, format_cmd)
