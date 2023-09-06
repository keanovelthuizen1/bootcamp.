#les7_opdracht5

geld = 10000
rente = 1.028
jaaren = float (input("hoeveel jaar zit je geld al in de bank? "))

totaalgeld =  geld*rente**jaaren

print(f'10000 euro met 2.8% rente elk jaar voor {jaaren} jaar is {totaalgeld} euro')