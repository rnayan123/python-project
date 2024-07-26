import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read the new Excel file
data = pd.read_excel("Modified_Analysis.xlsx")

# Correct the column name for gender to match the exact name in the dataset
trust_column = 'TrustPayment'

# Create a table of counts
count_table = pd.crosstab(data['AgeGroup'], data[trust_column])

# Create subplots
fig, axes = plt.subplots(1, 2, figsize=(15, 6))

# Create a stacked bar chart with count labels
count_table.plot(kind='bar', stacked=True, ax=axes[0])
axes[0].set_title("Stacked Bar Chart of Trust in Online Payment by Age Group")
axes[0].set_xlabel("Age Group")
axes[0].set_ylabel("Count")

# Calculate the accurate count of responses for the pie chart
accurate_counts = data[trust_column].value_counts()

# Create a pie chart for TrustPayment
selected_responses = ['Completely', 'Neither', 'Never', 'Quite often', 'Sometimes']
filtered_data = data[data[trust_column].isin(selected_responses)]

# Calculate the proportion of each selected response category
trust_counts = filtered_data[trust_column].value_counts(normalize=True) * 100

# Plotting the pie chart with adjusted parameters
trust_counts.plot(kind='pie', autopct='%1.1f%%', startangle=140, colors=sns.color_palette("pastel"), pctdistance=0.85, ax=axes[1])
axes[1].set_title("Pie Chart of Trust in Online Payment")
axes[1].set_ylabel("")  # Remove the ylabel
axes[1].axis('equal')

plt.tight_layout()
plt.show()
