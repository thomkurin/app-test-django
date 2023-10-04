from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.lista_produtos, name='lista_produtos'),
    path('produto/<int:produto_id>/', views.detalhes_produto, name='detalhes_produto'),
    path('produtos/', include('produtos.urls')),
    path('carrinho/', include('carrinho.urls')),
    path('usuarios/', include('usuarios.urls')),
    path('criar_pedido/<int:produto_id>/', views.criar_pedido, name='criar_pedido'),
    path('produtos/', include('produtos.urls')),
]
