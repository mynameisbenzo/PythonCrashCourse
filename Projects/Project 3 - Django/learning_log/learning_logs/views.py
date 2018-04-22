from django.shortcuts import render

from .models import Topic

'''
	the home page for learning log
'''
def index(request):
	print("ayy")
	return render(request, 'learning_logs/index.html')
	
'''
	show all topics
'''
def topics(request):
	topics = Topic.objects.order_by('date_added')
	context = {'topics': topics}
	return render(request, 'learning_logs/topics.html', context)