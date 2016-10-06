#exercise 7
#Days between two dates

import math

dates =[x for x in input("Please enter dates: ").split()]

date1 = dates[0].split("/")
date2 = dates[1].split("/")

day1 = int(date1[0])
day2 = int(date2[0])
month1 = int(date1[1])
month2 = int(date2[1])
year1 = int(date1[2])
year2 = int(date2[2])

if year1 < 0:
    year1 = abs(year1)
if year2 < 0:
    year2 = abs(year2)
    
c1 = 365*year1 + math.floor(year1/4) - math.floor(year1/100) + math.floor(year1/400) + math.floor((306*month1 + 5)/10) + (day1 - 1)
c2 = 365*year2 + math.floor(year2/4) - math.floor(year2/100) + math.floor(year2/400) + math.floor((306*month2 + 5)/10) + (day2 - 1)     

if year1*year2 >= 0:
    dif = abs(c1 - c2)
elif year1 < 0:
    dif = abs(c1 - c2) + 2*c1
elif year2 < 0:
    dif = abs(c1 - c2) + 2*c2

    
print(day1, day2, month1,month2,year1,year2)
print(dif, " days.")

