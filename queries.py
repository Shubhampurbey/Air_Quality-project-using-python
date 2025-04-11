#Queries likhne wala script  
import pandas as pd

# Load original CSV file
data = pd.read_csv("air_quality.csv")

# Handle missing values
data.ffill(inplace=True)

# 1️⃣ Total Rows & Columns Count
print("\nTotal Rows and Columns:")
print(data.shape)

# 2️⃣ Top & Bottom 5 Records
print("\nTop 5 Rows:")
print(data.head())

print("\nBottom 5 Rows:")
print(data.tail())

# 3️⃣ Missing Values Count
print("\nMissing Values Count:")
print(data.isnull().sum())

# 4️⃣ Average Pollutant Level
print("\nAverage Pollutant Level:")
print(data['pollutant_avg'].mean())

# 5️⃣ Max & Min Pollutant Avg
print("\nMax & Min Pollutant Avg:")
print("Max:", data['pollutant_avg'].max())
print("Min:", data['pollutant_avg'].min())

# 6️⃣ State-wise Average Pollution
print("\nState-wise Pollution:")
state_pollution = data.groupby('state')['pollutant_avg'].mean().reset_index()
print(state_pollution)

# 7️⃣ Most Polluted State
most_polluted = state_pollution.sort_values('pollutant_avg', ascending=False).head(1)
print("\nMost Polluted State:")
print(most_polluted)

# 8️⃣ City-wise Pollution
city_pollution = data.groupby('city')['pollutant_avg'].mean().reset_index()
print("\nCity-wise Pollution:")
print(city_pollution)

# 9️⃣ Highest AQI Station
max_station = data.loc[data['pollutant_avg'].idxmax()]
print("\nHighest AQI Station:")
print(max_station)

# 🔟 Query: Filter by CO Pollution
co_pollution = data[data['pollutant_id'] == 'CO']
print("\nCO Pollution Data:")
print(co_pollution)
