Weekly Progress Log – Scheduler Evaluation & Visualization (July 1–5, 2025)

Weekly Focus:

    Extracting meaningful metrics from TensorBoard
    Comparing performance between WaggleScheduler and FairshareScheduler
    Fixing energy consumption reporting bugs
    Building visualizations for clarity
    Adapting Henry’s dual descent scheduler into simulation




Goals for this week 


Task 1
Convert TensorBoard logs into CSV for better metric visibility

Task 2
Add per-node statistics: mean energy, workload count, task time

Task 3
Compare all metrics across different schedulers

Fixes
Address bug where TensorBoard showed energy=0 despite CPU usage

Enhancement
Add support for visualizing and identifying scheduler results

Research
Integrate Henrys dual_descent into new scheduler module


Monday

    🛠 Bugfix: Fixed issue where TensorBoard reported 0 energy usage even with non-zero CPU.
    subtask : bug fix  26c24d2a7f13a7f0fafd66713ecb27390a0f12b0

    🔧 Added new metrics lines to __init__() for energy tracking.
    ✅ Simulation now records meaningful energy data.
    🧪 Verified both WaggleScheduler and FairshareScheduler logs generate usable CSVs.




Tuesday

    🤝 Met with Henry to discuss dual descent scheduler integration.
    📈 Clarified expected output from dual_descent:
    A matrix like:
    [[0, 1], [1, 0], [0, 1]] → Each row = workload, column = node.
    🧠 Brainstormed how to pass simulation state to dual descent function.
    🧰 Began adapting simulation run to accept new dual-descent placement matrix.




Wednesday
    Met with Yongho
    ✅ Updated run.py line 103 to include total energy in TensorBoard logs.
    📊 TensorBoard now outputs energy correctly.
    🧠 Brainstormed visual identification for scheduler logs:
        Current challenge: All logs look similar (over 30+), hard to trace which run = which scheduler.
        Solution: Need clear naming/labeling for scheduler in TensorBoard or CSV.



Thursday

    🎨 Finished first version of visualization code:
        Plots energy, task count, execution time per node.

    ✅ Task 2 completed: all metrics per node calculated.
    ✅ Task 3 attempted:
        CSV output works
        ❌ Error: [ERROR] No scheduler data to compare.
            Suspected cause: TensorBoard logs don’t differentiate waggle vs fairshare


    🔧 Fixed file path bugs that caused directory mismatch errors earlier.
    🧪 Now receives output files with task metrics per scheduler — working toward full comparison.

my new working code 
f5bbbf49b94c5a4feaf7fbb2faf3b11c91e38df7


