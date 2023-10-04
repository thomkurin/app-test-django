from django.db import models
from produtos.models import Produto

class CarrinhoItem(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField(default=1)

    def subtotal(self):
        return self.produto.preco * self.quantidade
