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

# Save column names to a text file
text_file_path = os.path.join(ciq_folder, "ciq_columns_summary.txt")

with open(text_file_path, "w") as f:
    for file, columns in ciq_columns.items():
        f.write(f"File: {file}\n")
        f.write(f"Columns: {', '.join(columns)}\n")
        f.write("-" * 50 + "\n")  # Separator line

print(f"Column names summary saved to {text_file_path}")
