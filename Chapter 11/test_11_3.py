'''
	11-3 test: We'll create a test for the
	Employee class we created in 11-3 main.
'''
import unittest
from main_11_3 import Employee

class TestEmployee(unittest.TestCase):
	
	# setup class for use in test cases
	def setUp(self):
		self.employee_test = Employee('lorenzo',
						'hernandez',15000)
	
	# test default give raise
	def test_defRaise(self):
		self.employee_test.give_raise()
		self.assertEqual(20000,self.employee_test.salary)
	
	# test custom give raise
	def test_custRaise(self):
		self.employee_test.give_raise(2500)
		self.assertEqual(17500,self.employee_test.salary)

if __name__ == '__main__':
	unittest.main()