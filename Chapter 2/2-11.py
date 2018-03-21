# incorporating integers into string

number = 1
front = 'I have '
back = ' dog.'

""" Should be noted that attempting to concatenate strings alongside integers, like so:
	
		sentence = front + number + back
		
	...will result in errors.  See below for proper methods.
"""

# using the str() function
sentence = front + str(number) + back

# prints out 'I have 1 dog.'
print(sentence)