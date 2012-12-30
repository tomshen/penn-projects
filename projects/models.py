from django.db import models
import datetime
from django.utils import timezone

class Project(models.Model):
	name = models.CharField(max_length=200)
	sub_date = models.models.DateTimeField('date submitted')
	authors = models.TextField(max_length=200) # list of author names separated by '\n'
	demo_url = models.URLField()
	description = models.TextField()
	album_url = models.URLField()
	description = models.TextField(max_length=200)
	source_url = models.URLField()