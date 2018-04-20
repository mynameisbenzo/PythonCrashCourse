import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

from operator import itemgetter

# make an api call and store the response
url = "https://hacker-news.firebaseio.com/v0/topstories.json"
r = requests.get(url)
print("Status code: ", r.status_code)

# process information about each submission
submission_ids = r.json()
users, submission_dicts = [], []
for submission_id in submission_ids[:30]:
	# make a seperate api call for each submission
	url = ('https://hacker-news.firebaseio.com/v0/item/' +
			str(submission_id) + '.json')
	submission_r = requests.get(url)
	print(submission_r.status_code)
	response_dict = submission_r.json()
	
	submission_dict = {
		'value':response_dict.get('descendants',0),
		'label':response_dict['title'],
		'xlink':'https://news.ycombinator.com/item?id=' + str(submission_id),
	}
	submission_dicts.append(submission_dict)
	
submission_dicts = sorted(submission_dicts, key=itemgetter('value'),
							reverse=True)

for submission_dict in submission_dicts:
	print("\nUser: ", submission_dict['value'])
	print("Discussion Link: ", submission_dict['xlink'])
	print("Title: ", submission_dict['label'])
	
# make the visualization
my_style = LS("#111133", base_style=LCS)

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
chart.title = 'Most Active articles on Hacker News'
# chart.x_labels = names

chart.add('',submission_dicts)
chart.render_to_file('hacker_news_activity.svg')