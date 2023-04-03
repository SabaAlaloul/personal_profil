from django.shortcuts import render
from projects.models import project


# Create your views here.
def project_index (request):
    projects = project.objects.all()

    context = {
        'projects':projects
    }
    return render(request, 'project_index.html', context)


def project_details(request, pk):
    Project = project.objects.get(pk=pk)
    context = {
        'Project':Project
    }
    return render(request,'project_details.html', context)

