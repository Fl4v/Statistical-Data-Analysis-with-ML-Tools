from preprocessing import data
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pandas as pd

linear_regression = LinearRegression()
stellar_data = data('q1_q16_stellar_clean.csv')

mass_median = stellar_data['mass'].median()
stellar_temperature_median = stellar_data['stellar_temperature'].median()

stellar_data['mass'].fillna(mass_median, inplace=True)
stellar_data['stellar_temperature'].fillna(stellar_temperature_median, inplace=True)

X = stellar_data['mass'].values.reshape(-1, 1)
y = stellar_data['stellar_temperature'].values.reshape(-1,1)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

stellar_data_regression = linear_regression.fit(X_train, y_train)

y_pred = stellar_data_regression.predict(X_test)

actual_v_predicted = pd.DataFrame({'Actual': y_test.flatten(), 'Predicted': y_pred.flatten()})
print(actual_v_predicted)
