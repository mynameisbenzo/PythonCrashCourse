# 3-8: More lists!  This time let's get a list of places
places = ['Aruba', 'Jamaica', 'Bermuda', 'Bahama', 'Key Largo', 'Montego', 'Kokomo']

# FIRST! we show the list
print(places)

# THEN!!!! we show it sorted, but let's not sort the list yet
print(sorted(places))

# ...just to be sure it hasn't been changed
print(places)

'''
	Now, let's sort it again, not changing the list, 
	but this time reverse alphabetical order.
'''
print(sorted(places, reverse=True))

# Again, check it's not changed.
print(places)

# Let's flip the list around.
places.reverse()
print(places)

# ...enough that.  Put it back.
places.reverse()
print(places)

# alright, well I guess we should sort the list permanently
places.sort()
print(places)

# ...and then we sort again, but in reverse order.
places.sort(reverse=True)
print(places)

# NOTE: Could've just called places.reverse(), too

'''
	3-9: Let's go back and see how many guests we had
	in the 3-7 list of guests.  
'''

people = ['Jim Carrey', 'Dave Chappelle', 'Dunkey']
people[2] = 'Keanu Reeves'
people.insert(0, 'Jackie Chan')
people.insert(2, 'Arnold Schwarzenegger')
people.append('Akira Toriyama')

print('The guest list you finished with had ' + str(len(people)) + ' people in it!')

'''
	3-10: Our goal now is to use all the list functions 
	and properties!
		- Access elements by index
		- append()
		- insert()
		- del
		- pop()
		- remove()
		- sort(), sort(reverse=True)
		- sorted(list, reverse=True)
		- reverse()
		- len()
'''
# Let's make a list of things I do to pass the time.
hobbies = [	'Program','Learn','Exercise','Read something fictional', 
			'Play a game', 'Watch a show', 'Build rockets'
		]
		
# alright, got it... no wait.
hobbies.append('Apply for jobs')

# okay, think that's it... well, no.  Just one more.
hobbies.insert(0, 'Chase dogs that aren\'t mine for thorough petting.')

# ...uh, okay.  Well, I'm thinking rockets aren't too 
# but if I'm being honest... I don't do that.
hobbies.remove('Build rockets')

# AND.. I guess... applying for jobs can't really be a hobby... 
del hobbies[7]

# alright now... I don't chase dogs often... so let's flip this around.
hobbies.reverse()

# well, now that I think about it.  I barely do it all so...
hobbies.pop(6)

# Pretty sure I lost count... how many hobbies is that?
print("Lorenzo has " + str(len(hobbies)) + " hobbies.")

# quick preview of what it looks like sorted
print(sorted(hobbies))

# Nope.  Not feeling it.  Let's flip it.  I think I'll be good with that.
hobbies.sort(reverse=True)

# Let's see what we got!
print(hobbies)