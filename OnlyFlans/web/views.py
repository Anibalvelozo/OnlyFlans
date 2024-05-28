from django.shortcuts import render, redirect
from .models import Flan, ContactForm
from .forms import ContactFormModelForm

def index(request):
    flanes = Flan.objects.filter(is_private=False)
    return render(request, 'index.html', {'flanes': flanes})

def bienvenido(request):
    flanes = Flan.objects.filter(is_private=True)
    return render(request, 'welcome.html', {'flanes': flanes})

def acerca(request):
    return render(request, 'about.html')

def contacto(request):
    if request.method == 'POST':
        form = ContactFormModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('exito')
    else:
        form = ContactFormModelForm()
    return render(request, 'contact.html', {'form': form})

def exito(request):
    return render(request, 'exito.html')
