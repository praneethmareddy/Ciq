import pandas as pd
import glob
import os
import re

# Folder containing CIQ Excel files
ciq_folder = "./ciq_files/"

# Get all Excel files in the folder
ciq_files = glob.glob(os.path.join(ciq_folder, "*.xlsx"))

# Dictionary to store column names from each CIQ
ciq_columns = {}

# Dictionary to map normalized column names to original names
normalized_columns = {}

for file in ciq_files:
    df = pd.read_excel(file, nrows=0)  # Read only column names
    original_columns = list(df.columns)
    
    normalized_file_columns = []
    
    for col in original_columns:
        normalized_col = re.sub(r"[\s_]+", "_", col.strip().lower())  # Normalize spaces & underscores
        if normalized_col not in normalized_columns:
            normalized_columns[normalized_col] = col  # Store original formatting
        normalized_file_columns.append(normalized_columns[normalized_col])
    
    ciq_columns[os.path.basename(file)] = normalized_file_columns

# Generate a unique list of normalized column names
unique_columns = list(normalized_columns.values())

# Save column names to a text file
text_file_path = os.path.join(ciq_folder, "ciq_columns_summary.txt")

with open(text_file_path, "w") as f:
    f.write("Unique Column Names:\n")
    f.write(", ".join(unique_columns) + "\n")
    f.write("=" * 50 + "\n\n")

    for file, columns in ciq_columns.items():
        f.write(f"File: {file}\n")
        f.write(f"Columns: {', '.join(columns)}\n")
        f.write("-" * 50 + "\n")

print(f"Column names summary saved to {text_file_path}")
