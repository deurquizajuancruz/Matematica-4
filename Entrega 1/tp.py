import pandas as pd
from math import sqrt
from scipy.stats import t

df = pd.read_csv("titanic.csv")

x = df["SibSp"]
# x = df["Sex"].str.lower().map({"male": 0, "female": 1})
y = df["Survived"]

average_x: float = x.mean()
average_y: float = y.mean()
desviations_x: list = [element - average_x for element in x]
desviations_y: list = [element - average_y for element in y]
sum_desviations: float = 0
squared_desviations: float = 0

for i in range(len(desviations_x)):
    sum_desviations += desviations_x[i] * desviations_y[i]
    squared_desviations += pow(desviations_x[i], 2)

b1 = sum_desviations / squared_desviations
b0 = average_y - (b1 * average_x)
print(f"B0: {b0:.5f}")
print(f"B1: {b1:.5f}")

# ESTIMADOR YI:
print(f"^yi = {b1:.5f}x1 + {b0:.5f}")


# ESTIMADOR SIGMA CUADRADO:
def yi(x1):
    return b1 * x1 + b0


sum_sigma_squared: float = sum(pow(y[i] - yi(x[i]), 2) for i in range(len(y)))
sigma_squared: float = sum_sigma_squared / (len(y) - 2)
print(f"sigma squared: {sigma_squared:.5f}")

# ESTIMADOR R^2:
sct: float = sum((pow(element - average_y, 2) for element in y))
r2: float = 1 - (sum_sigma_squared / sct)
print(f"r^2: {r2:.5f}")

# ESTIMADOR r:
r: float = sqrt(r2)
if (b1 < 0):
    r = -r
print(f"r: {r:.5f}")

# IC(b1):
s: float = sqrt(sigma_squared)
sum_se: float = sum(pow(element - average_x, 2) for element in x)
sqrt_sum_se: float = sqrt(sum_se)
se: float = s / sqrt_sum_se
alpha: float = 0.05
t_value = t.ppf(1 - alpha / 2, df=len(y) - 2)
lower = b1 - t_value * se
upper = b1 + t_value * se

print(f"IC(95%) para b1: [{lower:.5f}, {upper:.5f}]")

# IC(b0):
se_b0: float = s * sqrt(1 / len(y) + (pow(average_x, 2) / sum_se))
lower_b0 = b0 - t_value * se_b0
upper_b0 = b0 + t_value * se_b0
print(f"IC(95%) para b0: [{lower_b0:.5f}, {upper_b0:.5f}]")

# ICM(Y):
lower_icm = yi(average_x) - t_value * s * sqrt(1 / len(y))
upper_icm = yi(average_x) + t_value * s * sqrt(1 / len(y))
print(f"ICM(95%) para Y con x={average_x:.5f}: [{lower_icm:.5f}, {upper_icm:.5f}]")

# IP(Y):
right_part: float = s * sqrt(1 + (1 / len(y)))
lower_ip = yi(average_x) - t_value * right_part
upper_ip = yi(average_x) + t_value * right_part
print(f"IP(95%) para Y con x={average_x:.5f}: [{lower_ip:.5f}, {upper_ip:.5f}]")
