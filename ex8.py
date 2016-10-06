#Exercise 8


numbers = input("please enter a sequence of numbers: ")

sum = 0

if len(numbers)%2==1:
    sum = int(numbers[-1])
    numbers = numbers[:-1]

while numbers !='':
    sum += int(numbers[0])*int(numbers[1])
    numbers = numbers[2:]



print(sum)
    

                
