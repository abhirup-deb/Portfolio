from django.db import models
from django.utils import timezone
from django.conf import settings

class Blog(models.Model):
	title = models.CharField(max_length=250)
	pub_date = models.DateTimeField(auto_now_add=True,
            blank=True, null=True)
	body = models.TextField()
	image = models.ImageField(upload_to='images/')

	def __str__(self):
		return self.title

	def summary(self):
		return self.body[:140]

	def pub_date_pretty(self):
		return self.pub_date.strftime('%b %e %Y')
