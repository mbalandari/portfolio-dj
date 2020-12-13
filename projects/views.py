from django.shortcuts import render
from .models import Project

def home(request):
    sections = Project.objects.all()
    return render(request, 'portfolio/home.html', {'sections':sections})
