# from django import forms - DEPRECATED
from django.forms import ModelForm

from .models import Topic

class TopicForm(ModelForm):
	class Meta:
		model = Topic
		fields = ['text']
		labels = {'text':''}