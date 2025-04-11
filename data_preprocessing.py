#Data cleaning & missing value handling  
import pandas as pd

# Load CSV File
file_path = "air_quality.csv"
data = pd.read_csv(file_path)

# Missing Values Handle
data.ffill(inplace=True)

# Display the output
print("\nDataset Info After Cleaning:")
print(data.info())
print("\nFirst 5 Rows:")
print(data.head())

