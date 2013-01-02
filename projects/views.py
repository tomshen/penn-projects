from django.template import Context, loader
from projects.models import Project
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404, render
from projects.forms import ProjectForm
from django.utils import timezone

def index(request):
    latest_projects = Project.objects.all().order_by('-sub_date')[:5]
    t = loader.get_template('projects/index.html')
    c = Context({
        'latest_projects': latest_projects,
    })
    return HttpResponse(t.render(c))

def projectdisplay(request, project_id):
    p = get_object_or_404(Project, pk=project_id)
    return render_to_response('projects/projectdisplay.html', {'project': p})

def projectsubmit(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            pd = form.save(commit=False)
            pd.sub_date = timezone.now()
            pd.approved = False

            # format the authors list
            al = pd.authors.strip().replace('\r\n', '*').replace('\r', '*').replace('\n', '*').split('*')
            print al
            if len(al) > 1:
                al[-1] = 'and ' + al[-1].strip()

            if len(al) > 2:
                pd.authors = ', '.join(al)
            else:
                pd.authors = ' '.join(al)

            # make the thumbnail url a direct link if not already
            thumb = pd.thumbnail_url.strip()
            if 'imgur' in thumb and 'i.' not in thumb:
                pd.thumbnail_url = 'i.' + thumb.replace('https://', '').replace('http://', '')
            if '.jpg' not in pd.thumbnail_url:
                pd.thumbnail_url += '.jpg'

            pd.save()
            return render(request, 'projects/projectsubmit.html', {'submitted': True})
    else:
        form = ProjectForm()
    return render(request, 'projects/projectsubmit.html', {'form': form, 'submitted': False})
