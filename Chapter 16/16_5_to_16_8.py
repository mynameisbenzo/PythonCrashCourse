'''
	16-5:
		Goal:
			There are some countries in that cannot
			be found in the COUNTRIES dictionary.
			Determine what those countries are and
			return the correct country_code.
	16-6:
		Goal:
			Create a world map that displays the GDP
			of each country with the link given in 
			the book.
	16-7:
		Goal:
			Choose my own data to display on the world
			map for each country.
	16-8:
		Goal:
			Write a proper test for the first problem 
			16-5.
			
	Approach:
		Problem 5 will be addressed in the projects 
		section and not here.
		
		Problem 6 will be addressed here as well as
		Problem 7.
		
		Problem 8 will also be addressed in the projects
		section.
'''
import json
import math

from pygal.maps.world import World
from pygal.style import LightColorizedStyle, RotateStyle

from countries import get_country_code

# load data into a list
filename = 'gdp.json'
with open(filename) as f:
	gdp_data = json.load(f)
	
# build a dictionary for population data
cc_gdp = {}
for gdp_dict in gdp_data:
	if gdp_dict['Year'] == 2010:
		country_name = gdp_dict['Country Name']
		gdp = float(gdp_dict['Value'])/1000000000
		code = get_country_code(country_name)
		if code:
			cc_gdp[code] = gdp
			
# group the countries into 3 population levels
cc_gdp_1, cc_gdp_2, cc_gdp_3 = {},{},{}
for cc, gdp in cc_gdp.items():
	if gdp < 50:
		cc_gdp_1[cc] = gdp
	elif gdp < 10000:
		cc_gdp_2[cc] = gdp
	else:
		cc_gdp_3[cc] = gdp
		
# see how many countries are in each level
print(len(cc_gdp_1), len(cc_gdp_2), len(cc_gdp_3))
			
wm_style = RotateStyle('#336699', base_style=LightColorizedStyle)
wm = World(style=wm_style)
wm.force_uri_protocol = 'http'
wm.title = "World GDP in 2010, by Country\n per billion"
wm.add('0-1bn', cc_gdp_1)
wm.add('1bn-1qd', cc_gdp_2)
wm.add('>1qd', cc_gdp_3)

wm.render_to_file('world_gdp.svg')