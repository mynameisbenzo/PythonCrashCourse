import pygal

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
	
# visualize results
hist = pygal.Bar()

hist.title = "Results of rolling one d6 1000 times"
hist.x_labels = [str(x) for x in range(1,7)]
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6', frequencies)
hist.render_to_file('die_visual.svg')