from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

app_name = 'users'
urlpatterns =[
	# login page
	path('login/$', auth_views.login, {'template_name': 'users/login.html'}, name='login'),	
	
	# logout page
	path('logout/$', auth_views.logout, {'template_name': 'index.html', 'next_page':'/'}, name='logout'),
	
	# registration page
	path('register/$', views.register, name='register')
]