hours = int(input("Enter the number of hours passed since midnight(12:00:00): "))
minutes = int(input("Enter the number of minutes passed since midnight(12:00:00): "))
seconds = int(input("Enter the number of seconds passed since midnight(12:00:00): "))

if(hours <= 12 and minutes<60 and seconds<60):
    print(f"Angle of hour hand from midnight position: {hours*30 + minutes*0.5 + seconds*(1/120)}")
