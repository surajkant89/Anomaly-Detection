from scapy.all import sniff, IP, TCP, UDP
import pandas as pd
import joblib

# Load trained ML model
model = joblib.load("model.pkl")

# Function to process captured packets
def process_packet(packet):
    if packet.haslayer(IP):
        features = {
            "protocol": packet[IP].proto,
            "length": len(packet),
            "count": 1,  # Example: Set default values for missing features
            "diff_srv_rate": 0,
            "dst_bytes": 0,
            "dst_host_count": 1,
            "dst_host_diff_srv_rate": 0,
        }
        return features

print("Capturing 1 packet...")
captured_packets = sniff(count=1)

# Process the captured packet
features = process_packet(captured_packets[0])

# Convert to DataFrame
df = pd.DataFrame([features])

# Ensure feature order matches training data
expected_features = model.feature_names_in_
df = df[expected_features]  # Select only the features used during training

print("\nFeature DataFrame for Prediction:")
print(df)

# Predict using ML model
prediction = model.predict(df)

if prediction[0] == 1:
    print("⚠️ Anomaly Detected!")
else:
    print("✅ Normal Traffic")
