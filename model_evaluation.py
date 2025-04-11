#Model evaluation 
import pandas as pd
from sklearn.metrics import mean_squared_error, r2_score
import joblib

# Load original CSV file
data = pd.read_csv("air_quality.csv")

# Missing values 
data.ffill(inplace=True)    # Updated line

# Load Model
model = joblib.load('air_quality_model.pkl')

# Prediction
X = data[['pollutant_min', 'pollutant_max']]
y = data['pollutant_avg']

y_pred = model.predict(X)

# Evaluation
mse = mean_squared_error(y, y_pred)
r2 = r2_score(y, y_pred)

print(f"Mean Squared Error: {mse}")
print(f"R2 Score: {r2}")
