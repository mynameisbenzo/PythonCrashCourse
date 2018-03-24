'''
	9-6: Time to learn about inheritance.
	Parents, children, and who's got access
	to what.  We'll work off of the restau-
	rant class to build an IceCreamStand 
	class.
'''
from myClasses import IceCreamStand

flavors = ['chocolate','vanilla','coffee',
			'rocky road','strawberry','rainbow sherbet',
			'sea salt', 'pistachio'
		]
myStand = IceCreamStand('Cold Spot','Ice Cream', flavors)
myStand.show_flavors()

'''
	9-7: We'll do the same thing we just
	did but this time we'll use the User
	class to create an Admin class.
'''
from myClasses import Admin
from myClasses import Privileges
# privs = ['can ban','can post',
		# 'can delete','can permaban']
privs1 = Privileges(True, True, True, True, False)
myAdmin = Admin('Gon','Freecs','wheresMyDad',
				'03/23/2011',privs1)
myAdmin.show_privileges()

'''
	9-8: Classes inside classes. The 
	privileges attribute will be turned
	into a class that has it's own method
	to check privileges.  An instance is
	a part of the Admin class.
'''
privs2 = Privileges(True, True, True, True, True)
myUser = Admin('Ging','Freecs','dontTellHim',
				'03/23/2001',privs2)
myUser.show_privileges()

'''
	9-9: Finally, we'll use the Car, ElectricCar,
	and Battery classes created in the book to
	do a little tweaking.
'''
from myClasses import ElectricCar
myECar = ElectricCar("Toyota","Prius Prime",2018)
myECar.battery.get_range()
myECar.battery.upgrade_battery()
myECar.battery.get_range()