from utils import main

status_filename = f".{__file__.split('/')[-1]}"

def list_layouts():
    return ["us", "latam"] # eñe!

def format_cmd(next_layout):
    return f"setxkbmap -option 'ctrl:nocaps' {next_layout}".split(" ")

main(status_filename, list_layouts, format_cmd)
