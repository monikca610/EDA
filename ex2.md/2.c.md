Program 3: Histogram – Age Distribution:

# Program 3: Histogram

import pandas as pd
import matplotlib.pyplot as plt

# Load the Employee dataset
df = pd.read_csv("Employee (3)(1).csv")

# Create Histogram
plt.figure(figsize=(8,5))

plt.hist(df["Age"], bins=10, edgecolor="black")

plt.title("Age Distribution of Employees")
plt.xlabel("Age")
plt.ylabel("Frequency")

plt.grid(True)
plt.show()

OUTPUT:
<img width="887" height="595" alt="Screenshot 2026-08-13 213633" src="https://github.com/user-attachments/assets/9decd763-a3b7-4f1e-9790-1d91a226b697" />
