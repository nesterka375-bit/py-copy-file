def copy_file(command: str) -> None:
    parts = command.split(" ")
    if len(parts) == 3 and parts[0] == "cp" and parts[1] != parts[2]:
        cp, old_file, new_file = parts
        try:
            with (open(old_file, "r") as file_in,
                  open(new_file, "w") as file_out):
                file_out.write(file_in.read())
        except Exception:
            pass
