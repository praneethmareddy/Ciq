import pandas as pd
import glob
import os

# Folder containing CIQ Excel files
ciq_folder = "./ciq_files/"

# Get all Excel files in the folder
ciq_files = glob.glob(os.path.join(ciq_folder, "*.xlsx"))

# Dictionary to store column names from each CIQ
ciq_columns = {}

for file in ciq_files:
    df = pd.read_excel(file, nrows=0)  # Read only column names
    ciq_columns[os.path.basename(file)] = list(df.columns)

# Print column names for each file
for file, columns in ciq_columns.items():
    print(f"\nFile: {file}")
    print(f"Columns: {columns}")

# Optionally, save the columns to a CSV file
columns_df = pd.DataFrame(dict([(k, pd.Series(v)) for k, v in ciq_columns.items()]))
columns_df.to_csv(os.path.join(ciq_folder, "ciq_columns_summary.csv"), index=False)

print("\nColumn names summary saved to ciq_columns_summary.csv")
