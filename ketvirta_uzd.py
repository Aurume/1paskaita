# Leistų įvesti pirmą skaičių
# Leistų įvesti antrą skaičių
# Paklaustų, kokį matematinį veiksmą reiktų atliktų
# Atspausdintų rezultatą: pasirinktų skaičių suma, daugybą ar pan.

a = int(input("Pirmas skaičius: "))
b = int(input("Antras skaičius: "))

zenklas = input("Kokį veiksmą atlikti? ")

if zenklas == "*":
    print(a * b)
if zenklas == "+":
    print(a + b)
if zenklas == "-":
    print(a - b)
if zenklas == "/":
    print(a / b)
