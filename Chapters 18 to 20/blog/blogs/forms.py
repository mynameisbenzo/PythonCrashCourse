from django.forms import ModelForm, Textarea, CharField

from .models import BlogPost

class BlogPostForm(ModelForm):
	class Meta:
		model = BlogPost
		fields = ('title', 'text')