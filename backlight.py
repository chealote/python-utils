import sys
import subprocess
import re

max_backlight_filepath="/sys/class/backlight/intel_backlight/max_brightness"
current_backlight_filepath="/sys/class/backlight/intel_backlight/brightness"
min_backlight=1
max_backlight=min_backlight
current_backlight=min_backlight
change_step=300

with open(max_backlight_filepath) as f:
    max_backlight = int(re.search("([0-9]+)", f.read()).group(1))

with open(current_backlight_filepath) as f:
    current_backlight = int(re.search("([0-9]+)", f.read()).group(1))

command = ""

if len(sys.argv) == 1:
    print(current_backlight)
    sys.exit(0)
elif len(sys.argv) == 2:
    command = sys.argv[1]

if command == "up":
    current_backlight += change_step
    if current_backlight > max_backlight:
        print("max!")
        current_backlight = max_backlight
elif command == "down":
    current_backlight -= change_step
    if current_backlight < min_backlight:
        print("min!")
        current_backlight = min_backlight

with open(current_backlight_filepath, "w") as f:
    f.write(str(current_backlight))
