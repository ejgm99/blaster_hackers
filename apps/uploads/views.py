from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

import json
# Create your views here.

#importing from inventory/task app to write items to database
from apps.inventory.models import Item
from apps.projects.models import Component, Project
from apps.projects.resources import ComponentResource, ProjectResource
from apps.inventory.resources import ItemResource
import tablib #python library that makes it easier to upload data
#views for uploads app
from .parsing import parseProjectContent


def index(request):
    template = loader.get_template('template.html')
    return HttpResponse(template.render({}, request));

def components(request):
    if request.method == 'POST':
        data = parseProjectContent(request.POST)
        if data != False:
            component_headers = ['id', 'title', 'projectID', 'description'] #
            upload(ComponentResource(),data,component_headers) #
    return render(request, 'uploads/upload.html')


def upload(resource, data, headers):
    try:
        c = Component.objects.get(title = data[1])
        c.description = data[3] #
        c.save()
    except Component.DoesNotExist:
        print("Importing new")
        importNew(resource,data,headers)


def updateItem(resource, title, description):
    try:
        resource.objects.get(title = title)
    except resource.DoesNotExist:
        importNew(resource, data, header_list)


def importNew(resource, data, header_list):
    data_set = tablib.Dataset(data, headers = header_list)
    result = resource.import_data(data_set, dry_run = True)
    if not result.has_errors():
        #print("----Uploaded "+data[1]+ " as " + str(resource))
        resource.import_data(data_set, dry_run = False)
    else:
        print("Errors")

def getUrlDict(chunk): #gets dictionary to reformat text for url
    url_dict = {}
    for url_pair in prepareCSVForImport(chunk)[1:]:
        key, value = url_pair.replace(" ", "").split('|')
        url_dict[key] = value
        return url_dict


def inventory(request):
    if request.method == 'POST':
        print("INVENTORY UPLOAD BEGINNING")
        for chunk in request.FILES['log']:
            chunk = prepareCSVForImport(chunk)
            if(len(chunk)>1):
                try:
                    #Item.objects.filter(title = chunk[1]).quantity +=int(chunk[3])
                    item = Item.objects.get(title = chunk[1])
                    item.quantity += int(chunk[3])
                    item.save()
                except(Item.DoesNotExist):
                    headers = ["id", "title", "price", "quantity", "link"]
                    importNew(ItemResource(), chunk, headers)
                    template = loader.get_template('template1.html')
                    return render(request, 'uploads/upload.html')


def prepareCSVForImport(chunk): #takes line from csv file and parses for values to be added as new item to import
    chunk = (str(chunk)[2:-3]).split(',')
    if chunk[-1][1:] == "\\r":
        chunk[-1] = chunk[-1][0]
        if len(chunk[0]) and (chunk[0] != "Name"):
            chunk = prepareCSVData(chunk)
            return chunk
            return [""]

def prepareCSVData(chunk):
    return [""] +chunk[:-3]+chunk[4:-1]
