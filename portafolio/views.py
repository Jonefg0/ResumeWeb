from django.shortcuts import render
from .models import Project

# Create your views here.
def portfolio(request):
    projects = Project.objects.all()
    print("accessing to portafolio...")
    return render(request, "portfolio/portfolio.html", {'projects': projects})#diccionario de contexto)