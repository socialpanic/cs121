import random								#I import the random lib to use randint
pot=input("how much do you want to spend on this game? ")		#ask the user how much they want to spend
count = 0								#set a counter
gross = pot								#gross is set up keep track of how much the player wins at any given time
while True:								#good ol while loop
	count += 1		
	d1 = random.randint (1, 6)					#roll some d6's
	d2 = random.randint (1, 6)
	total = d1 + d2							#add them
	print total							#print the total to the player
	if total == 7:							#if they equal 7 the player wins
		if gross<pot:						#BEFORE wins and looses are figured the program sees if the pot is bigger than gross
			gross=pot					#if its not then gross keeps its value
		pot += 4
		print "lucky you. +4. you have", pot,"dollars"
		
	else:
		if gross<pot:
			gross=pot
		pot -= 1
		print "oh no -1. you have", pot,"dollars" 
	if pot == 0:							#finally, when the player hits rock bottom
		print "thanks for playing"				#they are thanked for their time
		break							#and the loop breaks
print "it took", count,"to break you"					#the number of rounds
print "the most u had was", gross					#and the players highest gross or winnings are displayed


	
