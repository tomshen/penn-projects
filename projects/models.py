from django.db import models

APPROVAL = (
	(True, 'Approved'),
	(False, 'Pending approval'))

class Project(models.Model):
	name = models.CharField('project name', max_length=50)
	sub_date = models.DateTimeField('date submitted', editable=False)
	authors = models.TextField(max_length=100)
	demo_url = models.URLField(blank=True)
	description = models.TextField()
	album_url = models.URLField(blank=True)
	pitch = models.TextField(max_length=200)
	source_url = models.URLField(blank=True)
	thumbnail_url = models.URLField(blank=True)
	approved = models.BooleanField(choices=APPROVAL)

	def __unicode__(self):
		return self.name