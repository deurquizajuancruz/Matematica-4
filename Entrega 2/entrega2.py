r: int = 187
d: int = 23
decipher: list = [135, 146, 171, 106, 70, 147, 70, 106, 146, 0, 115, 98, 115, 1, 171]
letters: str = " abcdefghijklmnopqrstuvwxyz"
mapping: dict = {i: letters[i] for i in range(len(letters))}
result: str = ""
for number in decipher:
    c_powered: int = pow(number, d)
    m: int = c_powered % r
    result += mapping[m]

print(result)
