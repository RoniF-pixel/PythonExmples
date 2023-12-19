"""creating a linear egression model"""
import numpy as np
from sklearn.linear_model import LinearRegression

#to make the array a two dimensional array we use reshape
x = np.array([1,0,2,0,3,1,0,1,2,0]).reshape((-1, 1))
y = np.array([16,9,17,12,22,13,8,15,19,11])
#creating a model
model = LinearRegression()
model.fit(x, y)
#obtaining the coefficient of determination,𝑅²
r_sq = model.score(x, y)
print(f"coefficient of determination: {r_sq}")
#.intercept representing the coefficient 𝑏₀, and .coef representing 𝑏₁
print(f"intercept: {model.intercept_}")
print(f"slope: {model.coef_}")
#obtaining the predicted response
y_pred = model.predict(x)
print(f"predicted response:\n{y_pred}")