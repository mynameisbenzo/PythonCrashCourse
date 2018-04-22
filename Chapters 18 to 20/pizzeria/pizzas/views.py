from django.shortcuts import render

from .models import Pizza

'''
	home page
'''
def index(request):
	return render(request, 'pizzas/index.html')
	
'''
	list of pizza names
'''
def pizzas(request):
	pizzas = Pizza.objects.order_by('date_added')
	context = {'pizzas':pizzas}
	return render(request, 'pizzas/pizzas.html', context)
	
'''
	single pizza and the toppings for said pizza
'''
def pizza(request, pizza_id):
	pizza = Pizza.objects.get(id=pizza_id)
	toppings = pizza.topping_set.order_by('-date_added')
	context = {'pizza':pizza, 'toppings':toppings}
	return render(request, 'pizzas/pizza.html', context)