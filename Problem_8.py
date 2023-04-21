import pandas as pd
import matplotlib.pyplot as plt

# Load data from CSV file
data = pd.read_csv("actor_kill_counts.csv")

# Sort data by kill count in descending order
sorted_data = data.sort_values('Count', ascending=False)

# Create a horizontal bar chart
fig, ax = plt.subplots(figsize=(10, 6))
ax.barh(sorted_data['Actor'], sorted_data['Count'], color='orange')

# Set chart title and axis labels
ax.set_title('Deadliest Actors in Hollywood by Kill Count')
ax.set_xlabel('Kill Count')
ax.set_ylabel('Actor')

# Invert y-axis to show actors with highest kill count at the top
ax.invert_yaxis()

# Display the chart
plt.show()
