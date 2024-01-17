# Prasa lietotājam ievādīt savu vārdu un uzvārdu
vards = input("Lūdzu, ievadiet savu vārdu: ")
uzvards = input("Lūdzu, ievadiet savu uzvārdu: ")

# Veido teksta failu un ieraksta lietotāja vārdu un uzvārdu
with open("ziema.txt", "w") as faila_objekts:
    faila_objekts.write(vards + " " + uzvards)  