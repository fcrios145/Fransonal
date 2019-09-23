from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as do_login
from django.contrib.auth import logout as do_logout
from django.contrib.auth.decorators import login_required
from .forms import ArticleForm


# Create your views here.
def home(request):
    return render(request, 'index.html')


def article(request):
    return render(request, 'article.html')


@login_required(login_url='login')
def new_article(request):
    if(request.method == 'POST'):
        form = ArticleForm(request.POST)
        print(request.POST["raw_content"])
    else:
        form = ArticleForm()
    return render(request, 'new_article.html', {'authenticated': request.user.is_authenticated, 'form': form})


def logout(request):
    do_logout(request)
    return redirect('/')


def login(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # Recuperamos las credenciales validadas
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Verificamos las credenciales del usuario
            user = authenticate(username=username, password=password)

            # Si existe un usuario con ese nombre y contraseña
            if user is not None:
                # Hacemos el login manualmente
                do_login(request, user)
                # Y le redireccionamos a la portada
                return redirect('/')

    return render(request, 'login.html')
