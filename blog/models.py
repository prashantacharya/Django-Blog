from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.
class Category(models.Model):
	category_name = models.CharField(max_length=64)

	def __str__(self):
		return self.category_name

class Post(models.Model):
	author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
	title = models.CharField(max_length=200)
	text = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)
	cover = models.ImageField(upload_to="blog/static/images/", null=False)
	category = models.ManyToManyField(Category, blank = False)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title
