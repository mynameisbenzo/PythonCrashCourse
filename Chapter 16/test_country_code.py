import unittest
from countries import get_country_code

class CCTestCase(unittest.TestCase):
	# check return for existing country
	def test_existing_country(self):
		code = get_country_code('Brazil')
		self.assertEqual(code, 'br')
		
	'''
		check return for existing country located in
		created associations dictionary
	'''
	def test_association_country(self):
		code = get_country_code("Venezuela, RB")
		self.assertEqual(code, 've')
		
	# check return None for country that does not exist
	def test_no_country(self):
		code = get_country_code("Lorenzostan")
		self.assertEqual(code, None)
		
unittest.main()