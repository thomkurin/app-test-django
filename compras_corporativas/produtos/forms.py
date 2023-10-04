from django import forms
from .models import Produto
from django.shortcuts import render, redirect

def novo_produto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()  # Salva o produto com a categoria como uma string arbitrária
            return redirect('lista_produtos')  # Redireciona após o cadastro bem-sucedido
    else:
        form = ProdutoForm()
    return render(request, 'produtos/cadastrar_produto.html', {'form': form})

class ProdutoForm(forms.ModelForm):
    categoria = forms.CharField(max_length=100, required=False, help_text='Preencha a categoria')

    class Meta:
        model = Produto
        fields = ['nome', 'descricao', 'preco', 'categoria']