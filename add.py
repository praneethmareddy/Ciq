import pandas as pd

# Path to your original Excel file
file_path = 'path_to_your_file.xlsx'

# Name of the sheet you want to extract (replace with your actual sheet name)
sheet_name = 'Sheet1'

# Load the specific sheet into a DataFrame
df = pd.read_excel(file_path, sheet_name=sheet_name)

# Create a new file name for the extracted sheet
new_file_name = f"{sheet_name}_extracted.xlsx"

# Save the DataFrame (which contains the sheet data) to a new Excel file
df.to_excel(new_file_name, index=False)

print(f"Created a new file: {new_file_name}")
