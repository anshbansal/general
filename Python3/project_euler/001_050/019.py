def is_leap_year(year):
    return (year % 4 == 0) and ( \
        (year % 100 != 0) or (year % 400 == 0))


def prob_019():
    total = 0
    days = 1 + 365
    #1 for monday
    #Added 365 because 1900 isn't a leap year
    for year in range(1901, 2001):
        is_leap = is_leap_year(year)
        for month in range(1, 13):
            if month in [4, 6, 9, 11]:
                days += 30
            elif month == 2:
                if is_leap:
                    days += 29
                else:
                    days += 28
            else:
                days += 31

            days %= 7
            if days == 0:
                total += 1

    return total
                    
if __name__ == "__main__":
    print(prob_019())
