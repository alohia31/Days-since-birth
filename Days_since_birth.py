import time
## dd/mm/yyyy format
DaysInMonths = []
DaysInMonths[1:12] = 31,28,31,30,31,30,31,31,30,31,30,31

def leap_check(year):
    if year%4 == 0:
        return 1
    else:
        return 0
    
def numberOfLeaps(now_date, birth_date):
    number = 0
    year = birth_date[2]
    if (birth_date[1] > 3):
        year = year + 1
    while (year <= now_date[2]):
        number = number + leap_check(year)
        year += 1
    if (now_date[1] > 3):
        number = number + leap_check(year)

    return number
    
def countDaysInMonth(now_date, birth_date):
    month = birth_date[1]
    number = 0
    while(month < now_date[1]):
        number = number + DaysInMonths[month-1]
        month += 1
    return number

def validation(birth_date, now_date):
    if (birth_date[2] > now_date[2]) or ((birth_date[2] == now_date[2]) and (birth_date[1] > now_date[1])) or ((birth_date[2] == now_date[2]) and (birth_date[1] == now_date[1]) and (birth_date[0] > now_date[0])): 
        return False
    elif (birth_date[1] > 12) or (birth_date[0] > DaysInMonths[birth_date[1]-1]):
        return False
    else:
        return True

def count_days(birth_date, now_date):
    if validation(birth_date, now_date) == False:
        print "invalid input"
        quit()

    days = 0

    if (now_date[2] - birth_date[2] != 0):
        days += (now_date[2] - birth_date[2])*365 + numberOfLeaps(now_date, birth_date)

    if (now_date[1] - birth_date[1] > 0):
        days += countDaysInMonth(now_date, birth_date)
    elif (now_date[1] - birth_date[1] < 0):
        days -= countDaysInMonth(birth_date, now_date)

    days += now_date[0] - birth_date[0]

    return days
        
#Main Program
now_date = []
now_date[:2] = int(time.strftime("%d")), int(time.strftime("%m")), int(time.strftime("%Y"))

birth_d = raw_input("Enter your Birth date(dd/mm/yyyy): ")
birth_date = []
birth_date[:2] = int(birth_d[:2]), int(birth_d[3:5]), int(birth_d[6:])

print str(count_days(birth_date, now_date)) + " Days"
