from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import Topic, Entry
from .forms import TopicForm, EntryForm

'''
	the home page for learning log
'''
def index(request):
	return render(request, 'learning_logs/index.html')
	
'''
	show all topics
'''
@login_required
def topics(request):
	topics = Topic.objects.filter(owner=request.user).order_by('date_added')
	context = {'topics': topics}
	return render(request, 'learning_logs/topics.html', context)
	
'''
	show a single topic and all its entries
'''
@login_required
def topic(request, topic_id):
	topic = Topic.objects.get(id=topic_id)
	
	# make sure the topic belongs to the current user
	check_owner(topic.owner, request.user)
	
	entries = topic.entry_set.order_by('-date_added')
	context = {'topic':topic, 'entries':entries}
	return render(request, 'learning_logs/topic.html', context)
	
'''
	allow user to add a new topic
'''
@login_required
def new_topic(request):
	if request.method != 'POST':
		# no data -> blank form
		form = TopicForm()
	else:
		# data -> process data
		form = TopicForm(request.POST)
		if form.is_valid():
			new_topic = form.save(commit=False)
			new_topic.owner = request.user
			new_topic.save()
			return HttpResponseRedirect(reverse('topics'))
	
	context = {'form':form}
	return render(request, 'learning_logs/new_topic.html', context)
	
'''
	allow user to add a new entry for a topic
'''
@login_required
def new_entry(request, topic_id):
	topic = Topic.objects.get(id=topic_id)
	
	if request.method != 'POST':
		# no data -> blank form
		form = EntryForm()
	else:
		# data -> process data
		form = EntryForm(request.POST)
		if form.is_valid():
			new_entry = form.save(commit=False)
			new_entry.topic = topic
			new_entry.save()
			return HttpResponseRedirect(reverse('topic',args=[topic_id]))
	
	context = {'topic':topic, 'form':form}
	return render(request, 'learning_logs/new_entry.html', context)
	
'''
	allow users to edit previously entered entries
'''
@login_required
def edit_entry(request, entry_id):
	entry = Entry.objects.get(id=entry_id)
	topic = entry.topic
	
	# make sure the topic belongs to the current user
	check_owner(topic.owner, request.user)
		
	if request.method != 'POST':
		# fill form with current entry data
		form = EntryForm(instance=entry)
	else:
		# data -> process data
		form = EntryForm(instance=entry, data=request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('topic',args=[topic.id]))
	
	context = {'entry': entry, 'topic': topic, 'form':form}
	return render(request, 'learning_logs/edit_entry.html', context)
	
'''
	check topic owner
'''
def check_owner(owner, user):
	if topic.owner != request.user:
		raise Http404