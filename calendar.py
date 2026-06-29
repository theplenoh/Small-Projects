import datetime

def getLastDay(year, month):
    lastDays = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        lastDays[2] = 29

    return lastDays[month]

monthNames = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December')

currYear = 2026
currMonth = 4

monthInfo = []
for i in range(1, 13):
    monthInfo.append({
        'ordinal': i, 
        'name': monthNames[i - 1], 
        'lastDay': getLastDay(currYear, i)
    })

cnt = 0
print("%d년" % currYear)
for n in range(1, 13):
    print("[%3d월]" % n)
    for i in range(0, datetime.date(currYear, n, 1).weekday() + 1):
        print("    ", end="")
        cnt = cnt + 1
        if cnt % 7 == 0:
            print("")
    for i in range(1, monthInfo[n-1]['lastDay']+1):
        print("%4d" % i, end="")
        cnt = cnt + 1
        if cnt % 7 == 0:
            print("")
    print("")
    print("")
    cnt = 0
