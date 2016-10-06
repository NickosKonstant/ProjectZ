#Exercise 2
#parity bit


number = input("Please enter binary number: ")

parity_bit = number[-1]
parity = number[:-1]

print(parity)

if parity.count('1')%2 == 0:
    parityOK = 1                    #even parity
else:
    parityOK = 0                    #odd parity

if parity_bit == parityOK:
    print("Parity check OK.")
else:
    print("Parity check not OK")
