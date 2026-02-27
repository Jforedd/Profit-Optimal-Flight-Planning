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
- data/raw: raw dataset (or link)
- data/processed: aggregated parameters for optimization
- src: python scripts (cleaning, model, experiments)
- outputs: solutions and experiment results

## Plan (Week 3)
- Create repo structure (data/, src/)
- Clean + aggregate data to monthly parameters (route, month, aircraft)
- Implement baseline MILP (fleet-hours capacity + minimum service)
- Define experiment grid (10+ scenario runs)

## Roles (this week)
Individual work:
- Data prep: cleaning + aggregation
- Modeling: MILP formulation + Gurobi implementation
- Experiments: scenario definitions
- Reporting: tables/figures for proposal and Week 3 PDF
