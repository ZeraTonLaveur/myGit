#7

d = {'nom':'Dupuis','prenom':'Jacque','age': 30}

d.update({'prenom':'Jacques'})
print(d)
print(d.keys())
print(d.values())

print(d['prenom'] ,d['nom'] ,"a" ,d['age'] ,"ans" )

#8

def semaine(jourDeLaSemaine) :

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
    

print("Choisir un jour de la semaine (lundi/mercredi/vendredi/samedi/dimanche)")
jourDeLaSemaine = str(input())
semaine(jourDeLaSemaine)

#9

def nombre(number) :

    if number > 0 :

        print("Le nombre est positif")

    elif number < 0 :

        print("Le nombre est négatif")

    else :

        print("Le nombre est nul")

    
print("Choisissez un nombre :")
number = int(input())
nombre(number)