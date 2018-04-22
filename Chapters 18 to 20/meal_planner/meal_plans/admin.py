from django.contrib import admin

from meal_plans.models import Meal, Food

admin.site.register(Meal)
admin.site.register(Food)