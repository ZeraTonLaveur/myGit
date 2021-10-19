#Lire un nombre, écrire s'il est positif, négatif ou nul

number_1 = 24

if number_1 > 0 :

    print("Le nombre est positif")

elif number_1 < 0 :

    print("Le nombre est négatif")

else :

    print("Le nombre est nul")

    
#Lire un nombre, écrire s'il est pair ou impair

number_2 = 56
pairOuImpair = number_2 % 2

if pairOuImpair == 0 :
    
    print("Le nombre est pair")

elif pairOuImpair == 1 :

    print("Le nombre est impair")

#Lire deux nombres, retourner le plus petit des deux

nombre_3 = 123
nombre_4 = 78

if nombre_3 > nombre_4 :

    print("Le plus petit nombre est : ",nombre_4)

else :

    print("Le plus petit nombre est : " ,nombre_3)

#Lire trois nombres, retourner le plus petit et le plus grand

nombre_5 = 8468
nombre_6 = 789
nombre_7 = 248

if nombre_5 > nombre_6 and nombre_5 > nombre_7 :

    print("Le plus gros chiffres est : ", nombre_5)

    if nombre_6 < nombre_7 :

        print("Le plus petit chiffre est : ", nombre_6)
    
    else :

        print("Le plus petit chiffre est : ", nombre_7)

elif nombre_6 > nombre_5 and nombre_6 > nombre_7 :

    print("Le plus gros chiffre est : ", nombre_6)

    if nombre_5 < nombre_7 :

        print("Le plus petit chiffre est : ", nombre_5)

    else :

        print("Le plus petit chiffre est : ", nombre_7)

elif nombre_7 > nombre_5 and nombre_7 > nombre_6 :

    print("Le plus gros chiffre est : ", nombre_7)

    if nombre_5 < nombre_7 :

        print("Le plus petit chiffre est : ", nombre_5)

    else :

        print("Le plus petit chiffre est : ",nombre_7)

else :

    print("Rien")

#Lire un jour de la semaine, 
# si c'est lundi écrire <<c'est reparti!>>, 
# si c'est mercredi écrire <<jour des enfants>>
# si c'est vendredi écrire <<bientôt le week-end>>
# si c'est samedi ou dimanche écrire <<bon week-end>>
# sinon écrire <<bonne semaine>>

print("Choisir un jour de la semaine (lundi/mercredi/vendredi/samedi/dimanche)")
jourDeLaSemaine = input()

if jourDeLaSemaine == "lundi" :

    print("C'est reparti !")

elif jourDeLaSemaine == "mercredi" : 

    print("Jour des enfants")

elif jourDeLaSemaine == "vendredi" :

    print("Bientôt le week-end")

elif jourDeLaSemaine == "samedi" or jourDeLaSemaine == "dimanche" :

    print("Bon week-end !")

else :

    print("Bonne semaine")

#Lire une couleur,
# si c'est rouge magenta, bleu cyan ou jaune, écrire <<couleur primaires>>
# si c'est orange, violet ou vert, écrire <<couleurs secondaires>>
# sinon écrire <<autres couleurs>>

print("Choisir une couleur (rouge magenta/bleu cyan/jaune/orange/violet/vert/autre)")
maCouleur = input()

if maCouleur == "rouge magenta" or maCouleur == "bleu cyan" or maCouleur == "jaune" :

    print("C'est une couleur primaire")

elif maCouleur == "orange" or maCouleur == "violet" or maCouleur == "vert" :

    print("C'est une couleur secondaire")

else :

    print("Pas connu du registre :/")

# Exercice 6 :

print("Choisissez un nombre x (27/3339/2345/666)")
y = None
x = int(input())
multipleDeNeuf = x % 9
print(multipleDeNeuf)

if multipleDeNeuf == 0 :

    y = x / 9
    print(y)

elif multipleDeNeuf != 0 :

    y = x - 9
    print(y)

else :

    print(y)

# 1)

# Pour 27 : 3.0
# Pour 3339 : 371.0
# Pour 2345 : 2336
# Pour 666 : 74.0

# 2) 

# Si le chiffre est un multiple de 9 alors il sera divisé par 9 
# sinon le chiffre sera soustrait de 9

# Exercice 7 :

prixLocation = 700
forfaitSki = 210
forfaitSkiGroupe = 170
montantTotal = 0

print("Combien êtes-vous à partir au ski ?")
nombreDePersonne = int(input())

if nombreDePersonne >= 5 :

    montantTotal = prixLocation + forfaitSkiGroupe * nombreDePersonne
    print("Chalet pour la semaine : ",prixLocation,"€")
    print("Groupe de ",nombreDePersonne, "personnes : ",forfaitSkiGroupe * nombreDePersonne,"€ //Tarif réduit (170€)")
    print("--------------------")
    print("Le montant s'élèvera à " ,montantTotal, "€")
    
elif nombreDePersonne < 5 :

    montantTotal = prixLocation + forfaitSki * nombreDePersonne
    print("Chalet pour la semaine : ",prixLocation,"€")
    print("Groupe de ",nombreDePersonne, "personne(s) : ",forfaitSki * nombreDePersonne,"€ //Tarif plein (210€)")
    print("--------------------")
    print("Le montant s'élèvera à ",montantTotal, "€")

else :

    print(montantTotal)

#3 Si le groupe de personne est de 5 ou plus alors ils auront un tarif réduit sur leur forfait de ski 
# sinon si le groupe est inférieur à 5 alors ils devront payer tarif plein

# Exercice 8 :
 
 # 1)
 
 #  Si on saisit oui en entrée , nous auront "oui" en sortie, pareil pour "non"

# 3)

 # Le programme nous demande de saisir soit "oui" ou soit "non" et retourne ce que
 # nous avons entrée, et si nous ne retournons pas un des deux choix alors il nous
 # dira que la réponse est mauvaise (car il attend "oui" ou "non" en entrée)
 # Si la réponse fait 3 caractères, il le précisera

reponse = input("Répondre (oui / non)")


if reponse == "oui" or reponse == "non" :

    print("La réponse est : ",reponse)

else :

    print("C'est une mauvaise réponse")

    if len(reponse) == 3 :

        print("La réponse fait 3 caractères")

        






