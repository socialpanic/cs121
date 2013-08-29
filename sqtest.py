from sqclass import sqclass
l = input ("Give me the Length: ")
w = input ("Give me the Width: ")
h = input ("Give me the Height: ")
test = sqclass(l,w,h)                                                                  	#length, width, and height are passed to sqclass as l, w, h
print "The Volume of the box is", test.volume(), "meters sq" 				#volume function is called from that class 
print "The Surface Area of the box is", test.surface_area(), "meters sq"		#Then the surface_area function
