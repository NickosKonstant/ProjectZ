#Exercise 6

numbers =[ x for x in input("Please enter numbers: ").split()]

row_1 = ''
row_2 = ''
row_3 = ''


for index, elem in enumerate(numbers):
    if index%3 == 0:
        row_1 = row_1 + '  ' + elem + '|'
    elif index%3 == 1:
        row_2 = row_2 + ' ' + elem + '|'
    elif index%3 == 2:
        row_3 += elem + '|'

# Drop last '|' on every line
row_1 = row_1[:-1]
row_2 = row_2[:-1]
row_3 = row_3[:-1]


print(row_1)
print(row_2)
print(row_3)
