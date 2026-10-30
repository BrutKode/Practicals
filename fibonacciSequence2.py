limit = int(input("How many terms: "))

n1 = 0
n2 = 1
i = 0
while limit > i:
    print(n1)
    n = n1+n2
    n1 = n2
    n2 = n
    i+=1
