#Calculate the sum and average of first n natural numbers
n = int(input("The number of numbers to consider: "))

for i in range(1, n+1):
    sum+=i

print(f"The sum of the first {n} numbers is {sum} and the average is {sum/n}")