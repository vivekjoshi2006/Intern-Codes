import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

data = pd.read_csv(r"D:\house_data.csv")       
print("\nDataset Loaded Successfully\n")   
data.fillna(data.mean(numeric_only=True), inplace=True)   
data = pd.get_dummies(data, drop_first=True)               

X, y = data.drop("price", axis=1), data["price"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression().fit(X_train, y_train)
print("Model Trained Successfully\n")

y_pred = model.predict(X_test)
print("MAE :", mean_absolute_error(y_test, y_pred))
print("RMSE:", np.sqrt(mean_squared_error(y_test, y_pred)))
print("R²  :", r2_score(y_test, y_pred))

plt.scatter(y_test, y_pred)
plt.xlabel("Actual House Prices"); plt.ylabel("Predicted House Prices")
plt.title("Actual vs Predicted House Prices")
plt.show()

print("\nSample Prediction:", model.predict(X.iloc[[0]])[0])