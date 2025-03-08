import os
import re
import random
from util import Util

class Wallpapers(Util):
    def __init__(self):
        pass

    def list_options(self):
        basepath = os.getenv("HOME") + "/Pictures/wallpapers/"
        files = [ f"{basepath}/{f}" for f in os.listdir(basepath)
                  if re.match(".*\.(png|jpg)", f) != None ]
        return [ random.choice(files) ]

    def format_command(self, next_state):
        return f"feh --bg-fill {next_state}"
