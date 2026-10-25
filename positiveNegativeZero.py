#Check if number is positive, negative or zero
num = int(input("Enter a number: "))

#Conditionals are applied as per probability of number entered
if num>0:
    print("Positive number spotted", num)
elif num<0:
    print("Negative number spotted", num)
else:
    print("Zero spotted", num)