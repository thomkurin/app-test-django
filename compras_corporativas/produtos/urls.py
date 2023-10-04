from django.urls import path
from . import views
from compras.views import criar_pedido

urlpatterns = [
    path('novo/', views.novo_produto, name='novo_produto'),
    path('<int:produto_id>/', views.detalhes_produto, name='detalhes_produto'),
    path('<int:produto_id>/editar/', views.editar_produto, name='editar_produto'),
    path('<int:produto_id>/excluir/', views.excluir_produto, name='excluir_produto'),
    path('criar_pedido/', views.criar_pedido, name='criar_pedido'),
    path('lista/', views.lista_produtos, name='lista_produtos'),
]
