# 18-2:
### Goal:
##### Currently, the Entry model cuts the first 50 characters out of the text and appends an  ellipsis.  Alter the __str__ method to not  append an elipsis if the length of the text is less than 50.
# 18-3:
### Goal:
##### Writing code to access data in your project is the same as using a query.  Look over the Django API documentation about queries to get a more in depth look about them.
# 18-4:
### Goal:
##### Create a new project called pizzeria with an app called pizzas.  Define a model Pizza with a field with a field called name, which will hold name values such as 'Hawaiian' and 'Meat Lovers'.  Do the same with Topping with fields for pizza and name using Pizza as a foreign key.
# 18-5:
### Goal:
##### Create an app that helps people plan their meals. Make sure the app has a home page.
# 18-6:
### Goal:
##### Go back to pizzeria and add a homepage to the app.
# 18-7:
### Goal:
##### Read Django documentation to learn more about templates
# 18-8:
### Goal:
##### In Pizzeria, add a page to pizzeria that shows the pizza names.  Then display each pizza's topping when a pizza name is clicked.
# 19-1:
### Goal:
##### Create a blog app that allows users to create and edit blog posts.
# 19-2:
### Goal:
##### Create a registration, login, and logout system for the blog project.  Also, display logged-in users name while logged-out/non-users see a register link
# 19-3:
### Goal:
##### Refactor views.py in learning_log/learning_logs by turning code that is used twice into a function
# 19-4:
### Goal: 
##### Prevent users from adding to another users learning log by checking the current user matches the topic owner
# 19-5:
### Goal: 
##### In the blog project, connect all posts to a user.  Let all posts be visible but only registered users can post and edit. users can only edit their own posts.