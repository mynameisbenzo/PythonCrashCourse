'''
	11-1 a): We'll create a function 
	that takes in a city and country
	and prints it out like so:
		City, Country
'''
def cityCountryDisplay(city, country):
	return (city.title() + ", " + country.title())
'''
	11-2 a): We'll be creating a modified
	version of the above function that also
	takes in a parameter for population and
	returns a string constructed with all
	parameters.
'''
def cityCountryPopulation(city,country,population=-1):
	if population < 0:
		return cityCountryDisplay(city, country)
	else:
		return (city.title() + ", " + country.title() 
			+ " - population " + str(population))