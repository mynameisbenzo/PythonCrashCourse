from django.shortcuts import render

'''
	the home page for learning log
'''
def index(request):
	print("ayy")
	return render(request, 'meal_plans/index.html')