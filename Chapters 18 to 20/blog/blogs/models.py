from django.db import models
from django.contrib.auth.models import User

class BlogPost(models.Model):
	title = models.CharField(max_length=75)
	text = models.TextField()
	date_added = models.DateTimeField(auto_now_add=True)
	owner = models.ForeignKey(
		User,
		on_delete=models.CASCADE
	)
	
	class Meta:
		verbose_name_plural = 'blogposts'
	
	def __str__(self):
		return self.title + "\n" + self.text