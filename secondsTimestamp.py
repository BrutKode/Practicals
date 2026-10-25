#To calculate the number of seconds between 2 timestamps
h1, m1, s1 = map(int, input("Enter the first timestamp in HH:MM:SS format: ").split(":"))
h2, m2, s2 = map(int, input("Enter the second timestamp in HH:MM:SS format: ").split(":"))

secondsOf1 = h1*3600 + m1*60 + s1
secondsOf2 = h2*3600 + m2*60 + s2

difference = secondsOf2 - secondsOf1

print(f"The 2 timestamps are {difference} seconds apart")