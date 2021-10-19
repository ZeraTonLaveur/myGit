liste = ["lundi", "chaise", 78.65, "carton", "mardi", "mercredi", 14.27, 287, 
"jeudi", "xavier", "vendredi", "samedi", 789, "boîtier", "dimanche"]

anomalie = 0
listeAnomalie = []

print("Recherche d'anomalies...")
print("----------")

for name in liste :

    match name :   
        case "lundi":
            print("lundi")
        case "mardi":
            print("mardi")
        case "mercredi":
            print("mercredi")
        case "jeudi":
            print("jeudi")
        case "vendredi":
            print("vendredi")
        case "samedi":
            print("samedi")
        case "dimanche":
            print("dimanche")
        case _:
            print("Le jour :","<",name,">", "n'existe pas !")
            liste[liste.index(name)] = "error"
            listeAnomalie.append(name)
            anomalie += 1

listeCorretion = list(filter(("error").__ne__, liste))

print("----------")

if anomalie == 1 :

    print(anomalie," anomalie a été supprimée de la liste :")

elif anomalie > 1 :

    print(anomalie, "anomalies ont été supprimées de la liste :")

else :

    print("Aucunes anomalies détectées")

listeAnomalie = " / ".join(str(i) for i in listeAnomalie)

class couleurs:
    CORRECTE = '\033[92m'
    MAUVAIS = '\033[91m'
    BLANC = '\033[0m'
 
print(couleurs.MAUVAIS + listeAnomalie + couleurs.BLANC)

print("----------")

liste = " / ".join(str(i) for i in listeCorretion)

print("Tableau :")
print(couleurs.CORRECTE + liste + couleurs.BLANC)

print("----------")




