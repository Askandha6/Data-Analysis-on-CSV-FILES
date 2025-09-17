CSV Data Analysis Script

Overview

This script reads a CSV file and performs basic data analysis using the pandas library. It displays the first few rows of the data, data types of each column, summary statistics, and checks for missing values.

Requirements

- Python 3.x
- pandas library (install using pip install pandas)

Usage

1. Save this script as a Python file (e.g., csv_analysis.py).
2. Replace file_path in the main function with the path to your CSV file.
3. Run the script using Python (e.g., python csv_analysis.py).

Functions

read_csv(file_path)
- Reads a CSV file using pd.read_csv.
- Handles FileNotFoundError and pd.errors.EmptyDataError exceptions.

analyze_data(data)
- Displays the first few rows of the data using data.head().
- Prints data types of each column using data.dtypes.
- Calculates summary statistics using data.describe().
- Checks for missing values using data.isnull().sum().

Example Use Case

Suppose you have a CSV file data.csv containing:
Name	Age	Score
John	25	85
Jane	30	90
Bob	35	78
Running the script with file_path = 'data.csv' will output:
First few rows of the data:
   Name  Age  Score
0   John   25     85
1   Jane   30     90
2    Bob   35     78

Data types of each column:
Name      object
Age       int64
Score     int64
dtype: object

Summary statistics of the data:
          Age       Score
count  3.000000   3.000000
mean  30.000000  84.333333
std    5.000000   6.027713
min   25.000000  78.000000
25%   27.500000  81.500000
50%   30.000000  85.000000
75%   32.500000  87.500000
max   35.000000  90.000000

Missing values in the data:
Name     0
Age      0
Score    0
dtype: int64
