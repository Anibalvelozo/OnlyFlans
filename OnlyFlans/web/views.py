from django.shortcuts import render
from .models import Flan

# Create your views here.
def indice(request):
    flanes= Flan.objects.all()
    context = {
        'flanes':flanes
    }
    return render(request, 'index.html', context)

def acerca(request):
    return render(request, 'about.html', {})

def bienvenido(request):
    return render(request, 'welcome.html', {})
