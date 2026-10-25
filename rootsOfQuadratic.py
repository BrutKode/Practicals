#Finding the roots of a quadratic equation
#ax**2 + bx + c = 0 -> general form of quadratic equation
import math

a = int(input("Enter the coefficient of x square: "))
b = int(input("Enter the coefficient of x: "))
c = int(input("Enter the constant term: "))

D = b**2 - 4*a*c

if D>0:
    root1 = (-(b) + math.sqrt(D))/2*a
    root2 = (-(b) - math.sqrt(D))/2*a
    print(f"Roots are {root1} and {root2}")
elif D=0:
    root = -(b)/2*a
    print(f"Both roots are {root}")
else:
    real = -(b)/2*a
    imaginary = math.sqrt(-D)/2*a
    print(f"The roots are ({real} + {imaginary}i) and ({real} - {imaginary}i)")