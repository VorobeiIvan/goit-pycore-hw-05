def parse_input(user_input):
    parts = user_input.strip().split()
    if len(parts) == 0:
        return None, []
    cmd, *args = parts
    return cmd.lower(), args