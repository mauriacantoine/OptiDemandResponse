README.txt

===========================================
Project: Automated Demand Response Optimization with V2G and PV Integration
===========================================

DESCRIPTION
-----------
This Jupyter Notebook implements an energy management optimization model for a medium-sized factory equipped with PV panels, flexible appliances (AMM, heathing appliances), and EVs with bidirectional (V2G) capability. The goal is to minimize electricity costs under power threshold constraints using Gurobi. The notebook also simulates an uncontrolled baseline scenario to compare results across dynamic and fixed electricity pricing schemes.

CODE STRUCTURE
--------------
The notebook is organized as follows:

1. Input Parameters
   - Time resolution, pricing, power limits, comfort settings

2. Function Definitions
   - `ev_modeling()`: Models EVs as bidirectional batteries with SoC dynamics and cost tracking
   - `objective_function()`: Defines the total cost from all appliances
   - `compute_uncontrolled_baseline_with_breakdown()`: Simulates rule-based baseline costs

3. Optimization Model
   - Gurobi model creation and constraint formulation
   - Appliance scheduling for AMM, heating, EVs, etc.
   - Power threshold constraint logic

4. Scenario Analysis
   - Evaluation of 4 scenarios (fixed vs dynamic pricing, with/without PV)
   - Cost breakdown and SoC/charging plots
   - Comparison with baseline

5. Results Visualization
   - Cost vs threshold plots
   - Load profile and SoC plots


refer to the Outline of the Jupyter Notebook to travel easily across the code. 
REQUIREMENTS
------------
| Library       | Version         
|---------------|-----------------
| gurobipy      | >=10.0          
| numpy         | >=1.20          
| matplotlib    | >=3.5            
| pandas        | >=1.3    
| scipy.sparse  |        


REQUIRED FILES
--------------
- External data arrays CSV files (e.g., `dynamic_prices`, `critical_demand`, `PV_output`) 
- Gurobi license must be active and accessible for optimization

HOW TO RUN
----------
1. Ensure all required Python libraries are installed.
2. Activate your Gurobi license.
3. Open the notebook in JupyterLab or Jupyter Notebook.
4. Execute all cells sequentially.
5. Review outputs, plots, and cost comparisons across scenarios.

