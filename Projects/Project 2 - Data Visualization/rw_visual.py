import matplotlib.pyplot as plt

from random_walk import RandomWalk

#keep making new walks if the program is active
while True:
	# make a random walk and plot points
	rw = RandomWalk()
	rw.fill_walk()
	
	# set plotting window size
	plt.figure(dpi=170, figsize=(10,6))

	point_numbers = list(range(rw.num_points))
	plt.plot(rw.x_values, rw.y_values)
		
	# emphasize first and last points
	# plt.plot(0, 0, c='green')
	# plt.plot(rw.x_values[-1], rw.y_values[-1], c='red')
		
	# remove the axis
	plt.axes().get_xaxis().set_visible(False)
	plt.axes().get_yaxis().set_visible(False)
	
	plt.show()
	
	keep_running = input("Make another walk? (y/n): ")
	if keep_running == 'n':
		break