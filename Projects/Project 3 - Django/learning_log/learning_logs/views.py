from django.shortcuts import render

from .models import Topic

'''
	the home page for learning log
'''
def index(request):
	return render(request, 'learning_logs/index.html')
	
'''
	show all topics
'''
def topics(request):
	topics = Topic.objects.order_by('date_added')
	context = {'topics': topics}
	return render(request, 'learning_logs/topics.html', context)
	
'''
	show a single topic and all its entries
'''
def topic(request, topic_id):
	topic = Topic.objects.get(id=topic_id)
	entries = topic.entry_set.order_by('-date_added')
	context = {'topic':topic, 'entries':entries}
	return render(request, 'learning_logs/topic.html', context)