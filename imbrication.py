
print("Fera t'il froid durant cette journée ? (oui/non)")
temperature = input()

if temperature == "oui" :

    froid = True

elif temperature == "non" :

    froid = False

else :

    exit()


print("Pleuvera t'il ? (oui/non)")
pluvieux = input()

if pluvieux == "oui" :

    pleut = True

elif pluvieux == "non" :

    pleut = False

else :

    exit()


if froid :
    
    print("Il fait froid, vous prenez votre manteau..")

    if pleut :

        print("La pluie se met à tomber vous sortez donc votre parapluie")

    else :

        print("Les nuages s'annoncent tout de même bon, vous prenez alors votre casquette")

else :

    print("Le temps est agréable, vous prendrez une veste légère..")
    
    