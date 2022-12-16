# Leistų įvesti skaičius a ir b (int arba float)

a = int(input("Įveskite skaičių: "))
b = float(input("Įveskite antrą skaičių: "))

# Išvestų į ekraną „a mažesnis už b“, jei taip yra
# Išvestų į ekraną „a lygu b“, jei taip yra
# Išvestų į ekraną „a didesnis už b“, jei taip yra

if a < b:
    print("a mažesnis už b")
elif a == b:
    print("a lygu b")
elif a > b:
    print("a didesnis už b")
