from django.shortcuts import render, redirect, get_object_or_404
from .models import CarrinhoItem
from produtos.models import Produto

def adicionar_carrinho(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)
    carrinho_item, created = CarrinhoItem.objects.get_or_create(produto=produto)

    if not created:
        carrinho_item.quantidade += 1
        carrinho_item.save()

    return redirect('lista_produtos')

def visualizar_carrinho(request):
    carrinho_itens = CarrinhoItem.objects.all()
    total = sum(item.subtotal() for item in carrinho_itens)
    return render(request, 'carrinho/visualizar_carrinho.html', {'carrinho_itens': carrinho_itens, 'total': total})

def remover_do_carrinho(request, item_id):
    carrinho_item = get_object_or_404(CarrinhoItem, id=item_id)
    carrinho_item.delete()
    return redirect('visualizar_carrinho')
