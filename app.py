import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd
import pickle

# Load trained model
with open("model.pkl", "rb") as file:
    model = pickle.load(file)

# Function to predict a single input
def predict_single():
    try:
        input_data = entry.get()
        values = [float(x) for x in input_data.split(",")]
        prediction = model.predict([values])[0]
        result_label.config(text=f"Prediction: {'Anomaly' if prediction else 'Normal'}", fg="red" if prediction else "green")
    except Exception as e:
        messagebox.showerror("Error", f"Invalid input! {e}")

# Function to predict from CSV file
def predict_csv():
    file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    if not file_path:
        return
    try:
        df = pd.read_csv(file_path)
        predictions = model.predict(df)
        df["Prediction"] = ["Anomaly" if p else "Normal" for p in predictions]
        df.to_csv("output_predictions.csv", index=False)
        messagebox.showinfo("Success", "Predictions saved in 'output_predictions.csv'")
    except Exception as e:
        messagebox.showerror("Error", f"Could not process file: {e}")

# UI Setup
root = tk.Tk()
root.title("Network Anomaly Detection")
root.geometry("400x300")

tk.Label(root, text="Enter network data (comma-separated):").pack(pady=5)
entry = tk.Entry(root, width=50)
entry.pack(pady=5)

predict_btn = tk.Button(root, text="Predict", command=predict_single)
predict_btn.pack(pady=5)

file_btn = tk.Button(root, text="Upload CSV & Predict", command=predict_csv)
file_btn.pack(pady=5)

result_label = tk.Label(root, text="Result will appear here", font=("Arial", 12))
result_label.pack(pady=10)

root.mainloop()
