first_loop = "Hello World !"
second_loop = ["one", "two", "three"]
third_loop = {"prenom":"louis", "nom":"birand", "age": 50}

for f in first_loop :

    print(f)

    if f == "W" :
        first_loop += "ERROR"
        print(first_loop)

for g in second_loop :

    print(g)

for h in third_loop.items() : #items() #values() #keys()

    print(h)

for i in range(0,50) :

    print(i)

print("--------------------------")

first = "PREMIER"
second = ["1", "2", "3", "4", "5", "6", 7]

for f in first :

    for s in second :

        text = str(f) + str(s)
        print(text)