import os
import pandas as pd
from glob import glob

# Folder containing all CIQ CSV files
ciq_folder = "path_to_your_ciq_files"  # Change this to your folder path

# Get a list of all CSV files in the folder
ciq_files = glob(os.path.join(ciq_folder, "*.csv"))

# List to store dataframes
dfs = []

# Read each CIQ file
for file in ciq_files:
    try:
        df = pd.read_csv(file, encoding="utf-8")  # Read CSV
        df["Source_File"] = os.path.basename(file)  # Add a column to track source CIQ
        dfs.append(df)
    except Exception as e:
        print(f"Error reading {file}: {e}")

# Merge all CIQs into one Master CIQ
if dfs:
    master_ciq = pd.concat(dfs, ignore_index=True, sort=False)  # Merge all dataframes
    master_ciq.fillna("N/A", inplace=True)  # Fill missing values
else:
    print("No valid CIQ files found!")
    exit()

# Save the Master CIQ
master_ciq.to_csv("Master_CIQ.csv", index=False, encoding="utf-8")

print("Master CIQ successfully created as 'Master_CIQ.csv'")
