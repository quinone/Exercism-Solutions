def leap_year(year):
    return not (not year % 4 == 0 or (year % 100 == 0 and not year % 400 == 0))
