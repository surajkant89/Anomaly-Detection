import pandas as pd
from sklearn.preprocessing import LabelEncoder
# Load the dataset
df = pd.read_csv("kddcup_data_10_percent_corrected.csv", header=None)

# Show first 5 rows
print(df.head())

# Show dataset info
print(df.info())

# Check for missing values
print("Missing Values:\n", df.isnull().sum())
# Save the preprocessed data to a new CSV file
df.to_csv("preprocessed_kddcup.csv", index=False)

print(" Preprocessing complete! Saved as preprocessed_kddcup.csv")


# Define column names based on the KDDCup99 dataset

# Define column names
column_names = [
    "duration", "protocol_type", "service", "flag", "src_bytes", "dst_bytes", 
    "land", "wrong_fragment", "urgent", "hot", "num_failed_logins", "logged_in", 
    "num_compromised", "root_shell", "su_attempted", "num_root", "num_file_creations", 
    "num_shells", "num_access_files", "num_outbound_cmds", "is_host_login", 
    "is_guest_login", "count", "srv_count", "serror_rate", "srv_serror_rate", 
    "rerror_rate", "srv_rerror_rate", "same_srv_rate", "diff_srv_rate", 
    "srv_diff_host_rate", "dst_host_count", "dst_host_srv_count", "dst_host_same_srv_rate", 
    "dst_host_diff_srv_rate", "dst_host_same_src_port_rate", "dst_host_srv_diff_host_rate", 
    "dst_host_serror_rate", "dst_host_srv_serror_rate", "dst_host_rerror_rate", 
    "dst_host_srv_rerror_rate", "label"
]

# Load dataset with correct column names
df = pd.read_csv("kddcup_data_10_percent_corrected.csv", names=column_names, header=None)

# Convert categorical columns to numerical values using Label Encoding
categorical_columns = ["protocol_type", "service", "flag", "label"]
encoder = LabelEncoder()

for col in categorical_columns:
    df[col] = encoder.fit_transform(df[col])

# Show first 5 rows to confirm encoding
print(df.head())

# Save the preprocessed data
df.to_csv("preprocessed_kddcup.csv", index=False)

print(" Preprocessing complete! Saved as preprocessed_kddcup.csv")
