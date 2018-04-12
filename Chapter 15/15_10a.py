'''
	Problem 10:
		A) Matplotlib on die rolling
'''
import matplotlib.pyplot as plt

from die import Die

die = Die()

results = []
for roll_num in range(5000):
	result = die.roll()
	results.append(result)
	
# y axis values
frequencies = []
for value in range(1, die.num_sides+1):
	frequency = results.count(value)
	frequencies.append(frequency)

x_vals = [str(x) for x in range(1, die.num_sides+1)]
print(frequencies)

plt.scatter(x_vals, frequencies, linewidth=5)
plt.title("Die Rolling Results", fontsize=24)
plt.xlabel("Values rolled", fontsize=14)
plt.ylabel("Frequency of value rolled", fontsize=14)

plt.tick_params(axis='both', labelsize=14)

plt.show()