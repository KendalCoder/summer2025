
# node.py

class ComputeNode:
    def __init__(self, name):
        self.name = name

    def run_task(self, task_name, task_func):
        print(f"[{self.name}] Running task: {task_name}")
        task_func()
        print(f"[{self.name}] Finished task: {task_name}")
