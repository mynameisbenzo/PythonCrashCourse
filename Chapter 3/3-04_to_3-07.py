# 3-4: Let's make of list of people I'd like to meet

people = ['Jim Carrey', 'Dave Chappelle', 'Dunkey']

# ...then we'll invite them.

frontInviteMsg = 'I am inviting '
backInviteMsg = ' to dinner.'
print(frontInviteMsg + people[0] + backInviteMsg)
print(frontInviteMsg + people[1] + backInviteMsg)
print(frontInviteMsg + people[2] + backInviteMsg)

# 3-5: Hmm looks like Dunkey can't make it

print(people[2] + ' is too busy playing KNACK 2 BAYBEE!!!')

# ...let's change Dunkey to Keanu Reeves and invite them all again.

people[2] = 'Keanu Reeves'
print(frontInviteMsg + people[0] + backInviteMsg)
print(frontInviteMsg + people[1] + backInviteMsg)
print(frontInviteMsg + people[2] + backInviteMsg)

''' 
	3-6: ...huh, looks like you forgot you've got an actual 
	table to sit on with enough space for 6 people and not 
	the end table you were planning on having everyone sit on.
	Weird. Not sure how you can miss that.
	
	Let's invite 3 more people.
'''
print('I found a bigger table!')

# add a guest in the beginning
people.insert(0, 'Jackie Chan')
people.insert(2, 'Arnold Schwarzenegger')
people.append('Akira Toriyama')

# ...once again! Let's send out all those invitations!
print(frontInviteMsg + people[0] + backInviteMsg)
print(frontInviteMsg + people[1] + backInviteMsg)
print(frontInviteMsg + people[2] + backInviteMsg)
print(frontInviteMsg + people[3] + backInviteMsg)
print(frontInviteMsg + people[4] + backInviteMsg)
print(frontInviteMsg + people[5] + backInviteMsg)

'''
	3-7: Whoops.  Looks like practicing your wrestling
	skills backfired and you broke your big table.
	Looks like it's back to the end table!  Before that,
	let's whittle down that list of people.
'''

print('Sorry, everyone.  There was a mishap and I can only invite two people.')
print('Thanks for all the great movies in the 90\'s Mr. ' + people.pop(1) + '.')
print('I\'m sorry, Mr. ' + people.pop(0) + ', but I don\'t want trouble!')
print('I don\'t have any vampire food, Mr. ' + people.pop(2) + '...')
print('I never thought you were crazy, Mr. ' + people.pop(1) + '.')

# now we invite the two left... for the third and final time!
print('Mr. ' + people[0] + ', I hope you know I passed up some great lines by keeping you on this list')
print('Mr. ' + people[1] + ' why can\'t Gohan have a bigger spot in the limelight!?!?')

# ...so after an okay dinner your guests leave.  The list should reflect that.
del people[1]
del people[0]

'''
	Now, I really doubt either of these guys would want to 
	hang out in your room, but let's check the list to see
	if they're still there.
'''
print(people)