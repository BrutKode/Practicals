#Delete all characters from a string whose indices are divisible by 3
myStr = input("Enter the string: ")
result = ""
for i in myStr:
    if i%3 == 0:
        myStr[i] = ""
    result+=myStr[i] #String concatenation
print(f"The modified string is {resultn}")