from django.shortcuts import render, get_object_or_404
from .models import Blog

def allblogs(request):
	blogs= Blog.objects
	return render(request,'blog/templates/allblogs.html', {'blogs':blogs})

def publish(self):
        self.published_date = timezone.now()
        self.save()
