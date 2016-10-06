#Exercise 3
#


numbers = input("Please enter a 10-digit number: ")

even = ""
odd = ""              
index = 0

for n in numbers:
    
    if index%2 == 0:
        even = even + n + " "
    else:
        odd = odd + " " + n 
    index += 1
              
print(even)
print(odd)
