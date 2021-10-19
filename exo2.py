liste1 = ["français", "anglais", "espagnol"]
liste2 = ["pomme", "fraise"]

liste1 = liste2[:]

liste2.append("triangle")
#liste2.remove("")

print(liste1)
print(liste2)

liste2[1] = "O"
print(liste2)

del liste2[0]
print(liste2)

string = " ___ ".join(liste2)
print(string)

liste2 = string.split(":")
print(liste2)



            
            
           




 



