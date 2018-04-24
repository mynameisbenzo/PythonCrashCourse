from django.db import models
from django.contrib.auth.models import User

''' a topic the user is learning about '''
class Topic(models.Model):
	text = models.CharField(max_length=200)
	date_added = models.DateTimeField(auto_now_add=True)
	owner = models.ForeignKey(
		User,
		on_delete=models.CASCADE
	)
	
	''' Return a string representation of the model '''
	def __str__(self):
		return self.text
		
''' something specific learned about a topic '''
class Entry(models.Model):
	'''
		The book version is deprecated.  Not only
		do you have to give the model for the 
		ForeignKey, but you also have to pass the
		what will happen when or if the entry is
		deleted.
	'''
	topic = models.ForeignKey(
		Topic,
		on_delete=models.CASCADE)
	text = models.TextField()
	date_added = models.DateTimeField(auto_now_add=True)
	
	class Meta:
		verbose_name_plural = 'entries'
		
	''' return a string representation of the model '''
	def __str__(self):
		if len(self.text) < 50:
			return self.text
		else:
			return self.text[:50] + "..."