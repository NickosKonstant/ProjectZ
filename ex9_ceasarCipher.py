#Exercise 9
# Ceasar cipher

shift = int(input("please enter swift: "))
phrase = input("please enter phrase: ")

alphabet_lower = "abcdefghijklmnopqrstuvwxyz"
alphabet_upper= "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

for letter in phrase:
    if letter in alphabet_upper:
        print(alphabet_upper[(alphabet_upper.index(letter) + shift)%26], end='')
    elif letter in alphabet_lower:
        print(alphabet_lower[(alphabet_lower.index(letter) + shift)%26], end='')
        

        
