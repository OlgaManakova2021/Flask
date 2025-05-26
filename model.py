import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle

salary = [50000, 55000, 78000, 80000, 82000, 84000, 89000, 90000, 91000, 96000, 99000, 110000]
experince = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
print(len(salary), len(experince))

X = np.array(experince).reshape(-1,1)
y = np.array(salary)

X_train, X_test, y_train, y_test = train_test_split(X, y,
                                                    test_size=0.2,
                                                    random_state=42)

lr = LinearRegression()
lr.fit(X_train, y_train)
y_pred = lr.predict(X_test)

with open('lr_model.pkl', 'wb') as f:
    pickle.dump(lr, f)
