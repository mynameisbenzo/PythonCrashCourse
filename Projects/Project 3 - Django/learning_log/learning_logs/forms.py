from django import forms

from .models import Topic

class TopicForm(froms.ModelForm):
	class meta:
		model = Topic
		fields = ['text']
		labels = {'text':''}