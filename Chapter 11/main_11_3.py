'''
	11-3 main: For this exercise, we'll
	be testing the creation of a class.
	
	We'll be creating an Employee class.
'''
class Employee():
	
	# initializer
	def __init__(self, first, last, salary):
		self.first = first
		self.last = last
		self.salary = salary
		
	'''
		gives 5000 raise by default or
		gives a raise of the given amount
		passed as a parameter
	'''
	def give_raise(self, salary_raise=5000):
		self.salary += salary_raise