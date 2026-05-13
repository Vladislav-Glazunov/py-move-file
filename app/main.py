import os


def move_file(command: str) -> None:  # 5 usages  new *

    mv, file_name, destination_path = command.split()
    if mv != "mv" or destination_path[-1] == "/":
        return
    new_file = "".join(destination_path.split("/")[-1])

    directory = "/".join(destination_path.split("/")[:-1])
    if not directory:
        os.replace(file_name, new_file)
    else:
        os.makedirs(directory, exist_ok=True)
        os.replace(f"{file_name}", f"{directory}/{new_file}")
