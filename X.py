import os
import pandas as pd
from glob import glob

# Folder containing all CIQ Excel files
ciq_folder = "path_to_your_ciq_files"  # Change this to your actual folder path

# Get all Excel files
ciq_files = glob(os.path.join(ciq_folder, "*.xlsx"))

# Print the list of found files
if not ciq_files:
    print("No XLSX files found in the specified folder!")
else:
    print("Found the following XLSX files:")
    for file in ciq_files:
        print(f"- {os.path.basename(file)}")

# List to store standardized dataframes
dfs = []

# Process each CIQ file safely
for file in ciq_files:
    try:
        # Read Excel with openpyxl engine (safer for XLSX)
        df = pd.read_excel(file, header=None, engine="openpyxl")
        
        # Check orientation: more rows than columns → likely row-wise
        if df.shape[0] > df.shape[1]:  
            df = df.T  # Transpose row-wise data to column format

        df.columns = df.iloc[0]  # Set first row as column headers
        df = df[1:].reset_index(drop=True)  # Remove the first row from data

        df["Source_File"] = os.path.basename(file)  # Add column to track the source file
        dfs.append(df)

        # Clear variables to free memory
        del df

    except Exception as e:
        print(f"❌ Error reading {file}: {e}")

# Ensure we have at least one valid CIQ before merging
if dfs:
    try:
        master_ciq = pd.concat(dfs, ignore_index=True, sort=False)  # Merge all dataframes
        master_ciq.fillna("N/A", inplace=True)  # Fill missing values

        # Save in chunks to prevent memory crash
        with pd.ExcelWriter("Master_CIQ.xlsx", engine="openpyxl") as writer:
            master_ciq.to_excel(writer, index=False)

        print("\n✅ Master CIQ successfully created as 'Master_CIQ.xlsx'")

    except Exception as e:
        print(f"\n❌ Error while merging CIQs: {e}")

else:
    print("\n❌ No valid CIQ files found! Master CIQ was not created.")
