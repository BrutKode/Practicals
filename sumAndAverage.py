#Calculate the sum and average of first n natural numbers
n = int(input("The number of numbers to consider: "))

result = 0
for i in range(1, n+1):
    result+=i

print(f"The sum of the first {n} numbers is {result} and the average is {result/n}")
