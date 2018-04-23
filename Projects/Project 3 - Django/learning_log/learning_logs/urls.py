'''
	Defines url patterns for learning_logs
'''

from django.urls import path

from . import views


app_name = "learning_logs"

urlpatterns = [
	# Home page
	path('', views.index, name='index'),
	
	# show all topics
	path('topics/$', views.topics, name='topics'),
	
	# detail page for a single topic
	path('topics/<topic_id>/$', views.topic, name='topic'),
	
	# letting users add new topics
	path('new_topic/$', views.new_topic, name='new_topic'),
	
	# letting users enter a new entry
	path('new_entry/<topic_id>/$', views.new_entry, name='new_entry'),
]