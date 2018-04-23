from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import BlogPost
from .forms import BlogPostForm

def index(request):
	blogposts = BlogPost.objects.order_by('-date_added')
	context = {'blogposts': blogposts}
	return render(request, 'blogs/index.html', context)
	
def new_post(request):
	if request.method != 'POST':
		post = BlogPostForm()
	else:
		post = BlogPostForm(request.POST)
		if post.is_valid():
			new_post = post.save(commit=False)
			new_post.save()
			return HttpResponseRedirect(reverse('index'))
			
	context = {'post':post}
	return render(request, 'blogs/new_post.html', context)