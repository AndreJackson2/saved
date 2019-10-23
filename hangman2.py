# hangman game 
myWord = "Gangman"

turns= 10 
if turns == 

choice = input("Type a word")

if choice == myWord:
	print(" Goodjob that's correct")
else:
	print(" Sorry thats wrong")

# how to check to see if your word is right or not 
letter = input("Type a letter")
if letter in myWord: 
	print("Letter is in the word")
else: 
	print("Letter is not in the word")

count = 0 
for s in myWord: 
	if s == letter: 
		print(count)
	count+= 1 

	
