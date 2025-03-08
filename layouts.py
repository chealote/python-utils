from util import Util

class Layouts(Util):
    def __init__(self):
        pass

    def list_options(self):
        return ["us", "latam"]

    def format_command(self, next_state):
        return f"setxkbmap -option 'ctrl:nocaps' {next_state}"
