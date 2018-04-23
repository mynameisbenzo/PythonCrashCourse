from django.urls import path

from . import views

app_name = "blogs"

urlpatterns = [
	# home page
	path('', views.index, name='index'),
	
	# add new post
	path('new_post/$', views.new_post, name='new_post'),
	
	# edit previous posts
	path('edit_post/<post_id>/$', views.edit_post, name='edit_post'),
]