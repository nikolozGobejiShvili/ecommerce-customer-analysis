import pandas as pd

def load_and_clean_data(filepath):
    print("🔹 Loading dataset...")
    data = pd.read_csv(filepath, encoding='ISO-8859-1')

    print("🔹 Cleaning data...")
    # Drop missing CustomerID
    data = data.dropna(subset=['CustomerID'])

    # Remove negative or zero values
    data = data[(data['Quantity'] > 0) & (data['UnitPrice'] > 0)]

    # Remove duplicates
    data = data.drop_duplicates()

    # Create TotalPrice
    data['TotalPrice'] = data['Quantity'] * data['UnitPrice']

    print("✅ Data cleaned successfully!")
    return data
