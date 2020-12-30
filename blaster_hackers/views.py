from django.shortcuts import render

def index(request):
    context = {"root":"http://127.0.0.1:8000"}
    return render(request, 'home/home.html', context)
