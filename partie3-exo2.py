import random

numbersList = [78, 35, 80, 43, 19, 46, 36]

n = int(input())

if n <= len(numbersList) :

    start = 0
    sum = 0

    while start < n :

        sum += numbersList[start]
        start += 1

    print("La somme des",n,"premiers nombres de la liste est égal à :",sum)

else :

    print("Vous ne pouvez pas choisir un nombre plus grand que la liste")

#--------------------------------------------------------------------------------

def PairOrNot(numberN) :

    pairOrNotPair = numberN % 2

    if pairOrNotPair == 0 :

        return True

    elif pairOrNotPair == 1 :

        return False

    else :

        return False
          
n = int(input())

start = 0
sum = 0

while start < n :

    isPair = PairOrNot(numbersList[start])

    if isPair :

        sum += numbersList[start]

    start += 1

print("La somme des premiers nombres pairs <= n de la liste est égal à :",sum)

#--------------------------------------------------------------------------------

n = int(input())

start = 0
isPairValidation = 0
sum = 0

while isPairValidation != n :

    isPair = PairOrNot(numbersList[start])

    if isPair :

        sum += numbersList[start]
        isPairValidation += 1
    
    start += 1

print("La somme des",n,"premiers nombres pairs de la liste est égal à :",sum)

#--------------------------------------------------------------------------------

numbersList = [4000, 8750, 605, 312, 895, 789, 6412, 1450, 2145, 7200, 3405]

none = input()

sum = 0
n = 0

while sum < 15000 :

    sum += numbersList[n]
    n += 1

    if sum >= 15000 :

        sum -= numbersList[n-1]
        n -= 1
        break

print("Le plus grand < n > est de :",n,"pour une somme de :",sum,"/ 15000")

#--------------------------------------------------------------------------------

none = input()

n = 0

def factorielle(n):
  
        global somme

        somme = 1

        for f in range(1,n+1):

            somme = somme * f

        return somme


while factorielle(n) < 15000 :

    n += 1
    print(somme)

    if somme >= 15000 :

        somme -= factorielle(n-1)
        print(somme)

#--------------------------------------------------------------------------------

start = 0
n1 = 75
n2 = 25
r = n1

while start < n2 :

    start += 1
    n1 += 1

print(f"{r} + {n2} = {n1}")

#--------------------------------------------------------------------------------

start = 0
n1 = 2
n2 = 17
r = n2

while start < n2 :

    start += 1
    r = r + n1

    if start == n2 :

        r -= n2
    
print(f"{n1} * {n2} = {r}")

#--------------------------------------------------------------------------------

def supprimeDoublon(myListe) :

    myListe = list(set(myListe))

    return myListe
    
liste = ["lundi", "mardi", "mercredi", "lundi"]

print(supprimeDoublon(liste))

#--------------------------------------------------------------------------------

liste = [3,4,5,3,4,5,1]

secondList = [] 

for number in liste : 

    if number not in secondList : 
        
        secondList.append(number) 

print(secondList)

#--------------------------------------------------------------------------------

liste = [27, 3339, 2345, 666]

for number in liste :
    
    multipleDeNeuf = number % 9

    if multipleDeNeuf == 0 :

        print(number, "est un multiple de 9")
        y = number / 9
        print(y)

    elif multipleDeNeuf != 0 :

        print(number, "n'est pas un multiple de 9")
        y = number - 9
        print(y)

    else :
        print(number, "n'est pas identifié")
        print(y)

#--------------------------------------------------------------------------------

stock = ["Ordinateur de bureau", "Ordinateur portable", 100, "Caméra", 310.28, "Haut-parleurs",
27.00, "Télévision", 1000, "Cartes mères", "souris", "clavier", 500, "barettes de mémoire"]

intStock = []
stringStock = []

for element in stock :

    if isinstance(element, (int, float)) :

        intStock.append(element)

    elif isinstance(element, (str)) :

        stringStock.append(element)

    else :

        print("error")

print(intStock)
print(stringStock)

#--------------------------------------------------------------------------------

eleve = ["Romuald", "Alexandre", "Adrian", "Leo", "Bastien", "Clément"]

randomNumber = random.randint(0,5)

print("L'élève tiré au sort est :",eleve[randomNumber])


    


