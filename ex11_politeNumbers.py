#Exercise 11
#Polite numbers

limit = int(input("Please enter limit: "))

if limit<= 7:
    imopoloite = [1,2,4]
else:
    impolite = [2**x for x in range(limit//2)]

counter = 0
polite = []    
for num in range(3,limit+1):
    if (num not in impolite):
        polite.append(num)

print(polite)
counter = 1
    
for num in polite:
    if counter<= 10:
        print(num, end= " ")
        counter +=1
    else:
        print('\n'+str(num), end=" ")
        counter = 2
    
