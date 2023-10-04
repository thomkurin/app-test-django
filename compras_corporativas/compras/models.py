from django.db import models
from django.contrib.auth.models import User
from carrinho.models import CarrinhoItem
from django.conf import settings

class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

class Pedido(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    itens = models.ManyToManyField(CarrinhoItem)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    data_pedido = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Pedido #{self.pk} - {self.usuario.username}'