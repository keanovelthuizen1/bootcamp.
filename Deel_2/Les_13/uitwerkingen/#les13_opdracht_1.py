#les13_opdracht_1

kleuren = ("rood", "blauw", "groen", "geel", "paars")

naam = input("Wat is jouw naam? ")

favoriete_kleur = input("Wat is jouw favoriete kleur? ")

if favoriete_kleur in kleuren:
    verhaal = f"{naam}, jouw favoriete kleur is {favoriete_kleur}. Dat is een geweldige keuze!"
    print(verhaal)
else:
    print("Deze kleur is niet zo geweldig!")
