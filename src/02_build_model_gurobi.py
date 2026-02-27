"""02_build_model_gurobi.py

TODO:
- Read data/processed/params_rta.csv
- Build MILP in Gurobi:
    Decision: x[r,t,a] = number of flights (integer >= 0)
    Objective: maximize sum(pi[r,t,a] * x[r,t,a])
    Constraints:
      * fleet-hour capacity: sum_r h[r,t,a] * x[r,t,a] <= H[t,a]
      * minimum service: sum_a x[r,t,a] >= L[r,t]  (or route-category version)
      * optional budget: sum_{r,a} c[r,t,a] * x[r,t,a] <= B[t]
- Export solution to outputs/solution_x_rta.csv and summary metrics
"""

def main():
    raise NotImplementedError("Implement Gurobi MILP model here.")

if __name__ == "__main__":
    main()
