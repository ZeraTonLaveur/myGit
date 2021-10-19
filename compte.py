username = None
password = None
age = None
confirmPassword = None
film  = False

easySecurityPassword = 4
mediumSecurityPassword = 8
highSecurityPassword = 12
degresProtection = None

def accountInformation():

    print("Information de votre compte :")
    print("--------------------")
    print("Prénom : ",username)
    print("Age : ",age)
    print("Mot de passe :",password, "// Degrès de protection : ",degresProtection)
    print("--------------------")

def orderFilm():

    if film :

        print("Votre film est commandé")
    
    else :

        print("Il faut être majeur pour pouvoir commander un film")

#---Start process---

print("Création de votre compte")
print("--------------------")

print("Choisissez un prénom :")
username = str(input())

print("Choisissez un age :")
age = int(input())

if age >= 18 :

    film = True

else :

    film = False

print("Choisissez un mot de passe :")
password = str(input())

print("Confirmez votre mot de passe :")
confirmPassword = str(input())


while password != confirmPassword :

    print("Vos mots de passe ne sont pas identiques merci de réessayer !")

    print("Choisissez un mot de passe :")
    password = str(input())

    print("Confirmez votre mot de passe :")
    confirmPassword = str(input())

else :

    print("Votre compte a été crée avec succès !")

    if len(password) <= easySecurityPassword :

        degresProtection = "faible"
    
    elif len(password) > easySecurityPassword and len(password) <= mediumSecurityPassword :

        degresProtection = "moyen"

    elif len(password) > mediumSecurityPassword and len(password) <= highSecurityPassword :

        degresProtection = "élevé"

    else :

        degresProtection = "INCREDIBLE"


    accountInformation()

def menu():

    print("Que voulez-vous faire ?")
    print("--------------------")
    print("1. Commander un film")
    print("--------------------")

    myChoice = str(input())

    match myChoice:
        case "1":
            orderFilm()
        case _:
            menu()

menu()

