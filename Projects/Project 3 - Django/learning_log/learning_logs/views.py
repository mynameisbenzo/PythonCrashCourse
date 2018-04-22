from django.shortcuts import render

'''
	the home page for learning log
'''
def index(request):
	print("ayy")
	return render(request, 'learning_logs/index.html')