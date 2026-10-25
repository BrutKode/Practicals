#Angle of hour hand at any given time
hours = int(input("Enter the number of hours passed since midnight: "))
minutes = int(input("Enter the number of minutes passed since midnight: "))
seconds = int(input("Enter the number of seconds passed since midnight: "))

#Hours cannot be more than 12
#Minutes and seconds cannot be more than 60
if(hours < 12 and minutes < 60 and seconds < 60):
    #1 rotation = 360 degrees, 1 hour = 360/12 = 30 degrees
    #1 minute = 30/60 = 0.5degrees
    #1 second = 0.5/60 = 1/120 degrees
    angleDueToHours = hours*30
    angleDueToMinutes = minutes*0.5
    angleDueToSeconds = seconds*(1/120)
    totalAngleRotated = angleDueToHours + angleDueToMinutes + angleDueToSeconds
    print(f"Angle of hour hand made from 00:00:00 is {totalAngleRotated}degrees at {hours}:{minutes}:{seconds}")
else:
    print("Invalid time entered!")