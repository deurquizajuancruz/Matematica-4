import numpy as np
import pandas as pd

df = pd.read_csv("titanic.csv")
df = df.dropna(subset=["Age"])
y = df["Survived"]
df["Sex"] = df["Sex"].str.lower().map({"male": 0, "female": 1})
df["const"] = 1
X = df[["Pclass", "Age", "SibSp", "Parch", "Fare", "Sex", "const"]]
amount_variables = len(X.columns)

x = np.array(X)
y = np.array(y)

xT = x.T
product = xT @ X
inverse = np.linalg.inv(product)
beta_hat = inverse @ xT @ y

print("Estimadores B:")
names = ["Pclass", "Age", "SibSp", "Parch", "Fare", "Sex"]
for i in range(amount_variables - 1):
    print(f"Estimador de {names[i]}: {beta_hat[i]:.5f}")

b0 = beta_hat[len(beta_hat) - 1]
print(f"B0: {b0:.5f}")

print("Ecuacion de regresion:")
coeffs = " + ".join(f"{beta_hat[j]:.4f} X_{j+1}" for j in range(amount_variables - 1))
print(f"y = {b0:.4f} + {coeffs}")


def yi_hat(array_x):
    return sum(beta_hat[i] * array_x[i] for i in range(len(beta_hat)))


average_y = y.mean()

sst: float = sum(pow(y[i] - average_y, 2) for i in range(len(y)))
sse: float = sum(pow(y[i] - yi_hat(x[i]), 2) for i in range(len(y)))
r2: float = 1 - (sse / sst)

print(f"R^2: {r2}")
