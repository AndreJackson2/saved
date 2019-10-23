import random

mystreyNunber = random.randint(1, 100)
score = 0 

while True: 
	guess = int(input("Guess a number between 1 and 10: "))
	score += 1 # the same as score = score + 1 
	if guess == mystreyNumber: 
		print("Youn guessed correctly, nicely done")
		break 
	elif guess > mystreyNumber:
		print("too high, try again")
	else :
		print("Too low, try again")
print("You took" + str(score) + "Guesses")
