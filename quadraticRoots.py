import math

a = float(input("Enter coefficient of x**2: "))
b = float(input("Enter coefficient of x: "))
c = float(input("Enter constant: "))

d = b**2 - 4*a*c

if d>0:
    root1 = (-b + math.sqrt(d)/(2*a))
    root2 = (-b - math.sqrt(d)/(2*a))
    print(f"The roots are {round(root1,2)} and {round(root2,2)}")
elif d==0:
    root = -b/(2*a)
    print(f"Both the roots are {round(root,2)}")
else:
    realPart = -b/(2*a)
    imgPart = math.sqrt(-d)/(2*a)
    print(f"The roots are complex, ({round(realPart,2)} + {round(imgPart,2)}i) and ({round(realPart,2)} - {round(imgPart,2)}i)")
