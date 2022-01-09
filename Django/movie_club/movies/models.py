from django.db import models

# Create your models here.
class movies_list(models.Model):
	name=models.CharField(max_length=255)
	rating=models.FloatField()
	image=models.ImageField(max_length=2083)
	date=models.DateTimeField()
class movies(models.Model):
	name=models.CharField(max_length=255)
	rating=models.FloatField()
	type=models.CharField(max_length=255)
	
