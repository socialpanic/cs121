print "Welcome to Five Star Rental"
fname=raw_input("Please enter customers first name: ")
lname=raw_input("Please enter customers last name: ")
phone=raw_input("Please enter customers phone number: ")
oldvids=input("How many old videos would you like? ")
newvids=input("How many new videos would you like? ")
oldprice=input("How much for old rentals? ")
newprice=input("How much for new rentals? ")
cost=(oldvids*oldprice)+(newvids*newprice)
print "=============RECIPT=================="
print "Customer Name: ", fname, lname
print "Phone: ", phone
print "Old Rentals QTY", oldvids, "@",oldprice, "dollars"
print "New Rentals QTY", newvids, "@",newprice, "dollars"
print "Total:             ",cost, "dollars"
print "====================================="
input ("Thank you and have a nice day. Press Enter to exit POS")
end
