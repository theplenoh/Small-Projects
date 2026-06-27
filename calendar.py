def getLastDay(year, month):
    lastDays = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        lastDays[2] = 29

    return lastDays[month]

#currYear = 2024

monthInfo = []
