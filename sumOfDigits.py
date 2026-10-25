#Find the sum of the digits of a number
num = input("Enter a number: ")

result = 0
for i in num:
    result+=int(i)

print(f"The sum of all digits of the entered number are: {result}")
