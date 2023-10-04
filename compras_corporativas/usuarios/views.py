from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm

def registrar_usuario(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1']) 
            user.save()
            return redirect('login') 
    else:
        form = CustomUserCreationForm()
    return render(request, 'usuarios/registro.html', {'form': form})

def login(request):
    if request.method == 'POST':
        login_form = AuthenticationForm(request, data=request.POST)
        if login_form.is_valid():
            user = login_form.get_user()
            auth_login(request, user)
            return redirect('lista_produtos')
    else:
        login_form = AuthenticationForm()

    if request.method == 'POST' and 'register' in request.POST:
        register_form = CustomUserCreationForm(request.POST)
        if register_form.is_valid():
            user = register_form.save(commit=False)
            user.set_password(register_form.cleaned_data['password1'])
            user.save()
            auth_login(request, user)
            return redirect('lista_produtos')
    else:
        register_form = CustomUserCreationForm()

    return render(request, 'usuarios/login.html', {'login_form': login_form, 'register_form': register_form})

@login_required
def logout(request):
    auth_logout(request)
    return redirect('lista_produtos')

@login_required
def perfil(request):
    return render(request, 'usuarios/perfil.html')
