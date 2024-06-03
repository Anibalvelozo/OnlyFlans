from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from web.views import index, bienvenido, acerca, contacto, exito

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('bienvenido/', bienvenido, name='bienvenido'),
    path('acerca/', acerca, name='acerca'),
    path('contacto/', contacto, name='contacto'),
    path('exito/', exito, name='exito'),

    # Agregando rutas para autenticación
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),

    # Incluyendo las URLs por defecto de auth para que gestionen el resto
    path('accounts/', include('django.contrib.auth.urls')),
]
