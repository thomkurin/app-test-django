from django.contrib import admin
from django.urls import path, include
from produtos.views import lista_produtos 
from usuarios.views import login, registrar_usuario

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login, name='pagina_de_login'),
    path('produtos/', include('produtos.urls')),
    path('registro/', include('usuarios.urls')),
]