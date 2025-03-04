import scapy.all as scapy
import pandas as pd
import joblib
import tkinter as tk
from tkinter import messagebox
import threading

# Load the trained model
model = joblib.load("model.pkl")

# Function to process network packets
# Function to process network packets
def process_packet(packet):
    if packet.haslayer(scapy.IP):
        features = {
            "count": 1,  # Example value, update it properly
            "diff_srv_rate": 0.5,  # Example value, update it properly
            "dst_bytes": len(packet),  # Length as dst_bytes
            "dst_host_count": 1,  # Example value, update it properly
            "dst_host_diff_srv_rate": 0.1  # Example value, update it properly
        }
        
        # Convert to DataFrame
        df = pd.DataFrame([features])

        # Make prediction
        prediction = model.predict(df)

        # Show result
        if prediction[0] == 1:  # Assuming '1' means anomaly
            print(f" Anomaly detected!")
            update_ui(f"Anomaly detected!")


# Function to start network sniffing
def start_sniffing():
    scapy.sniff(prn=process_packet, store=False)

# Tkinter UI
root = tk.Tk()
root.title("Real-Time Network Anomaly Detector")
root.geometry("500x300")

label = tk.Label(root, text="Monitoring Network Traffic...", font=("Arial", 12))
label.pack(pady=20)

def update_ui(message):
    messagebox.showwarning("Anomaly Alert!", message)

# Start sniffing in a separate thread
threading.Thread(target=start_sniffing, daemon=True).start()

root.mainloop()


