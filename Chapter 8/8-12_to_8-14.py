'''
	8-12: Functions with no specified parameters.
	
	This function will take an any amount of argu-
	ments and print them out.
'''
def show_toys(*toys):
	for toy in toys:
		print(toy + " is a toy in my toy box!")
show_toys('n64','snes','action figure','football')

'''
	8-13: Using a book example.
	
	The function build_profile() is used in the 
	book to build up information about a person
	and return a dictionary with that information.
'''
def build_profile(first, last, **more):
	'''
		Build a dictionary containing everything
		that is known about a user.
	'''
	profile = {}
	profile['first_name'] = first
	profile['last_name'] = first
	for k, v in more.items():
		profile[k] = v
	return profile
me = build_profile('lorenzo','hernandez',age=29,
	location='california',likes=['pizza',
		'working out', 'the color green',
		'dogs!'
	]
)
print(me)

'''
	8-14: Now it's our turn!  
	
	I'm going to make a function that does some-
	thing similar to 8-13, but instead will do 
	it for cars.
'''
def build_car(make, model, **more):
	car = {}
	car['make'] = make
	car['model'] = model
	for k,v in more.items():
		car[k] = v
	return car
myOldCar = build_car('honda','accord',miles=220000,
	year=2005,color='charcoal')
print(myOldCar)