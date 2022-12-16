# Kad leistų įvesti skaičių
# Išvesti į ekraną „Skaičius yra lyginis“, jei taip yra
# Išvesti į ekraną „Skaičius yra nelyginis“, jei taip yra
# Išvesti į ekraną „Skaičius dalinasi iš 3“, jei skaičius dalinasi iš trijų

sk = int(input("Įveskite skaičių: "))
if sk % 2 == 0:
    print("Skaičius yra lyginis")
if sk % 2 != 0:
    print("Skaičius yra nelyginis ")
if sk % 3 == 0:
    print("Skaičius dalinasi iš trijų")
