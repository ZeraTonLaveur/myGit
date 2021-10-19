n = int(input())
s = 0

for num in range(0, n+1) :

    s = s + num

print(s)

#--------------------------

n = int(input())
s = 0

for num in range(0, n+1) :

    pairOrNotPair = num % 2
    
    if pairOrNotPair == 0 and num <= n :

        s = s + num
   
print(s)

#--------------------------

n = int(input())
r = n
s = 0

for num in range(0, n) :

    pairOrNotPair = num % 2

    if pairOrNotPair == 0 :

        n = n + 1

n = n - r

print(n)

#--------------------------

n = 0
s = 0

while s < 15000 :

    n = n + 1
    s = s + n

    if s >= 15000 :

        print("go !")




