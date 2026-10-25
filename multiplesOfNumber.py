#Display first n multiples of a number
num = int(input("Enter an number: "))
n = int(input("Enter the number of multiples to display: "))

for i in range(1, n+1):
    print(f"{num} x {i} = {num*i}")