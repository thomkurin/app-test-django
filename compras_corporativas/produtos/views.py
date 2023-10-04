from django.shortcuts import render, get_object_or_404, redirect
from .models import Produto, Pedido
from .forms import ProdutoForm
from carrinho.models import CarrinhoItem
from django.contrib.auth.decorators import login_required

def novo_produto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_produtos')
    else:
        form = ProdutoForm()
    return render(request, 'produtos/novo_produto.html', {'form': form})

def detalhes_produto(request, produto_id):
    produto = get_object_or_404(Produto, pk=produto_id)
    return render(request, 'produtos/detalhes_produto.html', {'produto': produto})

def editar_produto(request, produto_id):
    produto = get_object_or_404(Produto, pk=produto_id)
    if request.method == 'POST':
        form = ProdutoForm(request.POST, instance=produto)
        if form.is_valid():
            form.save()
            return redirect('detalhes_produto', produto_id=produto.id)
    else:
        form = ProdutoForm(instance=produto)
    return render(request, 'produtos/editar_produto.html', {'form': form, 'produto': produto})

def excluir_produto(request, produto_id):
    produto = get_object_or_404(Produto, pk=produto_id)
    produto.delete()
    return redirect('lista_produtos')

def lista_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'produtos/lista_produtos.html', {'produtos': produtos})

@login_required
def criar_pedido(request):
    carrinho_itens = CarrinhoItem.objects.filter(usuario=request.user)
    total = sum(item.subtotal() for item in carrinho_itens)

    if request.method == 'POST':
        pedido = Pedido.objects.create(usuario=request.user, total=total)
        for item in carrinho_itens:
            pedido.itens.add(item)
        carrinho_itens.delete()
        return redirect('lista_produtos')  # Modificado

    return render(request, 'compras/criar_pedido.html', {'carrinho_itens': carrinho_itens, 'total': total})


