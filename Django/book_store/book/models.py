from django.db import models
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.
class Books(models.Model):
	title=models.CharField(max_length=50)
	rating=models.IntegerField()
	author=models.CharField(null=True,max_length=100)
	bestSeller=models.BooleanField(default=False)
	desc=models.TextField(blank=True)
	slug=models.SlugField(default="",null=False)
	
	def get_absolute_urls(self):
		return reverse("book_detail", args=[self.slug])
	
	def save(self,*args,**kwargs):
		self.slug=slugify(self.title)
		super().save(*args,**kwargs)
		
	def __str__(self):
		return f"{self.title} ({self.rating})"
		