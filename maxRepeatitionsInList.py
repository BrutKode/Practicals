#Return the number of repeatitions of same number consecutively in list
sequence = input("Enter numbers separated by spaces and terminate with zero: ").split()

count = 1
best = 1
for i in range(0, len(sequence)):
    if int(sequence[i]) == 0:
        break
    if i>0 and int(sequence[i]) == int(sequence[i-1]):
        count+=1
    else:
        best = max(best, count)
        count = 1
print(f"The widest fragment where numbers are equal to each other is {best+1} times")
