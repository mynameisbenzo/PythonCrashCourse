'''
	10-1: Intro to reading files using
	with and lists.
'''
# entire file method
with open('myText.txt') as file_object:
	contents = file_object.read()
	print(contents)

# reading line be line using a for loop
with open('myText.txt') as file_object:
	for line in file_object:
		print(line.rstrip())
		
# storing file contents in list
with open('myText.txt') as file_object:
	lines = file_object.readlines()

for line in lines:
	print(line.rstrip())
	
'''
	10-2: Using replace on incoming 
	words.
'''
# let's be mario
for line in lines:
	print(line.replace('is','WAHOO').rstrip())