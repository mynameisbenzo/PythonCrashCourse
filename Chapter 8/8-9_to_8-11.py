'''
	8-9: Functions and lists.
	
	In these next few exercises, we'll
	create a list of magicians and print
	it out to begin with.  I'll use the 
	only magicians I know.
'''
magicians = ['Abra','Kadabra','Alakazam','Hypno',
		'David Blaine'
	]
greatMagicians = []
def show_magicians(magicians):
	if len(magicians) < 1:
		print("There's no magicians!")
		return
	for magician in magicians:
		print(magician)
show_magicians(magicians)

'''
	8-10: Altering lists within functions.
	
	It's time to make these magicians great
	again.
'''
def make_great(magicians, greatMagicians):
	while magicians:
		greatMagicians.append("The Great " + magicians.pop())
make_great(magicians, greatMagicians)
show_magicians(greatMagicians)
show_magicians(magicians)

'''
	8-11: Copying lists for us in functions.
	
	It's great that they're great, but it's easy
	to be great.  Time to make carbon copies of
	their act!
'''
copyCats = []
magicians = ['Abra','Kadabra','Alakazam','Hypno',
		'David Blaine'
	]
make_great(magicians[:], copyCats)
show_magicians(copyCats)
show_magicians(magicians)