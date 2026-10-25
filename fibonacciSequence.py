#Display first n fibonacci numberss
n = int(input("Number of terms to consider: "))

previous = 0
current = 1
for i in range(1, n+1):
    tmp = previous
    previous = current
    current = current + tmp
    print(current)
