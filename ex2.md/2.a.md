Program 1: Bar Chart – Employee Count by Education:

# Program 1: Bar Chart

import pandas as pd
import matplotlib.pyplot as plt

# Load the Employee dataset
df = pd.read_csv("Employee (3)(1).csv")

# Count employees in each education category
education_count = df["Education"].value_counts()

# Create Bar Chart
plt.figure(figsize=(8,5))
education_count.plot(kind="bar")

plt.title("Employee Count by Education")
plt.xlabel("Education")
plt.ylabel("Number of Employees")

plt.show()

OUTPUT:
<img width="933" height="675" alt="Screenshot 2026-08-13 213318" src="https://github.com/user-attachments/assets/21df69bc-44e6-4d23-bff9-d241a018da60" />
