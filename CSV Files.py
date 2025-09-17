import pandas as pd

def read_csv(file_path):
    try:
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError:
        print("File not found. Please check the file path.")
        return None
    except pd.errors.EmptyDataError:
        print("No data in file. Please check the file contents.")
        return None

def analyze_data(data):
    print("First few rows of the data:")
    print(data.head())

    print("\nData types of each column:")
    print(data.dtypes)

    print("\nSummary statistics of the data:")
    print(data.describe())
