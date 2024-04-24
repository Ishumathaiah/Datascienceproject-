housing_data = pd.read_csv("housing_data.csv"

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

X = housing_data.drop("price", axis=1)
y = housing_data["price"
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


model = RandomForestRegressor()


model.fit(X_train, y_train)
 mean_squared_error
y_pred = model.predict(X_test)


mse = mean_squared_error(y_test, y_pred)
print("Mean Squared Error:", mse)
