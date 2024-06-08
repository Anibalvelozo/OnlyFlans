from django.shortcuts import render, redirect
from .models import Flan, ContactForm
from django.contrib.auth.decorators import login_required
from .forms import ContactFormModelForm
from django.contrib.auth import logout as auth_logout
from django.contrib import messages

def index(request):
    flanes = Flan.objects.filter(is_private=False)
    return render(request, 'index.html', {'flanes': flanes})

@login_required
def bienvenido(request):
    flanes_privados = Flan.objects.filter(is_private=True)
    return render(request, 'bienvenido.html', {'flanes': flanes_privados})

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

def custom_logout(request):
    auth_logout(request)
    messages.success(request, "Has cerrado sesión exitosamente.")
    return redirect('index')
