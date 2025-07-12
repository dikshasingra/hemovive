import pandas as pd

csv_path = "data/processed/NFHS-5 States data.csv"

try:
    df = pd.read_csv(csv_path)

    print("📊 Columns in CSV:")
    print(df.columns.tolist())

    print("\n🧾 First 5 Rows:")
    print(df.head())

    print("\n📍 Rows with Missing Anemia Data:")
    print(df[df.isnull().any(axis=1)])

except FileNotFoundError:
    print(f"❌ File not found at {csv_path}. Please check the filename and path.")
except Exception as e:
    print(f"⚠️ Error: {e}")
