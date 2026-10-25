#Find the sum of the digits of a number
num = int(input("Enter a number: "))

while(num%(10**i) != 0):
    sum += num%(10**i)

print(f"The sum of all digits of the entered number are: {sum}")