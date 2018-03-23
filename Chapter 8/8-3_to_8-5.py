'''
	8-3: Functions 103 - Using keywards and 
	positional objects in calls.  
	
	For this, we'll make a function that prints
	name and age.  We'll call the function in
	two different ways with the same input.
'''
def personAge(name, age):
	print(name.title() + " is " + str(age) + " years old.")
personAge('lorenzo', 29)
personAge(name='lorenzo', age=29)

'''
	8-4: Default parameter values in functions.
	
	We definitely want to pass this function of
	as semi-sentient, so let's modify the function
	definition just a tad.
'''
def personAgeTricky(age, name='human'):
	print(name.title() + " is " + str(age) + " years old.")
personAgeTricky(12)

'''
	8-5: Continuing to build on functions.
	
	We've got a handle on function basics so this
	next section will be a new function that will
	take in two parameters (sports_team and location)
	with a default location parameter.
'''
def teamInfo(sports_team, location="USA"):
	print("The " + sports_team + " represent " +
		location + ".")
teamInfo("49ers", "San Francisco")
teamInfo("Raiders", "Las Vegas")
teamInfo("Team USA")