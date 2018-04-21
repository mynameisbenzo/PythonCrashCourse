from django.db import models

''' a topic the user is learning about '''
class Topic(models.Model):
	text = models.CharField(max_length=200)
	date_added = models.DateTimeField(auto_now_add=True)
	
	''' Return a string representation of the model '''
	def __str__(self):
		return self.text