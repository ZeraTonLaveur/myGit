def number(myNumber) :

    if myNumber > 0 :

        print("Le nombre est positif")

    elif myNumber < 0 :

        print("Le nombre est négatif")

    else :

        print("Le nombre est nul")

def pairOrNotPair(myNumber) :

    pairOuImpair = myNumber % 2

    if pairOuImpair == 0 :
    
        print("Le nombre est pair")

    elif pairOuImpair == 1 :

        print("Le nombre est impair")

def twoFunction(myNumber) :

    number(myNumber)
    pairOrNotPair(myNumber)