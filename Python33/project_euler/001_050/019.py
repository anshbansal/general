def prob_019():
    total = 0
    days = 0
    for year in range(1900, 2001):
        for month in range(1, 13):
            if month in [4, 6, 9, 11]:
                days += 30
            elif month == 2:
                if year % 4: # Not leap year
                    days += 28
                if not(year % 4) and year % 400: #Leap year
                    days += 29

            days %= 7
            if days == 0:
                total += 1

    return total
                    
if __name__ == "__main__":
    print(prob_019())
