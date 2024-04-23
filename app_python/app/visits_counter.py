from pathlib import Path

from config import VISITS_FILE


def increment_visit_counter():
    create_visits_file_if_not_exist()
    with open(VISITS_FILE, 'r') as f:
        line = f.readline()
        try:
            visits = int(line)
        except ValueError:
            visits = 0
    with open(VISITS_FILE, 'w') as f:
        f.write(str(visits + 1))


def get_visits() -> int:
    create_visits_file_if_not_exist()
    with open(VISITS_FILE, 'r') as f:
        line = f.readline()
        try:
            visits = int(line)
        except ValueError:
            visits = 0
    return visits


def create_visits_file_if_not_exist():
    file_path = Path(VISITS_FILE)
    file_path.parent.mkdir(parents=True, exist_ok=True)
    file_path.touch()
