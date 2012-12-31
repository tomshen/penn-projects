from django.db import models

APPROVAL = (
	(True, 'Approved'),
	(False, 'Pending approval'))

class Project(models.Model):
	name = models.CharField('project name', max_length=50)
	sub_date = models.DateTimeField('date submitted', editable=False)
	authors = models.TextField(max_length=100) # list of author names separated by commas
	demo_url = models.URLField()
	description = models.TextField()
	album_url = models.URLField()
	pitch = models.TextField(max_length=200)
	source_url = models.URLField()
	thumbnail_url = models.URLField()
	approved = models.BooleanField(choices=APPROVAL)

	def __unicode__(self):
		return self.name