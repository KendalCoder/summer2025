🧾 Project Overview

This project simulates a basic task scheduling system designed to mimic how tasks are distributed and run on different types of computers in an edge computing environment. It models a simple scheduler that assigns tasks to various compute nodes, each representing a different kind of hardware device.


🧱 Components



- main.py

This is the main script that:

Creates a Scheduler instance.
Registers 3 example tasks (Task A, Task B, and Task C).
Executes all tasks through the scheduler.



- scheduler.py

Defines the Scheduler class. 
It:

Stores all registered tasks.
Initializes 3 compute nodes, each representing a different kind of computer:
🧠 rpi – A Raspberry Pi, a small single-board computer commonly used in IoT.
⚡ jetson – An NVIDIA Jetson, designed for edge AI computing with GPUs.
💻 blade – A blade server, a powerful, rack-mounted machine used in data centers.

When running tasks:
Randomly assigns each task to one of the three compute nodes.
Tells the node to run the task.
Tracks how many times each task is executed.

Prints a summary of task executions at the end.



- node.py

Defines the ComputeNode class. Each node:



Has a name (representing the type of computer it simulates).
Receives tasks from the scheduler.
Runs the task function and prints which node handled it.



- task_a.py , task_b.py , task_c.py

Each file contains a function that simulates a real task:

run_task_a, run_task_b, and run_task_c simulate execution using time.sleep().
They print start and completion messages for visibility.


- Output 

Assigned task 'Task A' to node 'jetson'
Node jetson is executing: Task A
Task A started
Task A completed

Assigned task 'Task B' to node 'rpi'
Node rpi is executing: Task B
Task B started
Task B completed

Assigned task 'Task C' to node 'blade'
Node blade is executing: Task C
Task C started
Task C completed

=== Task Execution Summary ===
Task A: 1 time(s)
Task B: 1 time(s)
Task C: 1 time(s)