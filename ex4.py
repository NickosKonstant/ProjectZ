#Exercise 4


numbers = input("Please enter a 9-digit number: ")

row1 = ""
row2 = ""
row3 = ""


for elem in numbers:

    if int(elem)%3 == 1:
        row1 = row1 + elem + "  "
    elif int(elem)%3 == 2:
        row2 = row2 + " " + elem + " " 
    else:
        row3 = row3 + "  " + elem

print(row1)
print(row2)
print(row3)
