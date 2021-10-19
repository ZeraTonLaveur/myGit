

def account():
    
    global username
    global password
    global confirmPassword

    print('Création de votre compte :')
    print('----------------------')

    print('Entrez un username :')
    username = input()

    print('Entrez votre mot de passe :')
    password = input()

    print ('Confirmez votre mot de passe :')
    confirmPassword = input()

account()

while password != confirmPassword :

    print('Vos mots de passe ne sont pas identiques')
    print('Merci de réessayer !')
    print('----------------------')
    account()

print('Votre compte a été crée avec succès !')
print('----------------------')
print('Bienvenue ',username,)
print('Votre mot de passe actuel :' ,password,)
print('----------------------')

def menu():

    print('Que voulez vous faire ?')
    print('----------------------')
    print('1. Quitter le compte')
    print('----------------------')

    choix = input()
    
    match choix:
        case "1":
            exit()
        case _:
            menu() 
menu()




    
    
    

    
    











