"""01_clean_aggregate.py

TODO:
- Load the raw Excel dataset (airline_route_profitability.xlsx)
- Clean missing values (e.g., infer missing ancillary/catering/handling from totals when possible)
- Aggregate to planning level (route, period, aircraft) to compute:
    * profit_per_flight (π_rta)
    * flight_hours_per_flight (h_rta)
    * cost_per_flight (c_rta)
    * revenue_per_flight (rev_rta)
    * observed_flights (n_rta)
- Export parameters to: data/processed/params_rta.csv
"""

def main():
    raise NotImplementedError("Implement data cleaning + aggregation here.")

if __name__ == "__main__":
    main()
