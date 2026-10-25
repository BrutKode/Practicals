#Bowling recreated in python
n = int(input("Enter the number of pins standing: "))
k = int(input("Enter the number of balls to bowl: "))

pins = ("! "*n).split(' ')
print(pins)
for i in range(1, k+1):
    start = int(input("Enter the index at which to start: "))
    end = int(input("Enter the index at which to end: "))
    for j in range(start, end+1):
        pins[j] = "."

print(pins)
