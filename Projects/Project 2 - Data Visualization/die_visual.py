import pygal

from die import Die

# create a d6
die_1 = Die()
die_2 = Die(10)

# roll and store the results
results = []
for roll_num in range(50000):
	result = die_1.roll() + die_2.roll()
	results.append(result)
	
# analyze results
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(1, max_result+1):
	frequency = results.count(value)
	frequencies.append(frequency)
	
# visualize results
hist = pygal.Bar()
hist.title = "Results of rolling one d6 1000 times"
hist.x_labels = [str(x) for x in range(1,max_result+1)]
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6 + D10', frequencies)
hist.render_to_file('die_visual.svg')