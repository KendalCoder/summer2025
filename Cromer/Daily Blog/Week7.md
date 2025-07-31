July 14- 18 

Final goal to show for presentation: 
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


    Monday



    Finalized metrics to collect: mean energy, task count, avg execution time per node.
    Updated the task logger to include start_time, end_time, and energy_consumed_joules.
    Wrote extract_metrics() function to compute per-node statistics.
    Successfully generated CSVs for both WaggleScheduler and FairshareScheduler.



📁 Output:


    logs/WaggleScheduler_task_log.csv
    logs/FairshareScheduler_task_log.csv






Tuesday



    Created comparison script to merge Waggle and Fairshare metrics into:
        logs/scheduler_comparison_metrics.csv

    Validated that each node’s stats reflect accurate workload and energy data.



🧪 Learned:


    Efficient use of pandas.groupby() and datetime arithmetic.
    How scheduler design affects per-node behavior.







Wednesday



    Plotted three graphs using pandas.plot() and matplotlib:
        mean_energy_comparison.png
        num_tasks_comparison.png
        avg_task_time_comparison.png

    Each plot visualizes metrics side-by-side for Waggle and Fairshare across nodes.



📈 Visuals help:


    Quickly assess which scheduler is more energy-efficient or better at balancing load.


Thursday



    Edited waggle.yml to add more nodes:
        2x Raspberry Pi
        2x Jetson
        1x Blade

    Ensured rpi node participates in scheduling.
    Ran simulation again to confirm expanded topology worked as expected.



💡 Learned:


    YAML structure and impact of node types on task distribution and power use.






Friday



    Worked on poster section: Visual Results (WIP).
    Added key insights from graph analysis:
        Waggle is more energy-efficient but not always fastest.
        Fairshare balances task count better on high-power nodes.

    Added key takeaways for “Learning on the Lawn” presentation.


