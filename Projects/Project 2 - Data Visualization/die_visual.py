from die import Die

# create a d6
die = Die()

# roll and store the results
results = []
for roll_num in range(100):
	result = die.roll()
	results.append(result)
	
print(results)