import os
import pandas as pd
from glob import glob

# Folder containing all CIQ Excel files
ciq_folder = "path_to_your_ciq_files"  # Change this to your folder path

# Get all Excel files
ciq_files = glob(os.path.join(ciq_folder, "*.xlsx"))

# List to store standardized dataframes
dfs = []

# Process each CIQ file
for file in ciq_files:
    try:
        df = pd.read_excel(file, header=None)  # Read Excel without assuming headers
        
        # Check orientation: more rows than columns → likely row-wise
        if df.shape[0] > df.shape[1]:  
            df = df.T  # Transpose row-wise data to column format

        df.columns = df.iloc[0]  # Set first row as column headers
        df = df[1:].reset_index(drop=True)  # Remove the first row from data

        df["Source_File"] = os.path.basename(file)  # Add column to track the source file
        dfs.append(df)

    except Exception as e:
        print(f"Error reading {file}: {e}")

# Merge all standardized CIQs
if dfs:
    master_ciq = pd.concat(dfs, ignore_index=True, sort=False)  # Merge dataframes
    master_ciq.fillna("N/A", inplace=True)  # Fill missing values
else:
    print("No valid CIQ files found!")
    exit()

# Save the Master CIQ as Excel
master_ciq.to_excel("Master_CIQ.xlsx", index=False, encoding="utf-8")

print("Master CIQ successfully created as 'Master_CIQ.xlsx'")
