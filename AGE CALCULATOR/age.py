import time
import calendar 

def judgeleapyear(year):
    if calendar.isleap(year):
        return True
    else:
        return False
    
def monthdays(month, leapyear):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    elif month == 2:
        if leapyear:
            return 29
        else:
            return 28
    else:
        return 0
    
name = input("Enter your name: ")
age = int(input("Enter your age: "))
localtime = time.localtime(time.time())

year = int(age)
month = year * 12 + localtime.tm_mon
day = 0

beginyear = int(localtime.tm_year) - year
endyear = beginyear + year

for y in range(beginyear, endyear):
    if judgeleapyear(y):
        day = day + 366
    else:
        day = day + 365

leapyear = judgeleapyear(localtime.tm_year)
for m in range(1, localtime.tm_mon):
    day = day + monthdays(m, leapyear)

day = day + localtime.tm_mday

print("%s's age is %d years or " % (name, year), end="")
print("%d months or %d days." % (month, day))