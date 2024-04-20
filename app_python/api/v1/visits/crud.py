import os


def get_visits():
    if not os.path.exists('visits'):
        with open('visits', 'w') as f:
            f.write(str(0))
        return 0

    with open("visits", "r") as f:
        return int(f.read())


def set_visits(new_visit: int):
    with open("visits", "w") as f:
        f.write(str(new_visit))
