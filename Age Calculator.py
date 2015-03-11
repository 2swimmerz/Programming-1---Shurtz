#Python V. 3.4.2
from datetime import datetime, date, time

bmonth = input("Enter your birth month: ")
bday = input("Enter your birth day: ")
byear = input("Enter your birth year: ")

print ("Your birthday is {0}-{1}-{2}".format(bmonth, bday, byear))
print ("Todays date is ", datetime.today().strftime("%m-%d-%Y"))

if int(datetime.today().strftime("%m")) <= int(bmonth):
    if int(datetime.today().strftime("%d")) < int(bday):
        age = int(datetime.today().strftime("%Y")) - int(byear) - 1
    else:
        age = int(datetime.today().strftime("%Y")) - int(byear)
else:
    age = int(datetime.today().strftime("%Y")) - int(byear)

print ("You are {0} years old.".format(age))