#Check whether the entered date is valid
year = int(input("Enter the year: "))
month = int(input("Enter the month: "))
day = int(input("Enter the day: "))

valid = True
monthsWith31Days = [1, 3, 5, 7, 8, 10, 12]

if day > 31 or month > 12:
    valid = False
if month not in monthsWith31Days:
    if month == 2:
        if year%400 == 0 or (year%4 == 0 and year%100 != 0):
            if day > 29:
                valid = False
        elif day > 28:
            valid = False
    if day > 30:
        valid = False

if valid:
    print(f"The date {day}/{month}/{year} is valid")
else:
    print(f"The date {day}/{month}/{year} is invalid")
