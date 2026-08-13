Program 2: Pie Chart – Employee Distribution by Gender:

# Program 2: Pie Chart

import pandas as pd
import matplotlib.pyplot as plt

# Load the Employee dataset
df = pd.read_csv("Employee (3)(1).csv")

# Count employees by gender
gender_count = df["Gender"].value_counts()

# Create Pie Chart
plt.figure(figsize=(7,7))
gender_count.plot(kind="pie", autopct="%1.1f%%")

plt.title("Employee Distribution by Gender")
plt.ylabel("")

plt.show()

OUTPUT:
<img width="697" height="681" alt="Screenshot 2026-08-13 213455" src="https://github.com/user-attachments/assets/51cb958d-2849-4b15-99ea-a99071c6856f" />
