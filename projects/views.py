from django.template import Context, loader
from projects.models import Project
from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response, get_object_or_404

def index(request):
    latest_projects = Project.objects.all().order_by('-sub_date')[:5]
    t = loader.get_template('projects/index.html')
    c = Context({
        'latest_projects': latest_projects,
    })
    return HttpResponse(t.render(c))

def display(request, project_id):
    p = get_object_or_404(Project, pk=project_id)
    return render_to_response('projects/display.html', {'project': p})
