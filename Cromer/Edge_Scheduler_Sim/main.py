# This is the main entry point for the Edge Scheduler Simulation.
# It initializes the scheduler and registers tasks to be executed.
# Edge_Scheduler_Sim/main.py
# main.py

from Scheduler import Scheduler
from task_a import run_task_a
from task_b import run_task_b
from task_c import run_task_c
from node import Node

# Create nodes
rpi = Node("rpi")
jetson = Node("jetson")
blade = Node("blade")

nodes = [rpi, jetson, blade]

# Initialize scheduler with nodes
scheduler = Scheduler(nodes)
scheduler.register_task("Task A", run_task_a)
scheduler.register_task("Task B", run_task_b)
scheduler.register_task("Task C", run_task_c)

# Run all tasks
scheduler.run_all()