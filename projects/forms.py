from django.forms import ModelForm
from projects.models import Project
from django.utils import timezone

class ProjectForm(ModelForm):

    class Meta:
        model = Project
        exclude = ('approved', )

    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)
        self.fields['authors'].widget.attrs['rows'] = 3
        self.fields['description'].widget.attrs['rows'] = 10
        self.fields['pitch'].widget.attrs['rows'] = 3