class Account :
    def __init__(self, username, password, balance, key, status="unknow") : 
        self.username = username
        self.password = password
        self.balance = balance
        self.key = key
        self.status = status
    
        if key == 1 :
            
            self.status = "VIP"
        
        else :

            self.status = "normal"

def accountInformation() :
    print("--------------------")
    print("Nom :" ,myAccount.username)
    print("Mot de passe :" ,myAccount.password)
    print("Solde :" ,myAccount.balance ,"€")
    print("Statut client :" ,myAccount.status)
    print("--------------------")

def withdrawMoney() :
    
    withdrawMyMoney = -1

    while withdrawMyMoney <= 0 or withdrawMyMoney > 1000 or withdrawMyMoney > myAccount.balance :

        print("Combien d'argent voulez-vous retirer ? (1 à 1000)")
        print("Votre solde :", myAccount.balance, "€")
        withdrawMyMoney = int(input())

    myAccount.balance -= withdrawMyMoney

    print(withdrawMyMoney, "€ on été retiré de votre compte")
    print("Solde mis à jour :", myAccount.balance, "€")

def depositMoney() :

    depositMyMoney = -1

    while depositMyMoney <= 0 or depositMyMoney > 1000 :

        print("Combien d'argent voulez-vous déposer ? (1 à 1000)")
        print("Votre solde :", myAccount.balance, "€")
        depositMyMoney = int(input())

    myAccount.balance += depositMyMoney

    print(depositMyMoney, "€ on été ajouté sur votre compte")
    print("Solde mis à jour :", myAccount.balance, "€")

def menu() :

    print("Quelle action voulez-vous effectuer ?")
    print("--------------------")
    print("1. Information du compte")
    print("2. Déposer de l'argent")
    print("3. Retirer de l'argent")
    print("4. Se déconnecter du compte")
    print("--------------------")

    choix = input()

    match choix :
        case "1":
            accountInformation()
        case "2":
            depositMoney()
        case "3":
            withdrawMoney()
        case "4":
            exit(0)
        case _:
            menu()

    menu()

def keyActivation() :

    global key
    mykey = False
    keyForVIP = "AEMD-4562"

    while mykey == False :

        print("Avez-vous une clef d'activation pour un compte premium ?")
        print("1. oui")
        print("2. non")

        choix = input()

        if choix == "1" :

            codeActivation = "unknow"

            while codeActivation != keyForVIP :

                print("Veuillez entrer un code d'activation")
                print("1. Annuler l'opération")

                codeActivation = str(input())

                if codeActivation == "1" :

                    mykey = True
                    key = 0
                    break

                elif codeActivation == keyForVIP :

                    print("Code valide...")

                    mykey = True
                    key = 1
                    break
        
        elif choix == "2" :

            mykey = True
            key = 0

        else :

            mykey = False

#-----------------------------------------------------------------------

print("Nous allons débuter la création de votre compte")
print("--------------------")

print("Choisissez un nom :")
myUsername = str(input())

print("Choisissez un mot de passe :")
myPassword = str(input())

myBalance = 0

keyActivation()

myAccount = Account(myUsername, myPassword, myBalance, key)

print("Votre compte a été crée avec succes :")

menu()





