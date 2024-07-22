import pandas as pd
import matplotlib.pyplot as plt

# Your data
data = {
    'SD': [72, 110, 82, 94, 53, 29, 56, 69, 27],
    'SMP': [32, 53, 53, 73, 39, 46, 9, 7, 25],
    'SMA': [47, 84, 25, 26, 5, 18, 42, 46, 18],
    'SMK': [57, 79, 110, 141, 87, 57, 23, 30, 34],
    'SLB': [69.23, 67.48, 60.74, 56.29, 57.61, 38.67, 86.15, 90.79, 51.92],
    'Internet': [45.19, 51.53, 18.52, 15.57, 5.43, 24.0, 64.62, 60.53, 34.62],
    '% Tersedia Internet': [104, 163, 135, 167, 92, 75, 65, 76, 52]
}

# Creating a DataFrame
df = pd.DataFrame(data)

# Plotting line chart for '% Tersedia Internet' for each category
categories = ['SD', 'SMP', 'SMA', 'SMK', 'SLB']
fig, axes = plt.subplots(nrows=1, ncols=5, figsize=(20, 5))

for i, category in enumerate(categories):
    # Line chart
    df_plot = df[[category, '% Tersedia Internet']]
    df_plot.plot(kind='line', x=category, y='% Tersedia Internet', marker='o', ax=axes[i])
    axes[i].set_title(category)
    axes[i].set_ylabel('Persentase Internet (%)')
    axes[i].set_xlabel('')

plt.tight_layout()
plt.show()
