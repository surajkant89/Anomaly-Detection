import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score










# Load the preprocessed dataset
df = pd.read_csv("preprocessed_kddcup.csv")

# Separate features (X) and labels (y)
X = df.drop(columns=["label"])  # All columns except "label"
y = df["label"]  # Target column (anomaly or normal)

# Split into training (80%) and testing (20%) sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the Decision Tree Classifier
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy * 100:.2f}%")



# Load the dataset
df = pd.read_csv("preprocessed_kddcup.csv")

# Now "label" should exist
X = df.drop(columns=["label"])  # Features
y = df["label"]  # Target variable






import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.metrics import confusion_matrix, classification_report

# Predict on test data
y_pred = model.predict(X_test)

#  Confusion Matrix
cm = confusion_matrix(y_test, y_pred)

#  Define class labels (use fewer categories if possible)
class_labels = np.unique(y_test)  # This dynamically assigns labels

plt.figure(figsize=(10, 6))  # Increase figure size
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=class_labels, yticklabels=class_labels)
plt.xlabel("Predicted Label")
plt.ylabel("Actual Label")
plt.title("Confusion Matrix (Improved)")
plt.xticks(rotation=45)  # Rotate labels for better visibility
plt.yticks(rotation=0)
plt.show()

#  Print Classification Report
print("Classification Report:\n", classification_report(y_test, y_pred))


import pickle

# Save the trained model
with open("model.pkl", "wb") as file:
    pickle.dump(model, file)

print(" Model saved as 'model.pkl'")
