from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from web.views import index, bienvenido, acerca, contacto, exito, custom_logout, like_flan

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('bienvenido/', bienvenido, name='bienvenido'),
    path('acerca/', acerca, name='acerca'),
    path('contacto/', contacto, name='contacto'),
    path('exito/', exito, name='exito'),

    # Agregando rutas para autenticación
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', custom_logout, name='logout'),

    # Incluyendo las URLs por defecto de auth para que gestionen el resto
    path('accounts/', include('django.contrib.auth.urls')),

    # Ruta para dar like a un flan
    path('flan/<int:flan_id>/like/', like_flan, name='like_flan'),
]
