import pandas as pd

# Path to your Excel file
file_path = "path_to_your_file.xlsx"

# Read the Excel file
df = pd.read_excel(file_path, engine="openpyxl", header=None)  # Read without assuming a header

# Collect all unique column names from all rows
unique_columns = set()
for row in df.values:  # Iterate over rows
    unique_columns.update(str(item).strip() for item in row if pd.notna(item))  # Remove NaNs & whitespace

# Convert to DataFrame
master_ciq = pd.DataFrame({"Master CIQ Columns": list(unique_columns)})

# Save as new Excel file
output_file = "master_ciq.xlsx"
master_ciq.to_excel(output_file, index=False, engine="openpyxl")

print(f"Master CIQ saved to: {output_file}")
