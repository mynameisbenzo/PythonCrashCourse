from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse
	
'''
	create new user
'''
def register(request):
	if request.method != 'POST':
		# blank form
		form = UserCreationForm()
	else:
		# process completed form
		form = UserCreationForm(data=request.POST)
		
		if form.is_valid():
			new_user = form.save()
			# log user in and redirect to home page
			authenticated_user = authenticate(username=new_user.username,
				password=request.POST['password1'])
			login(request, authenticated_user)
			return HttpResponseRedirect(reverse('index'))
		
	context = {'form':form}
	return render(request, 'users/register.html', context)