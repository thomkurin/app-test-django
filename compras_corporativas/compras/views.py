from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Produto, Pedido
from carrinho.models import CarrinhoItem

def lista_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'compras/lista_produtos.html', {'produtos': produtos})

def detalhes_produto(request, produto_id):
    produto = get_object_or_404(Produto, pk=produto_id)
    return render(request, 'compras/detalhes_produto.html', {'produto': produto})

@login_required
def criar_pedido(request):
    carrinho_itens = CarrinhoItem.objects.filter(usuario=request.user)
    total = sum(item.subtotal() for item in carrinho_itens)

    if request.method == 'POST':
        pedido = Pedido.objects.create(usuario=request.user, total=total)
        for item in carrinho_itens:
            pedido.itens.add(item)
        carrinho_itens.delete()
        return redirect('lista_produtos')

    return render(request, 'compras/criar_pedido.html', {'carrinho_itens': carrinho_itens, 'total': total})