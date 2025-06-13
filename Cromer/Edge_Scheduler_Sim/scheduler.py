
# scheduler.py

import random
from node import ComputeNode

class Scheduler:
    def __init__(self, nodes):
        self.tasks = []
        self.task_counter = {}
        
        self.nodes = nodes  # List of Node objects

    def register_task(self, name, func):
        self.tasks.append((name, func))
        self.task_counter[name] = self.task_counter.get(name, 0)

    def run_all(self):
        for name, func in self.tasks:
            node = random.choice(self.nodes)
            print(f"Assigning {name} to node {node.name}")
            node.run_task(name, func)
            self.task_counter[name] += 1

        print("\nExecution Summary:")
        for task, count in self.task_counter.items():
            print("{task}: executed {count} time(s)")