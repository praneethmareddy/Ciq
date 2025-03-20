import os
import pandas as pd

# Folder containing Excel files
folder_path = "path_to_your_folder"
csv_folder = os.path.join(folder_path, "converted_csvs")  # Temporary folder for CSVs

# Ensure CSV folder exists
os.makedirs(csv_folder, exist_ok=True)

# Set to store unique column names
unique_columns = set()

# Convert Excel to CSV and extract columns
for file in os.listdir(folder_path):
    if file.endswith((".xlsx", ".xls")):
        file_path = os.path.join(folder_path, file)
        
        # Read Excel file (with proper engine)
        if file.endswith(".xlsx"):
            df = pd.read_excel(file_path, engine="openpyxl")
        else:  # .xls case
            df = pd.read_excel(file_path, engine="xlrd")
        
        # Save as CSV
        csv_file = os.path.join(csv_folder, file.replace(".xlsx", ".csv").replace(".xls", ".csv"))
        df.to_csv(csv_file, index=False)

        # Collect column names
        unique_columns.update(df.columns)

# Convert to DataFrame
unique_columns_df = pd.DataFrame({"Unique Columns": list(unique_columns)})

# Save unique columns to a new Excel file
output_file = os.path.join(folder_path, "unique_columns.xlsx")
unique_columns_df.to_excel(output_file, index=False, engine="openpyxl")

print(f"Converted Excel files to CSV in: {csv_folder}")
print(f"Unique columns saved to: {output_file}")
