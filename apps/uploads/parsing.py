import json

#importing from inventory/task app to write items to database
from apps.inventory.models import Item
from apps.projects.models import Component, Project
from apps.projects.resources import ComponentResource, ProjectResource
from apps.inventory.resources import ItemResource

import tablib

def getContentData(j):
    data = json.loads(j['d']) #parsing out the JSON object
    title = data['title']
    project = data['project']
    description = data['text']
    print(title)
    id = getProjectID(project)  #
    if project ==title: #this means it's the introduction for the particular project
        # print("--------Updating description for: ", project)
        Project.objects.filter(title=project).update(description=description)
        # print("yooooooooo")
        # print(Project.objects.get(title=project).description)
        return False
    else: #it's the project
        #print("----Uploading to project ID:", id)
        return ['',title, id, description]

def getProjectID(project): #returns id of component the project is for, if it doesn't have one it creates one
    try:
        project_id = Project.objects.get(title=project).id
    except Project.DoesNotExist: #checks the title of the doc parsed to see if this is a new project. If it is, uploads new project into database
        task_data = ['',project, "This is a new project. Please update description in admin"]
        task_headers = ['id', 'title', 'description']
        importNew(ProjectResource(), task_data, task_headers)
        project_id = Project.objects.get(title=project).id
    # print("--Got projectID: ",project_id)
    return project_id

def importNew(resource, data, header_list):
    data_set = tablib.Dataset(data, headers = header_list)
    result = resource.import_data(data_set, dry_run = True)
    if not result.has_errors():
        #print("----Uploaded "+data[1]+ " as " + str(resource))
        resource.import_data(data_set, dry_run = False)
    else:
        print("Errors")

def parseProjectContent(data):
    print("Parsing data", type(data))
    data = getContentData(data)
    return data
