class Scheduler:
    def __init__(self):
        self.tasks = []

    def register_task(self, name, func):
        self.tasks.append((name, func))

    def run_all(self):
        for name, func in self.tasks:
            print(f"Running task: {name}")
            func()
