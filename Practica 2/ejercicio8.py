from math import sqrt
from scipy import stats


x_numbers: list = [3, 4, 4, 7, 7, 8, 9, 11, 12, 12, 14, 16, 17, 20, 23, 25]
y_numbers: list = [25, 32, 26, 38, 34, 41, 39, 46, 44, 51, 53, 58, 61, 64, 66, 70]

x_average: float = sum(x_numbers) / len(x_numbers)
y_average: float = sum(y_numbers) / len(y_numbers)

total_sum: float = 0
divider: float = 0
for i in range(0, len(x_numbers)):
    x_difference: float = x_numbers[i] - x_average
    total_sum += x_difference * (y_numbers[i] - y_average)
    divider += pow(x_difference, 2)

b1: float = total_sum / divider
b0: float = y_average - (b1 * x_average)

print("INCISO A:")
print(f"{round(b1*24 + b0, 2)}")

sse_sum: float = 0
for i in range(0, len(x_numbers)):
    yi: float = b0 + (b1 * x_numbers[i])
    sse_sum += pow(y_numbers[i] - yi, 2)

alpha: float = 0.05
n: int = len(x_numbers) - 2
t_value = stats.t.ppf(1 - alpha / 2, n)
o2: float = sse_sum / n
value_15: float = b0 + (b1 * 15)
square: float = (1 / (n + 2)) + (pow(15 - x_average, 2) / divider)
se15: float = sqrt(o2 * square)
lower = value_15 - t_value * se15
upper = value_15 + t_value * se15

print("INCISO B:")
print(
    f"Con un 95% de confianza, el tiempo promedio de entrega para todos los autos que tienen 15 opciones está entre {lower} y {upper} días."
)

sb1: float = sqrt(o2 * (1 / divider))
t_stat: float = b1 / sb1
t_crit = stats.t.ppf(1 - alpha / 2, n)
print("INCISO C:")
if abs(t_stat) > t_crit:
    print("Hay relación significativa entre x e y")
else:
    print("No hay relación significativa entre x e y")
