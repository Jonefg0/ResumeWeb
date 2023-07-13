from django.shortcuts import render, HttpResponse

# Create your views here.

html_base = """
<h1> Welcome to my page </h1>
<ol>
    <li><a href="/">Portada</a></li>
    <li><a href="/about-me">Acerca de</a></li>
    <li><a href="/contact">Contacto</a></li>
    <li><a href="/portfolio"> Portfolio </a></li>
<ol>
"""

def home(request):
    print("accesing to home view from core")
    return render(request, "core/core.html")


def about(request):
    print("accesing to about ..")
    return render(request, "core/about-me.html")


def portfolio(request):
    print("accessing to portafolio...")
    return render(request, "core/portfolio.html")
                        
def contact(request):
    print("accessing to contact...")
    return render(request, "core/contact.html")