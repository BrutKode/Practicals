xes = []
yes = []

for i in range(1, 4):
    x = int(input(f"Enter x{i}: "))
    xes.append(x)

for i in range(1, 4):
    y = int(input(f"Enter y{i}: "))
    yes.append(y)

xans = 0
yans = 0
if(xes[0] == xes[1]):
    xans = xes[2]
elif(xes[1] == xes[2]):
    xans = xes[0]
else:
    xans = xes[1]

if(yes[0] == yes[1]):
    yans = yes[2]
elif(xes[1] == xes[2]):
    yans = yes[0]
else:
    yans = yes[1]


print(f"coordinates of missing point ({xans}, {yans})")

