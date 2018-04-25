from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import BlogPost
from .forms import BlogPostForm

'''
	home page
'''
def index(request):
	blogposts = BlogPost.objects.order_by('-date_added')
	context = {'blogposts': blogposts}
	return render(request, 'blogs/index.html', context)
	
'''
	create new post
'''
@login_required
def new_post(request):
	if request.method != 'POST':
		post = BlogPostForm()
	else:
		post = BlogPostForm(request.POST)
		if post.is_valid():
			new_post = post.save(commit=False)
			new_post.owner = request.user
			new_post.save()
			return HttpResponseRedirect(reverse('index'))
			
	context = {'post':post}
	return render(request, 'blogs/new_post.html', context)

'''
	edit previous post
'''
@login_required
def edit_post(request, post_id):
	post = BlogPost.objects.get(id=post_id)
	
	# check owner against current user
	if post.owner != request.user:
		print("boom")
		raise Http404
	
	if request.method != 'POST':
		blogpost = BlogPostForm(instance=post)
	else:
		blogpost = BlogPostForm(instance=post, data=request.POST)
		if blogpost.is_valid():
			blogpost.save()
			return HttpResponseRedirect(reverse('index'))
	
	context = {'post':post, 'blogpost':blogpost}
	return render(request, 'blogs/edit_post.html', context)