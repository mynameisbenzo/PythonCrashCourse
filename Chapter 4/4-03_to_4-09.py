'''
	4-3: Working with for loops.
	First, let's count to twenty
'''
for value in range(1,21):
	print(value)
'''
	4-4: Great.  You can count to twenty.
	What about a million?
'''
overkill = range(1,1000001)
# for number in overkill:
	# print(number)
'''
	4-5: ...hopefully that's enough counting for now.
	We'll comment that out for the time being.
	
	Obviously your list should be min = 1 and max = 1000000,
	so let's see if you did that right and we'll go ahead
	and up all the numbers.
'''
print(min(overkill))
print(max(overkill))
print(sum(overkill))
'''
	4-6: Really not surprised that takes much less time
	than printing that whole list out.  
	
	Whole list is overkill, though!  Let's just get odd 
	numbers between 0-20
'''
odd = range(1,20,2)
for num in odd:
	print(num)
'''
	4-7: Great.  Fun.  It might just be the time, but 
	for loops have lost their excitement in my head.
	
	BUT THE LESSONS MUST GO ON!  Let's get a list of
	multiples of three up to 30.
'''
threes = [value*3 for value in range(1,11)]
for mult in threes:
	print(mult)
'''
	4-8: ...could use some coffee. Haven't had sugar in
	awhile.  Wouldn't want it but would be cool to get
	those little sugar cubes.
	
	Cubes.  That's the next list!
'''
sugarCubes = []
for val in range(1,11):
	sugarCubes.append(val**3)
for cube in sugarCubes:
	print(cube)
'''
	4-9: That last one could've been a lot simpler with
	a list comprehension so let's do just that.
'''
sugarCubesComprehension = [val**3 for val in range(1,11)]
for cube in sugarCubesComprehension:
	print(cube)