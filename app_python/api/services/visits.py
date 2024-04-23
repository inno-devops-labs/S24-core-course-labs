def increment_visits():
    visits_n = get_visits()
    with open("visits", "w") as visits:
        visits.write(str(visits_n + 1))


def get_visits():
    with open("visits", "r") as visits:
        s = visits.read()
        if s == "":
            return 0
        return int(s)
