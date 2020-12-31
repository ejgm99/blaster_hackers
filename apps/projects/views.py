from django.shortcuts import render

# from django.contrib.staticfiles.templatetags.staticfiles import static #allows use of static files easily, use this to load images

from .models import Project
from .models import Step
from .models import Component


# Create your views here.

#the way items and projects are handled are incredibly similar,
#only major difference so far is that they will be sorted differently later.
#maybe we can abstract some behavior later on

def index(request): #index just means homepage for an app
    projects = Project.objects.all() #getting a list of all projects to display on webpage
    context = {'projects': projects} #mapping of our list to a string, which the html will use to display all of the projects
    return render(request, 'projects/index.html', context)

def project(request, project_id): #displays a project depending on id number given
	try:
		project = Project.objects.get(pk=project_id)
		steps = Step.objects.filter(projectID = project_id)
		components = Component.objects.filter(projectID = project_id)
		image_url =project.img #gets image based on what project has been loaded
	except Project.DoesNotExist:
		raise Http404("Project Does Not Exist")
	return render(request, 'projects/project.html', {'project': project, 'url':image_url, 'steps' : steps, 'components':components})

def get_image_url(project):
	return static('images/projects/'+str(project.id)+'.jpg')
