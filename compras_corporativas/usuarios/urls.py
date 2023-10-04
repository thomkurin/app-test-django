from django.urls import path
from . import views

urlpatterns = [
    path('registro/', views.registrar_usuario, name='registro'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('perfil/', views.perfil, name='perfil'),
]