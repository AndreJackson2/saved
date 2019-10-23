import random 
myWord = "ganghead"
count = 0 
secretList = list(myWord)
secret = []
for a in secretList: 
	secret.append("_")
	print (secret ) 
	while True:
		choice2 = input("Enter 1 to guess a letter f to guess a word and q to quit :")
		print("Game Over")
		break
	else:
		pass
		if secret == myWord:
			print("Congrats! You gguessed the right letter: ")
		if choice 2 =="1":
			letter = input("Type a letter:")
			if letter in myWord:
				if letter == "e":
					secret[0] = "e"
					secret[4] = "e"
					print(secret)
					print("Misses: "+ str count) 
					elif letter == "g"
					secret[1] =
