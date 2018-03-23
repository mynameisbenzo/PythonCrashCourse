'''
	8-15: Using functions in other modules.
	
	In this script, we'll call printMe from
	myPrint.py to print out the contents of
	a list.
'''
from myPrint import printMe
myList = ['cats','dogs','tv shows','lizards']
printMe(myList)

'''
	8-16: Pulling in functions and the different
	ways to do it.
	
	The above pulls in just the function printMe,
	but what if want the entire module or would 
	like to rename the module you're calling in?
	
	# get access to the entire python script
	import module_name
	
	# the follow does the same as the latter
	# the '*' symbol indicates 'all'
	from module_name import *
	
	# get access to a specific function in a module
	from module_name import function
	
	# rename the function or module you're accessing
	import module_name as newName
	from module_name import function as newName
'''

'''
	8-17: Styling.
	
	Note:
		- parameter='value' (no spaces) is preferred
		- if parameter list for function is too long,
			start a new line and continue your para-
			meter list.
'''