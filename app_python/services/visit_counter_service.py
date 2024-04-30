import os


class VisitCounterService:
    default_counter_path = 'tmp/visits.txt'

    def __init__(self):
        super().__init__()
        self.path = os.getenv('VISIT_COUNTER_PATH', self.default_counter_path)

    def increment(self) -> None:
        counter = self.get()
        with open(self.path, 'w+') as f:
            f.write(str(counter + 1))

    def get(self) -> int:
        try:
            with open(self.path, 'r') as f:
                visits = f.read()
            return int(visits)
        except FileNotFoundError:
            return 0
