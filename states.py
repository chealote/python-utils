def _decide_next_state(list_options, current_option):
    try:
        current_index = list_options.index(current_option)
        if current_index+1 != len(list_options):
            return list_options[current_index+1]
    except ValueError:
        pass

    return list_options[0]


def pick_next_state(list_options, util_name):
    if list_options == []:
        return None

    help_state_filepath = f"/tmp/.utils_state_{util_name}.tmp"

    current = None
    try:
        with open(help_state_filepath) as f:
            current = f.read()
    except FileNotFoundError as e:
        next_state = list_options[0]

    if current != None:
        next_state = _decide_next_state(list_options, current)

    # TODO in case there's an exception, ignore but the util is not
    # going to behave properly
    with open(help_state_filepath, "w") as f:
        f.write(next_state)

    return next_state
