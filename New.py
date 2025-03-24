import pandas as pd

# Load the Excel files
file1 = 'path_to_file1.xlsx'
file2 = 'path_to_file2.xlsx'

# Load the sheets into pandas DataFrames (you can specify sheet names or use sheet index)
sheet1_df = pd.read_excel(file1, sheet_name=0)  # Adjust sheet index or name as needed
sheet2_df = pd.read_excel(file2, sheet_name=0)  # Adjust sheet index or name as needed

# 1. Compare the number of rows in each sheet
rows_sheet1 = len(sheet1_df)
rows_sheet2 = len(sheet2_df)
print(f"Number of rows in Sheet 1: {rows_sheet1}")
print(f"Number of rows in Sheet 2: {rows_sheet2}")

# 2. Find common columns between both sheets
common_columns = sheet1_df.columns.intersection(sheet2_df.columns)
print(f"Common columns between the sheets: {common_columns.tolist()}")

# 3. Compare the content of the common columns
# First, align the columns in both DataFrames
sheet1_common = sheet1_df[common_columns]
sheet2_common = sheet2_df[common_columns]

# Check for differences in values between the common columns
comparison_result = sheet1_common == sheet2_common
rows_with_diff = comparison_result[~comparison_result.all(axis=1)]

print(f"Rows with differences in common columns: {len(rows_with_diff)}")
if not rows_with_diff.empty:
    print(rows_with_diff)

# 4. Advanced analysis - e.g., Missing values in the common columns
missing_values_sheet1 = sheet1_common.isnull().sum()
missing_values_sheet2 = sheet2_common.isnull().sum()

print("\nMissing values in Sheet 1 (common columns):")
print(missing_values_sheet1)

print("\nMissing values in Sheet 2 (common columns):")
print(missing_values_sheet2)

# 5. Identifying rows in Sheet 1 that are not in Sheet 2 (and vice versa)
unique_rows_sheet1 = sheet1_df[~sheet1_df.apply(tuple, 1).isin(sheet2_df.apply(tuple, 1))]
unique_rows_sheet2 = sheet2_df[~sheet2_df.apply(tuple, 1).isin(sheet1_df.apply(tuple, 1))]

print(f"\nUnique rows in Sheet 1 (not in Sheet 2): {len(unique_rows_sheet1)}")
print(f"Unique rows in Sheet 2 (not in Sheet 1): {len(unique_rows_sheet2)}")

# You can save the results to a new Excel file if needed
# with pd.ExcelWriter('comparison_results.xlsx') as writer:
#     unique_rows_sheet1.to_excel(writer, sheet_name="Unique Rows Sheet 1")
#     unique_rows_sheet2.to_excel(writer, sheet_name="Unique Rows Sheet 2")
