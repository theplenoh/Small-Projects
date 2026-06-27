def getLastDay(year, month):
    if month == 1:
        return 31
    elif (month == 2) and ((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)):
        return 29
    elif month == 2:
        return 28
