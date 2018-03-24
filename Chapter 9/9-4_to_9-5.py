'''
	9-4: For this exercise, we want to use
	the class created in 9-1.  This is a 
	chance to separate the class from that
	file and import it in.  We'll also
	add an attribute that shows the number
	served two class methods that will alter
	that attribute.
'''
from myClasses import *

myPlace = Restaurant('Lorenzo\'s','Mexican')
myPlace.open_restaurant()
myPlace.set_number_served(5)
print(str(myPlace.number_served))
myPlace.increment_number_served(5)
print(str(myPlace.number_served))

'''
	9-5: We'll be doing the same thing we did
	in 9-4 except this time we'll be doing it 
	for the User class in 9-3.  The User class
	will be updated to keep track of the amount
	of login attempts.
'''
me = User('Lorenzo','Hernandez','captPupper','03/23/2018')
me.increment_login_attempts()
me.increment_login_attempts()
print(str(me.login_attempts))
me.reset_login_attempts()
print(str(me.login_attempts))