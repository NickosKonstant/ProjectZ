#Exercise 1
#Tax ID Numder
#Input: TIN
#Output: check validity of TIN 

tin = int(input("Please enter TIN: ")) 
while len(tin) != 8:
    tin = int(input("Please enter an 8-digit TIN: "))

    
check_digit = tin%10
tin = tin//10                           #remove the check digit

digits = [int(i) for i in str(tin)]     #get reversed digits list
digits.reverse()

s = 0                                       
power = 1
for num in digits:
    s += num*(2**power)
    power += 1
# s = sum([n*(2**p) for n in digits for p in range(1,8)])


if (s%11)%10 == check_digit: 
    print("Tax Identification Number is valid ")
else:
    print("Tax Identification Number is not valid ")
