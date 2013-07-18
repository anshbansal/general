total = 0
days = 0
for year in xrange(1900,2001):
    for month in xrange(1,13):
        if (month in [4,6,9,11]):
                days += 30
        elif month == 2:
            if year % 4 != 0: # Not leap year
                days += 28
            if (year % 4 == 0) and (not (year % 400 == 0)): #Leap year
                days += 29

        days %= 7
        if days == 0:
            total += 1

print total
                
            
