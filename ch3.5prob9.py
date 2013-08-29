sum=0.0								#modified code from page 104
count=0								#added a counter
while True:							#while loop prompts the user for input
	data=raw_input("give me a number or press enter: ")	
	if data!="":						#If the users input is NOT enter then
		numb = float(data)				#the string is converted to a float
		count += 1					#the counter goes up by +1 so that the program knows how many values there are
		sum += numb					#the users information is added to the sum
	else:
		break						#else is called when the user hits enter breaking the if statement and ending the while loop
avg = sum/count							#avg is calculated with the sum divided by the count (number of values given)
print sum
print avg