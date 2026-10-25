#Check if the entered year is leap or not
year = int(input("Enter a year: "))

leap = False
if year%4 == 0 and year%100 != 0:
    leap = True
elif year%4 == 0 and year%100 == 0:
    leap = True

if leap:
    print(f"The year {year} is a leap year")
else:
    print(f"The year {year} is not a leap year")