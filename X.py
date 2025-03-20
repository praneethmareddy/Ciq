import os
import pandas as pd

# Folder containing Excel files
folder_path = "path_to_your_folder"

# Set to store unique column names
unique_columns = set()

# Loop through all Excel files in the folder
for file in os.listdir(folder_path):
    if file.endswith(".xlsx"):
        file_path = os.path.join(folder_path, file)
        df = pd.read_excel(file_path, nrows=0, engine="openpyxl")  # Use openpyxl for .xlsx
        unique_columns.update(df.columns)
    elif file.endswith(".xls"):
        file_path = os.path.join(folder_path, file)
        df = pd.read_excel(file_path, nrows=0, engine="xlrd")  # Use xlrd for .xls
        unique_columns.update(df.columns)

# Convert to DataFrame
unique_columns_df = pd.DataFrame({"Unique Columns": list(unique_columns)})

# Save to new Excel file
output_file = os.path.join(folder_path, "unique_columns.xlsx")
unique_columns_df.to_excel(output_file, index=False, engine="openpyxl")

print(f"Unique columns saved to: {output_file}")
