print("Welcome sur le tip calculator")
somme = int(input("Quelle somme souhaitez-vous partager? \nCFA"))
pourcent = int(input("Combien de pourcent souhaitez-vous distribuer? 10, 20 ou 30% \n"))
personne = int(input(f"A combien de personnes souhaitez-vous le distribuer les {somme} CFA? \n"))

pourcentage = (pourcent / 100) + somme

total = round(pourcentage / personne, 2)
print(f"Chacunes des {personne} personnes reçevra {total}CFA")


