from die import Die

# create a d6
die = Die()

# roll and store the results
results = []
for roll_num in range(1000):
	result = die.roll()
	results.append(result)
	
# analyze results
frequencies = []
for value in range(1, die.num_sides+1):
	frequency = results.count(value)
	frequencies.append(frequency)
	
print(frequencies)