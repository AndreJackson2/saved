# Andre
# Rock Paper Scizories 
#RPS.py
import random 
# Variables 
# added comment for github
pScore = 0 
cScore = 0
ties = 0
cMoves = ["Rock," " paper," "scissors"]

# Welcome message (DONE)
# Print a welcome message 
print("Welcome to rock paper scissiors")
# prompt for name
nName = input ("What is your name?")
# Score Tracker 

# Score Tracker 
# Make a function
def printscore():

	#Print Score:
	print("Score")	
# Show player Score 
	print(pName + ": " + str(pScore))
# Show computor score
	print("Somputor Score:" +str(cScore))
# Show how many ties 
	print("Ties." + str (ties))

# Game loop 
while True 
	# loop until q is entered 
	pMoive = input("Enter 'r' for rock, 'p' for paper, 's' fir Sissors or 'q' to quit ")
# print the score 
	printScore()
# check is q is entered if so end the game
# prompt for player move (r, p, s, q) 
	if pMove == 'q':
		break 
# get a computor move (random) 
cMoves = random.choice(CMoves)
# player picks rock
	elif pMove == "r"
		print("Computor picks Rock")
		print("Tie")
	pass
	# player picks paper 
	elif pMove == "p"
	pass
# player picks scissors
	elif pMove =="s"
	pass
# check if pMove is valid 
	else:
		print("That is not an option")