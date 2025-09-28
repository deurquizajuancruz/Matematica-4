def f(x, y):
    return pow(x, 2) * y


def fx(x):
    return 2 * x * y


def fy(y):
    return pow(x,2)


x: int = 10
y: int = 2
iterations: int = 0
tolerance: float = 0.0001
step: float = 0.4
difference: float = 100
while difference > tolerance:
    iterations += 1
    old_function: float = f(x, y)
    x: float = x - step * fx(x)
    y: float = y - step * fy(y)
    difference = abs(f(x, y) - old_function)

print(x)
print(y)
print(iterations)
