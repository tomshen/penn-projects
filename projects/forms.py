from django.forms import ModelForm, ValidationError
from projects.models import Project
from django.utils.html import strip_tags

class ProjectForm(ModelForm):

    class Meta:
        model = Project
        exclude = ('approved', )

    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)
        self.fields['authors'].widget.attrs['rows'] = 3
        self.fields['description'].widget.attrs['rows'] = 10
        self.fields['pitch'].widget.attrs['rows'] = 3

    def clean(self):
        super(ProjectForm, self).clean()
        if 'album_url' in self.cleaned_data and self.cleaned_data['album_url']:
            if 'imgur.com/a/' not in self.cleaned_data['album_url']:
                raise ValidationError('Not a valid imgur album url')
        for k in self.cleaned_data.keys():
            self.cleaned_data[k] = strip_tags(self.cleaned_data[k])
        return self.cleaned_data