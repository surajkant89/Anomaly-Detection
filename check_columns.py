import pandas as pd

# Load the dataset
df = pd.read_csv("preprocessed_kddcup.csv")

# Print column names
print("Column Names:", df.columns.tolist())  # Print column names as a list
