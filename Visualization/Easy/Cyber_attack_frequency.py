import matplotlib.pyplot as plt

# Preview the dataset
df.head()


# Sample cyber attack frequency data
# attack_types = ['Phishing', 'Malware', 'Ransomware']
# frequencies = [120, 85, 45]

# Required color mapping
colors = ['black', 'red', 'purple']

# Create the bar chart
plt.figure(figsize=(10, 6))
plt.bar(df['attack_type'], df['frequency'], color=colors)

# Add chart labels and title
plt.title('Frequency of Cyber Attacks on a Network')
plt.xlabel('Attack Type')
plt.ylabel('Frequency')

# Display the chart
plt.grid(axis='y', linestyle='--', alpha=0.7)
# plt.tight_layout()  (Here, grid() improves readability, while tight_layout() helps ensure the chart elements fit neatly inside the figure.)
plt.show()
