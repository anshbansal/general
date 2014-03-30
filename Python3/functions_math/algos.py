__author__ = 'Aseem'


def is_leap_year(year):
    """Returns whether year is leap or not"""
    if year % 4 != 0:
        return False
    elif year % 100 != 0 or year % 400 == 0:
        return True
    else:
        return False


def get_days(from_year, to_year):
    """Generates tuple of (month number, num of days)"""
    for year in range(from_year, to_year):
        for month in range(1, 13):
            if month in [4, 6, 9, 11]:
                yield (month, 30)
            elif month == 2:
                if is_leap_year(year):
                    yield (month, 29)
                else:
                    yield (month, 28)
            else:
                yield (month, 31)