#Check if the number is prime number
import math
num = int(input("Number to check: "))

if num < 2:
    print("Not Prime")
else:
    n = math.ceil(math.sqrt(num))
    prime = True
    for i in range(2, n):
        if num%i == 0:
            prime = False
            break
    if prime:
        print("Prime number spotted")
    else:
        print("Not Prime")
