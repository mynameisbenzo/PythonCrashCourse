'''
	15-1: 
		Goal: Plot first five cubic numbers
	15-2: 
		Goal: Add a colormap to the plot
'''
import matplotlib.pyplot as plt

x_values = list(range(1,6))
y_values = [y**3 for y in x_values]

plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Reds, 
	edgecolor='none', s=40)
	
plt.title("Cube numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Cube of Value", fontsize=14)

plt.tick_params(axis='both', which='major', labelsize=14)

plt.axis([0,6,0,6**3])

plt.show()