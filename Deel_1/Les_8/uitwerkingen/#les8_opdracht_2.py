#les8_opdracht_2

cijfer = int(input("Voer het cijfer in: "))

# Definieer de omschrijving na de controle van het cijfer.
if cijfer == 10:
    omschrijving = "uitmuntend"
elif cijfer == 9:
    omschrijving = "zeer goed"
elif cijfer == 8:
    omschrijving = "goed"
elif cijfer == 7:
    omschrijving = "ruim voldoende"
elif cijfer == 6:
    omschrijving = "voldoende"
elif cijfer == 5:
    omschrijving = "bijna voldoende"
elif cijfer == 4:
    omschrijving = "onvoldoende"
elif cijfer == 3:
    omschrijving = "gering"
elif cijfer == 2:
    omschrijving = "slecht"
elif cijfer == 1:
    omschrijving = "zeer slecht"

if 1 <= cijfer <= 10:

 if cijfer >= 6:
        print(f"Gefeliciteerd, {cijfer} is {omschrijving}.")
 else:
        print(f"Jammer, {cijfer} is {omschrijving}.")
else:
    print("Dit kan ik niet omzetten!")
