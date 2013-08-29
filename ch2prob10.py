wage = float(input("How much does employee earn per hour? "))
hour = float(input("How many regular hours? "))
over = float(input("How many Overtime hours? "))
pay = (wage*hour)+(wage*1.5*over)
print "The employees total pay is", round(pay, 2) 		#rounded the float for pay to two decimal places.