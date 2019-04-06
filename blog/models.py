from django.db import models

class Blog(models.Model):
	title = models.CharField(max_length=250)
	published_date = models.DateTimeField()
	body = models.TextField()
	image = models.ImageField(upload_to='images/')

	def __str__(self):
		return self.title

	def summary(self):
		return self.body[:140]

	def publish(self):
		return self.published_date.strftime('%b %d %Y')
