import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv('data.csv')
data_a = data[data['Group'] == 'A']
data_b = data[data['Group'] == 'B']

# print(data)
# print(data_a)
# print(data_b)
# print(data_a.describe())
# print(data_b.describe())

############################################

# Select a column to visualize
column = data_a['Total_Amount_Spent']

# Create a single plot (1x1) of a specific size
fig, axes = plt.subplots(1, 1, figsize=(16, 5))

# Initialize the plot title
axes.set_title(f'{column.name} Distribution')

# Generate histogram of column, specifying number of bins
axes.hist(column, bins=50)

# Label x and y axes
axes.set_xlabel(column.name)
axes.set_ylabel('Density')

# Render and save histogram data png file
out_file = "output/hist_chart.png"
plt.savefig(out_file, dpi=150)
print(f"Wrote hist chart to {out_file}")