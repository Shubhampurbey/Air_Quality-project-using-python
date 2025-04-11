#Data visulization(Graphs & charts )
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set Seaborn style
sns.set(style="whitegrid", palette="pastel")

# Load the dataset
data = pd.read_csv("air_quality.csv")

# Handle missing values
data.ffill(inplace=True)

# Correlation Heatmap
plt.figure(figsize=(12, 6))
sns.heatmap(data.corr(numeric_only=True), annot=True, cmap='YlGnBu', linewidths=0.5)
plt.title("Correlation Heatmap")
plt.show()

# Scatter Plot: pollutant_avg vs pollutant_max
plt.figure(figsize=(10, 5))
sns.scatterplot(x='pollutant_avg', y='pollutant_max', data=data, color='#1f77b4', s=60)
plt.title("Pollutant Average vs Max")
plt.xlabel("Pollutant Avg")
plt.ylabel("Pollutant Max")
plt.grid(True)
plt.show()

# Bar Plot: Top 10 Polluted States
plt.figure(figsize=(12, 6))
state_avg = data.groupby('state')['pollutant_avg'].mean().sort_values(ascending=False).head(10)
state_avg.plot(kind='bar', color=sns.color_palette("Set2"))
plt.title("Top 10 Polluted States")
plt.xlabel("State")
plt.ylabel("Avg Pollutant")
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.tight_layout()
plt.show()

# Line Plot: pollutant_avg Over Time
if 'date' in data.columns:
    data['date'] = pd.to_datetime(data['date'], errors='coerce')
    data.dropna(subset=['date'], inplace=True)
    data.sort_values('date', inplace=True)
    plt.figure(figsize=(14, 6))
    sns.lineplot(x='date', y='pollutant_avg', data=data, color='orange', linewidth=2)
    plt.title("Pollution Trend Over Time")
    plt.xlabel("Date")
    plt.ylabel("Pollutant Avg")
    plt.xticks(rotation=30)
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# Histogram: PM2.5 Distribution
if 'PM2.5' in data.columns:
    plt.figure(figsize=(10, 5))
    sns.histplot(data['PM2.5'], bins=30, kde=True, color='mediumorchid')
    plt.title("PM2.5 Distribution")
    plt.xlabel("PM2.5 Value")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.show()

# Pie Chart: Pollutant Type Distribution
if 'pollutant_id' in data.columns:
    plt.figure(figsize=(8, 8))
    data['pollutant_id'].value_counts().plot.pie(
        autopct='%1.1f%%', startangle=140,
        colors=sns.color_palette("pastel"), wedgeprops=dict(edgecolor='white')
    )
    plt.title("Pollutant Type Distribution")
    plt.ylabel("")
    plt.tight_layout()
    plt.show()

# Violin Plot: State-wise pollutant_avg Distribution
if 'state' in data.columns:
    plt.figure(figsize=(14, 6))
    sns.violinplot(x='state', y='pollutant_avg', data=data, palette='coolwarm', hue='state', legend=False)
    plt.title("State-wise Pollutant Avg Distribution")
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.show()
