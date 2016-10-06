#Exercise 5
#Easter Day

import math

year = int(input("Please enter year: "))

a = year%4
b = year%7
c = year%19
d = (19*c + 15)%30
e = (2*a + 4*b - d +34)%7

# Julia callender
month = math.floor((d + e + 114)/31)%31
day = (d + e + 114)%31 + 1

# Georgian calender

day_G = day + 13

# EasterMonths = [Mar: 31, Apr: 30, May: 31]

max_days = 0

if month == 3 or month == 5:
    max_days = 31
elif month == 4:
    max_days = 30


if day_G > max_days:
    month += 1
    day_G -= max_days 

print("Day: ",day_G, "Month: ", month)    
