# Conditional
print("Weldome to Ticket Bot")
print("You must be at least 18 to see R rated movies")
age = int(input("How old are you?"))

if age > 17: 
	print("You can go see an R rated movie")
else:
	print("You cannot go see an R rated movie")

print("Thank you")

mystreyNum = 6 
guess = int(input(" Guess a number betweeen 1 and 10: "))

if guess == mystreyNum:
	print("Good guess, That is correct")
elif guess > mystreyNum:
	print("Too high")
elif guess > 10:
	Print("Please read Directions")
else:
	print("Too low")
