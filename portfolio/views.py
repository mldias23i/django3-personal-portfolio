from django.shortcuts import render
from .models import Project

def home(request):
    # Retrieve all projects from the database
    projects = Project.objects.all()
    # Render the 'home.html' template with the projects data
    return render(request, 'portfolio/home.html', {'projects':projects})