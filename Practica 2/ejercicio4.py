x_numbers: list = [2, 3, 5, 9, 10, 16, 19, 20, 24, 27, 32, 41, 55, 60]
y_numbers: list = [
    100,
    200,
    250,
    400,
    500,
    850,
    930,
    900,
    1300,
    1360,
    1500,
    2050,
    2800,
    2900,
]

x_average = sum(x_numbers) / len(x_numbers)
y_average = sum(y_numbers) / len(y_numbers)

sum: int = 0
divider: int = 0
for i in range(0, len(x_numbers)):
    x_difference = x_numbers[i] - x_average
    sum += x_difference * (y_numbers[i] - y_average)
    divider += pow(x_difference, 2)

b1 = sum / divider
b0 = y_average - (b1 * x_average)

print("INCISO A:")
print(f"b1: {round(b1,2)}")
print(f"b0: {round(b0,2)}")

print("INCISO B:")
print(f"El valor promedio del ingreso fijo es: {round(b0,2)}")

print("INCISO C:")
print(f"El aumento promedio del ingreso por día de elaboración es: {round(b1,2)}")
