# Profit-Optimal Flight Planning (DS502 - Path B)

## Problem
Determine the number of flights per route, planning period, and aircraft type to maximize expected profit,
subject to fleet-hour capacity and minimum service constraints.

## Dataset (Source)
Airline Route Profitability and Cost Analysis (Kaggle):
https://www.kaggle.com/datasets/waleedfaheem/airline-route-profitability-and-cost-analysis/data

## Expected Method
Mixed-Integer Linear Programming (MILP) solved with Gurobi.

## Repo Structure
- data/raw: raw dataset 
- data/processed: aggregated parameters for optimization
- src: python scripts (cleaning, model, experiments)
- outputs: solutions and experiment results

## DS502 Deliverables Roadmap 

### D1 — Topic & Repo Setup (Week 3)
- Repo structure: `data/raw`, `data/processed`, `src`, `outputs`
- README: problem + dataset link + plan + roles
- LMS: one-page PDF (title, motivation, data source, problem, variables, MILP method, references)

### D2 — Proposal (Week 4)
- Finalize scope: monthly flight frequency planning for DXB routes
- Assumptions + data plan: parameter estimation for (route, month, aircraft)
- Baseline MILP: objective + core constraints + scenario list (10+)

### D3 — Mathematical Model v1 (Week 5)
- Write full notation: sets/parameters/variables/objective/constraints
- Define how π_rta, h_rta, c_rta are computed from aggregated data

### D4 — Implementation v1 + Baseline Results (Week 6)
- `src/01_clean_aggregate.py` → `data/processed/params_rta.csv`
- `src/02_build_model_gurobi.py` → baseline MILP solution + summary metrics
- Baseline outputs: total profit, utilization, route coverage

### D5 — Experiment Plan + Other Components (Week 7)
- Lock experiment matrix (≥10 runs): capacity scaling, fuel shock, min service tightening, budget cap
- Build simplified flow/assignment baseline for comparison (aircraft-hours allocation)

### Week 8 — First Progress Check
- Working pipeline + baseline + at least 3 scenario results

### D6 — Implementation v2 + Extended Results (Week 9)
- Add 1–2 realism constraints (budget and/or route-category service and/or loss-risk limit)
- Run full experiment set and export `outputs/experiments_summary.csv`

### D7 — ML/Advanced (Optional, Weeks 10–11)
- Optional: predict profit-per-flight (π_rta) using route/season/aircraft features and re-optimize

### D8 — Final Report + Slides (Week 12)
- Final report: data prep, MILP, flow baseline, experiments, results, limitations
- Slides: model summary + key scenario insights

### D9 — Presentation (Weeks 13–14)
- Final presentation with results, plots, and recommendations
