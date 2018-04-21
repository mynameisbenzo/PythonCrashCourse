from django.db import models

'''
	pizza class holds type of pizza
'''
class Pizza(models.Model):
	name = models.CharField(max_length=200)
	date_added = models.DateTimeField(auto_now_add=True)
	
	def __str__(self):
		return self.name
		
'''
	class to hold toppings for a pizza
'''
class Topping(models.Model):
	pizza = models.ForeignKey(
		Pizza,
		on_delete=models.CASCADE
	)
	toppings = models.TextField()
	date_added = models.DateTimeField(auto_now_add=True)
	
	class Meta:
		verbose_name_plural = "toppings"
		
	def __str__(self):
		if len(self.toppings) < 50:
			return self.toppings
		return self.toppings[:50] + "..."