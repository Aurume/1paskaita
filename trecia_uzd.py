# upper() - didziosios
# casefold() -mazosios
# capitalize() - pirma didzioji
# count() - skaiciuoja kiek kartu kartojasi pasirinkta raide
# find() - iesko pasirinktos raides ir nurodo kur ja rasti

x = "Laba diena"
print(x.upper())
print(x.casefold())
print(x.capitalize())
print(x.count("a"))
print(x.find("d"))

print(x.title())  # visu zodziu pirmos raides didziosios
print(x.center(20))  # kiek simboliu i centra, mano nurodytam plote ras centra
print(x.isalpha())  # ar visi simboliai tik raides
print(x.isdigit())  # ar visi simboliai skaiciai
print(x.islower())  # ar visos tik mazosios raides
print(x.lstrip("Laba "))  # istrina pasirinktus simbolius is kaires
print(x.rjust(25))  # kiek tarpu i is kaires i desine pastumti
print(x.split())  # atskiria visu zodzius
print(x.splitlines())  # atskiria eilutes i sarasa, jeigu ju yra
print(x.swapcase())  # kur buvo mazosios raides, pakeicia i didziasias ir atvirksciai
