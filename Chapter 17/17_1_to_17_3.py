'''
	17-1: 
		Github repo API call for a different language
		
		Resolved here.
		
	17-2:
		Alter hn_submissions to portray the data using a 
		bar chart.  
		
		Resolved in hn_submissions.py
	
	17-3:
		create unittest testcases to check status code of
		requests call.
		
		Resolved within Projects 2 directory.
'''


import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

# make an api call and store the response
url = ("https://api.github.com/search/repositories?q=language:" +
		"swift&sort=stars")
r = requests.get(url)
print("Status code: ", r.status_code)

# store api response in a variable
response_dict = r.json()
print("Total repositories: ", response_dict['total_count'])

# explore information about the repositories
repo_dicts = response_dict['items']

names, plot_dicts = [],[]
for repo_dict in repo_dicts:
	names.append(repo_dict['name'])
	
	# check if description exists to prevent errors
	if repo_dict['description'] == None:
		continue
	plot_dict = {
		'value':repo_dict['stargazers_count'],
		'label':repo_dict['description'],
		'xlink':repo_dict['html_url'],
	}
	plot_dicts.append(plot_dict)
	
# make a visualization
my_style = LS('#333366', base_style=LCS)

my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 18
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000

chart = pygal.Bar(my_config, style=my_style)
chart.title = 'Most-Starred Swift Projects on Github'
chart.x_labels = names

chart.add('', plot_dicts)
chart.render_to_file('swift_repos.svg')