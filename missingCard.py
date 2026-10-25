#Find missing cards if cards represent consecutive integers
limit = int(input("How many cards to generate: "))
numbers = map(int, input("Enter the remaining cards separated by spaces: ").split(" "))

expected = (limit*(limit+1))/2
reality = sum(numbers)

missingCard = expected - reality
print(f"The missing card is {missingCard}")