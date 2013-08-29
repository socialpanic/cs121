print "This program returns the value of two numbers"
x = input("Give me a number")
y = input("Give me another number")
while True:										#This while loop starts a series of if statements
	math = input("1 for Add, 2 for Subtract, 3 for Multiply, or 4 for Divide?")	#This is the menu that prompts the user for the desired function
	if math == 1:									
		z = x + y
		break									#These if statments can
	if math == 2:									#only be broken with
		z = x - y								#a valid input of 1-4
		break									#anything else prompts
	if math == 3:									#the user to try again
		z = x - y
		break
	if math == 4:
		z = x / y
		break									#valid input breaks the loop and prints the answer
	else:
		print "invlaid input"							#the else condition is called if anything but 1,2,3,or 4 is entered
print z
