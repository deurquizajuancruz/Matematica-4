x_numbers: list = [100, 110, 120, 150, 190, 200, 225, 265, 280, 300]
y_numbers: list = [52, 75, 62, 61, 84, 98, 110, 94, 100, 135]

x_average = sum(x_numbers) / len(x_numbers)
y_average = sum(y_numbers) / len(y_numbers)

total_sum = 0
divider = 0
for i in range(0, len(x_numbers)):
    x_difference = x_numbers[i] - x_average
    total_sum += (x_difference) * (y_numbers[i] - y_average)
    divider += pow(x_difference, 2)

b1 = total_sum / divider
b0 = y_average - (b1 * x_average)

print("INCISO A:")
print(f"b1: {round(b1,2)}")
print(f"b0: {round(b0,2)}")

print("INCISO B:")
print(f"Cuando x = 170: {round(b0 + (b1*170))}")

print("INCISO C:")
print("No, ya que solo se tienen datos desde 100 a 300 y 500 > 300")

print("INCISO D:")
print(f"Aumenta {round(b1,2)} milisegundos / bytes")