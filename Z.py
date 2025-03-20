import pandas as pd

# Path to the input CSV file
input_csv = "your_file.csv"  # Change this to your actual file path
output_csv = "master_columns.csv"

# Read CSV, ignoring blank lines
df = pd.read_csv(input_csv, header=None, skip_blank_lines=True, error_bad_lines=False, engine="python")

# Collect all unique column names from non-empty rows
unique_columns = set()
for row in df.itertuples(index=False):
    for col in row:
        if pd.notna(col) and str(col).strip():  # Ignore NaN and empty strings
            unique_columns.add(col.strip())  # Remove extra spaces

# Convert to DataFrame (as a single row)
master_df = pd.DataFrame([list(unique_columns)])

# Save to a new CSV file
master_df.to_csv(output_csv, index=False, header=False)

print(f"Master column row saved to: {output_csv}")
