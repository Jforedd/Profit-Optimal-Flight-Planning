from pathlib import Path
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# file path 
DATA_PATH = Path(r"C:\Users\ed024981\Desktop\DS502project\airline_route_profitability.xlsx")
# Output folder 
OUT_DIR = Path(r"C:\Users\ed024981\Desktop\DS502project\outputs\eda")
OUT_DIR.mkdir(parents=True, exist_ok=True)

# Read Excel
df = pd.read_excel(DATA_PATH, engine="openpyxl")
# Data info
print("Shape:", df.shape) # dimension preview
display(df.head(5)) # first rows
display(pd.DataFrame({"columns": df.columns})) # columns name
display(df.dtypes) # data types

# Check Dates 
df["Flight_Date"] = pd.to_datetime(df["Flight_Date"], errors="coerce") # Convert Flight_Date to datetime 

# check invalid dates
invalid_dates = df["Flight_Date"].isna().sum()
print("Invalid Flight_Date rows:", invalid_dates)

print("Date min:", df["Flight_Date"].min()) # data start date
print("Date max:", df["Flight_Date"].max()) # data end date
