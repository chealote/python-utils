import subprocess
import sys

status_filename = f".{__file__.split('/')[-1]}"
status_filepath = f"/tmp/{status_filename}"
default_current_layout = "us"

layouts = ["us", "latam"] # eñe!


try:
    with open(status_filepath) as f:
        current_layout = f.read()
except FileNotFoundError:
    current_layout = default_current_layout

if current_layout == "":
    current_layout = default_current_layout

next_layout = ""

if current_layout == layouts[-1]:
    next_layout = layouts[0]
else:
    for i, l in enumerate(layouts):
        if l == current_layout:
            next_layout = layouts[i+1]

with open(status_filepath, "w") as f:
    f.write(next_layout)

try:
    subprocess.Popen(f"setxkbmap -option 'ctrl:nocaps' {next_layout}".split(" "))
except Exception as e:
    print(f"Failed to switch layouts to {next_layout}")
    sys.exit(1)
