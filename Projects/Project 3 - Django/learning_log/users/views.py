from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import UserCreationForm

'''
	log the user out
'''

# found a different way as pointed out in this StackOverflow question
# https://stackoverflow.com/questions/25274104/logout-page-not-working-in-django
def logout_view(request):
	logout(request)
	return HttpResponseRedirect(reverse('learning_logs:index'))
	
'''
	register a new user
'''
def register(request):
	if request.method != 'POST':
		# blank registration form
		form = UserCreationForm()
	else:
		# process completed form
		form = UserCreationForm(data=request.POST)
		
		if form.is_valid():
			new_user = form.save()
			# log the user in and redirect to home page
			authenticated_user = authenticate(username=new_user.username,
				password=request.POST['password1'])
			login(request, authenticated_user)
			return HttpResponseRedirect(reverse('index'))
	
	context = {'form':form}
	return render(request, 'users/register.html', context)