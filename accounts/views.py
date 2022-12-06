from django.contrib import messages
from django.contrib.auth.models import User
from django.core.validators import validate_email
from django.shortcuts import redirect, render


# Create your views here.
def login(request):
    return render(request, 'accounts/login.html')


def logout(request):
    return render(request, 'accounts/logout.html')


def cadastro(request):
    if request.method != 'POST':
        return render(request, 'accounts/cadastro.html')

    nome = request.POST.get('nome')
    sobrenome = request.POST.get('sobrenome')
    email = request.POST.get('email')
    usuario = request.POST.get('usuario')
    senha = request.POST.get('senha')
    repetir_senha = request.POST.get('repetir_senha')

    if not nome or not sobrenome or not email or not usuario or not senha or not repetir_senha:  # noqa
        messages.error(request, 'Nenhum campo pode estar vazio.')
        return render(request, 'accounts/cadastro.html')

    try:
        validate_email(email)
    except:  # noqa
        messages.error(request, 'email inválido')
        return render(request, 'accounts/cadastro.html')

    if len(senha) < 6:
        messages.error(request, 'Senha precisa ter 6 caracteres ou mais.')
        return render(request, 'accounts/cadastro.html')

    if senha != repetir_senha:
        messages.error(request, 'Senhas não são iguais')
        return render(request, 'accounts/cadastro.html')

    if User.objects.filter(username=usuario).exists():
        messages.error(request, 'Usuário já existe.')
        return render(request, 'accounts/cadastro.html')

    if len(usuario) < 6:
        messages.error(request, 'Usuario precisa ter 6 caracteres ou mais.')
        return render(request, 'accounts/cadastro.html')

    if User.objects.filter(email=email).exists():
        messages.error(request, 'email já utilizado.')
        return render(request, 'accounts/cadastro.html')

    messages.success(request, 'registrado com sucesso! Agora faça login.')

    user = User.objects.create_user(
        username=usuario, email=email, password=senha, first_name=nome, last_name=sobrenome)  # noqa
    user.save()
    return redirect('login')


def dashboard(request):
    return render(request, 'accounts/dashboard.html')
