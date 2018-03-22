'''
	5-1: Conditional statements without the
	shampoo.  Not working with if statements
	just yet.
'''
cat = 'big'
print("I think cat == 'big' will be True.")
print(cat == 'big')
print("Now, obviously that means cat == 'small' will be False.")
print(cat == 'small')

# ...which isn't to say python some how knows what a cat is
# and can comprehend size.... maybe this is more clear.
print("I think cat == 'bug' will be False.")
print(cat == 'bug')

# 'big' not equal to 'bug.  That's what we're getting at!
# Now a true statement...
print(cat != 'bug')
# False
print(cat == 'T-Rex')
# True twice!
cat = 'dog'
print(cat == 'dog')
cat = 'catdog'
print(cat == 'catdog')
# false, true, false!
dog = 'dog'
cat = 'cat'

# irrefutable proof that dogs are clearly better pets
print(cat > dog) 
print(dog > cat)
print(cat == dog)

'''
	5-2: We've got an assignment!  ...assignment... S!
	With an s. 
		1) string equality/inequality
		2) tests incorporating lower()
		3) number tests with ==, !=, <, >, <=, >=
		4) and, or
		5) in
		6) not in
'''
# 1
pet1 = 'Cat'
pet2 = 'cat'
if pet1 == pet2:
	print("This won't get printed.")
else:
	print("This will, though.")

# 2
if pet1.lower() == pet2:
	print("This will get printed.")

# 3
numbers = range(1, 21)
for num in numbers:
	if num == 1:
		print("equals")
	elif num != 1:
		if num >= 19:
			print("We're at the finish line.")
		elif num <= 3:
			print("A long ways to go!")
		elif num < 10:
			print("Coming up on halfway!")
		elif num > 12:
			print("Getting closer...!")
		else:
			print("This number is 11!")

# 4
if pet1.lower() == pet2 and 5 in numbers:
	print("And.  I have nothing else for this.")
if pet1.upper() == pet2 or 12 in numbers:
	print("Or.  See above")

# 5
number = 2
if number in numbers:
	print("Found it.")

# 6
number = number * 11
if number not in numbers:
	print("Lost it.")