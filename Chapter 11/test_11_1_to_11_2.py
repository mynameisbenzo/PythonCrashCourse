'''
	11-1 b) The following will be
	testing our function from 11-1a
	to see if it is displaying the 
	correct information.
'''
import unittest
from main_11_1_to_11_2 import *

class TestCityCountry(unittest.TestCase):

	# testing 11-1
	def testCityCountry(self):
		cityCountry = cityCountryDisplay('santiago','chile')
		self.assertEqual(cityCountry, 'Santiago, Chile')
		
	# testing 11-2
	def testCityCtryPop(self):
		cityCtryPop = cityCountryPopulation('santiago',
									'chile',500000)
		self.assertEqual(cityCtryPop, 
			"Santiago, Chile - population 500000")
unittest.main()