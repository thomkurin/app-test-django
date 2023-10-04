from django.urls import path
from . import views

urlpatterns = [
    path('adicionar/<int:produto_id>/', views.adicionar_carrinho, name='adicionar_carrinho'),
    path('visualizar/', views.visualizar_carrinho, name='visualizar_carrinho'),
    path('remover/<int:item_id>/', views.remover_do_carrinho, name='remover_do_carrinho'),
]
