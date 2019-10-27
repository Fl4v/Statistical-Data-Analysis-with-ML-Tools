from preprocessing import data
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import numpy as np
import pandas as pd

# Load linear regression model
linear_regression = LinearRegression()

# Attach data to variable
stellar_data = data('q1_q16_stellar_clean.csv')

# Calculate the median for each attribute and replace n/a with the latter
mass_median = stellar_data['mass'].median()
stellar_temperature_median = stellar_data['stellar_temperature'].median()

# Set X and y
stellar_data['mass'].fillna(mass_median, inplace=True)
stellar_data['stellar_temperature'].fillna(stellar_temperature_median, inplace=True)

X = stellar_data['mass'].values.reshape(-1, 1)
y = stellar_data['stellar_temperature'].values.reshape(-1,1)

# Split the dataset for training and testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the algorithm
stellar_data_regression = linear_regression.fit(X_train, y_train)

# Predict y using the training dataset set aside for this purpose
y_pred = stellar_data_regression.predict(X_test)

# Compare side by side actual vs predicted values
actual_v_predicted = pd.DataFrame({'Actual': y_test.flatten(), 'Predicted': y_pred.flatten()})
print(actual_v_predicted)

# Calculate mean squared error
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
print(rmse)
