import os								#import the OS lib
os.chdir ("C:\\Documents and Settings\\socialpanic\\Desktop\\csfiles")	#NOTE: This was done on an XP VM so my working directory is different from the class enviroment
linecount = 0								#line counter is declaired and set to zero								
fileName = raw_input("Enter a file name: ")				#prompts the user for a file name
with open(fileName, 'r') as f:						#opened text file with 'r'ead rights
        for line in fileName:						#If statement that 
                linecount += 1						#count lines
        print "This document has", linecount, "lines in it."		#The number of lines in the file are printed
while True:								#Starts a loop that
	linex = input("Enter a number of line, to quit, press 0:")	#prompts for a file name
	if linex == '0':						#If zero is entered
                print "Have a good one"					#The user is told to have a good one
        	break							#and the loop breaks
	else:								#other wise
                with open(fileName, 'r') as f:				#the desired line is
                        print f.readlines()[:linex]			#printed
