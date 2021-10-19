print("Bienvenue à l'attraction !")
print("Pour pouvoir monter dans le manège merci d'indiquer")
print("--------------------")

tailleReglementaire = 160
poidsReglementaire = 40
poidsReglementaireTrain = 20

print("- Votre taille (centimètres) :")
taille = int(input()) 

print("- Votre poids (kilos) :")
poids = int(input())

if poids > poidsReglementaire and taille > tailleReglementaire :

    print("Vous pouvez monter dans le manège !")

else :

    print("Vous ne suivez pas les normes :")
    print("- Taille minimum :" ,tailleReglementaire, " centimètres")
    print("- Poids minimum :" ,poidsReglementaire, " kilos")

if poids < poidsReglementaire or taille < tailleReglementaire and poids > poidsReglementaireTrain :

    print("Vous pouvez tout de même faire l'attraction du petit train si vous le souhaitez ")
    print("- Taille minimum : aucunes")
    print("- Poids minimum : ",poidsReglementaireTrain,)




