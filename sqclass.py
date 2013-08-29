class sqclass:
    def __init__(self,length,width,height):	#The data members are defined here (length, width, height)
        self.length = length			#Length is passed into the class "l" from the test script
        self.width = width			#Width is passed in as "w"
	self.height = height			#Height is "h"

    def surface_area(self):
        return ((2*self.length * self.height)+(2*self.width*self.height)+(2*self.length*self.width)) #This returns the surface area to what called it.
    def volume(self):
        return self.length * self.width * self.height #This returns the volume
    
