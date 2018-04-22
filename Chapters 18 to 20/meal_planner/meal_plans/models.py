from django.db import models

class Meal(models.Model):
	name = models.CharField(max_length=200)
	date_added = models.DateTimeField(auto_now_add=True)
	
	def __str__(self):
		return self.name
		
class Food(models.Model):
	meal = models.ForeignKey(
		Meal,
		on_delete=models.CASCADE
	)
	description = models.TextField()
	calories = models.IntegerField()
	date_added = models.DateTimeField(auto_now_add=True)
	
	class Meta:
		verbose_name_plural = "description_calories"
		
	def __str__(self):
		str_return = "Description: "
		if len(self.description) < 50:
			str_return += self.description
		else:
			str_return += self.description[:50]
		return str_return + " Calories: " + str(self.calories)