from django.forms import ModelForm
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
        if 'demo_url' in self._errors:
            del self._errors['demo_url']
        if 'album_url' in self._errors:
            del self._errors['album_url']
        if 'source_url' in self._errors:
            del self._errors['source_url']
        if 'thumbnail_url' in self._errors:
            del self._errors['thumbnail_url']

        for k in self.cleaned_data.keys():
            self.cleaned_data[k] = strip_tags(self.cleaned_data[k])
        return self.cleaned_data