'''
	Problem 10:
		B) Visualize Random Walk with pygal
'''
import pygal

from random_walk import RandomWalk

rw = RandomWalk()
rw.fill_walk()

walk_vis = pygal.XY(stroke=False)

walk_vis.add("",
	[(rw.x_values[val], rw.y_values[val])
		for val in range(len(rw.x_values))])

# for val in range(len(rw.x_values)):
	# walk_vis.add("",(rw.x_values[val],rw.y_values[val]))
	
# print(rw.x_values)
# print(rw.y_values)
	
walk_vis.title = 'Random Walk'
walk_vis.show_x_labels = False
walk_vis.show_y_labels = False
walk_vis.show_legend = False
walk_vis.render_to_file('10b_visual.svg')