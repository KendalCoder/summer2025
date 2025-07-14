Weekly Progress Log – Scheduler Evaluation & Visualization (July 7-11 2025)

Task this week 


Continue Focus on visualization this week 

Answer which one is better?

Waggle scheduler used less energy 


    CSV - data format 

compare that respect which  one works better which one works worse 


70% focus :

Task 2: add more metrics about the statistics of the logs, for example mean energy consumption of each compute node, how many workloads (applications) did each node take, etc.


Task 3: get all the metrics we added in Task 2 against different schedulers. For example, run the simulation with WaggleScheduler, get all metrics, and change the scheduler to Fairshare and get metrics again. It will be interesting to compare the metrics between the schedulers and which one is better.



30%:
Make Henry’s code like the other schedulers formats 


Monday 
Met with yongho 




Tuesday 

Task 2: add more metrics about the statistics of the logs, for example mean energy consumption of each compute node, how many workloads (applications) did each node take, etc.


Finish working on visualization 

Start Make Henry’s code like the other schedulers formats 


fix henry code
dfd18f186b64a0a09ec752335d72e25488440ec9




Wednesday 

reformatted version of your DualDescent class in a style consistent with typical scheduler classes. 

Added docstrings and argument descriptions.

• Renamed id to node_id to avoid Python built-in shadowing.

• Moved the algorithm into a schedule() method (assuming your schedulers implement scheduling this way).

• Added placeholder TODOs for stopcondition() and share() to clarify they need implementation.

• Fixed while not self.stopcondition() (you want to loop until stopping condition).
• Consistent use of self. attributes.
• Proper numpy array shapes in initialization.
• Added comments consistent with your other schedul




Task 3: get all the metrics we added in Task 2 against different schedulers. For example, run the simulation with WaggleScheduler, get all metrics, and change the scheduler to Fairshare and get metrics again. It will be interesting to compare the metrics between the schedulers and which one is better.



Prepare slides for meeting 

Update methodology and approach 

Work on  results portion for presentation journal 





Thursday 

Morning Meeting 
Evening meeting with yongho n northwestern team


TODOs:

Under kubernetes/logs we want those directories with datetime to be datetime-"scheduler name"
By Updating TensorBoard class to accept a scheduler name and include it in the

Fix csvexport.py



Finalize writing results ( what I’ve learned) for my journal 





Friday:




Visual Results (WIP)

Generated CSV:

    logs/WaggleScheduler_task_log.csv
    logs/FairshareScheduler_task_log.csv
    Comparison Output:
    logs/scheduler_comparison_metrics.csv
    Plotted:
    mean_energy_comparison.png
    num_tasks_comparison.png
    avg_task_time_comparison.png