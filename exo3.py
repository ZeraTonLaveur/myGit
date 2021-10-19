#Exercice 1

#1)

print("Veuillez entrer le prénom << Jean >>")
prenom = str(input())

print("Bonjour",prenom, "!")

#2)

print("Quel est ton année de naissance ?")
naissance = int(input())
age = 2021 - naissance

print("Vous avez :",age, "an(s)")

#Exercice 2

listeSemaine = []
listeSemaine.append("Lundi")
listeSemaine.append("Mardi")
listeSemaine.append("Mercredi")
listeSemaine.append("jeudi")
listeSemaine.append("Vendredi")
listeSemaine.append("Samedi")
listeSemaine.append("Dimanche")

#1)
 
print(listeSemaine)

#2)

print(listeSemaine[4])

#3)

listeSemaine.reverse()

#Exercice 3

stock1 = ["Ordinateur de bureau", "Ordinateur portable", 100, "Caméra", 310.28, "Haut-parleurs",
27.00, "Télévision", 1000, "Cartes mères", "souris", "clavier", 500, "barettes de mémoire"]

stock2 = [1000, 500, 310.28, 100, 27.00]

stock3 = ["Ordinateur de bureau", "Ordinateur portable", "Caméra", "Haut-parleurs", "Télévision", 
"Cartes mères", "souris", "clavier", "barettes de mémoire"]

print(len(stock2))
print(len(stock3))

stock3.sort(key=len)
print(stock3)

stock3.reverse()
print(stock3)

stock2.sort()
print(stock2)

stock2.reverse()
print(stock2)

#Exercice 4

numlist = [1, 2, 3, 4, 5]

alphaList = ["a", "b", "c", "d", "e"]

print(numlist is alphaList) #faux

print(numlist == alphaList) #faux

numlist = alphaList

print(numlist is alphaList) #Vrai

print(numlist == alphaList) #Vrai

#Exercice 5
print('--------------------------------')

liste = [17, 38, 10, 25, 72]

liste.sort()
print(liste)

liste.append(12)
print(liste)

liste.reverse()
print(liste)

print(liste.index(17))

liste.remove(38)
print(liste)

print(liste[1:3])

print(liste[:2])

print(liste[-3:])

print(liste[-1:])

stringListe = ":".join(str(i) for i in liste)

print(stringListe)

stringListe += ":175"

print(stringListe)

liste = stringListe.split(":")

print(liste)




