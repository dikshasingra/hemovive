import pandas as pd
import os

# Input and Output Paths
input_path = "data/processed/NFHS-5 States data.csv"
output_path = "data/processed/NFHS-5 States cleaned.csv"

# Load the data
df = pd.read_csv(input_path)

# Optional: Print first few rows to confirm structure
print("Original Columns:", df.columns.tolist())

# Standardize state names using a mapping (example)
state_map = {
    "Odisha": "Orissa",
    "Delhi": "NCT of Delhi"
    # Add more corrections here if needed
}

# Apply cleaning (column name is lowercase 'state')
if 'state' in df.columns:
    df['state'] = df['state'].replace(state_map)
else:
    print("Column 'state' not found!")

# Save cleaned file
os.makedirs(os.path.dirname(output_path), exist_ok=True)
df.to_csv(output_path, index=False)
print(f"✅ Cleaned data saved to: {output_path}")

