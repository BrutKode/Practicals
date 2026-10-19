day = int(input("Enter day: "))
month = int(input("Enter month:"))
year = int(input("Enter year: "))

valid = True

if month<1 or month>12:
    valid = False
elif day<1 or day>31:
    valid = False
elif month in [4, 6, 9, 11] and day>30:
    valid = False
elif month == 2:
    if (year%400 == 0) or (year%4 == 0 and year%100 != 0):
        if day>29:
            valid = False
    elif day>28:
        valid = False
if valid:
    print(f"Entered date {day}/{month}/{year} is a valid date!")
else:
    print(f"Entered date {day}/{month}/{year} is an invalid date!")
