from django.shortcuts import render
from .models import Birthday, Project

def home(request):
    # Retrieve all projects from the database
    projects = Project.objects.all()
    # Render the 'home.html' template with the projects data
    return render(request, 'portfolio/home.html', {'projects':projects})

def birthday(request):
    # Render the 'birthday.html' template
    return render(request, 'portfolio/birthday.html')

def submit_birthday(request):
    if request.method == 'POST':
        names = request.POST.getlist('name[]')
        #dinners = request.POST.getlist('info[]')

        for name in zip(names):
            birthday = Birthday(name=name)
            birthday.save()

        return render(request, 'portfolio/success.html')

    return render(request, 'portfolio/birthday.html')