from django.urls import path

from . import views

urlpatterns = [
	# home page
	path('', views.index, name='index'),
	
	# list of pizzas
	path('pizzas/$', views.pizzas, name='pizzas'),
	
	# single pizza with detailed info
	path('pizzas/<pizza_id>/$', views.pizza, name='pizza'),
]