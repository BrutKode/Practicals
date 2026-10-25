#Display first n fibonacci numberss
n = int(input("Number of terms to consider: "))

i = 0
j = 0
k = 1
while i<n:
    tmp = j
    j = k
    k = tmp+1
    print(j, sep="")
    i+=1