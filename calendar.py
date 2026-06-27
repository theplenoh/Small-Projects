def getLastDay(year, month):
    lastDays = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        lastDays[2] = 29

    return lastDays[month]

monthNames = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December')

currYear = 2026

monthInfo = []
for i in range(1, 13):
    monthInfo.append({
        'ordinal': i, 
        'name': monthNames[i - 1], 
        'lastDay': getLastDay(currYear, i)
    })

print(monthInfo)
