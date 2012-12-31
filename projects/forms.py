from django.forms import ModelForm
from projects.models import Project
from django.utils import timezone

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        exclude = ('approved', )