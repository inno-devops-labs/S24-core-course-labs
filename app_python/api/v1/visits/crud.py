import os
import json

file = "./visits/visits.json"


def get_visits():
    if not os.path.exists(file):
        with open(file, 'w') as f:
            f.write(json.dumps({"visits": 0}))
        return 0

    with open(file, "r") as f:
        return int(json.loads(f.read())["visits"])


def set_visits(new_visit: int):
    with open(file, "w") as f:
        f.write(json.dumps({"visits": new_visit}))
