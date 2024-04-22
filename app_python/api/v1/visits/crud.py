import os

file = "./visits/visits.txt"


def get_visits():
    if not os.path.exists(file):
        with open(file, 'w') as f:
            f.write(str(0))
        return 0

    with open(file, "r") as f:
        return int(f.read())


def set_visits(new_visit: int):
    with open(file, "w") as f:
        f.write(str(new_visit))
