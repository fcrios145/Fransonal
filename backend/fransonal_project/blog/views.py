from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as do_login
from django.contrib.auth import logout as do_logout
from django.contrib.auth.decorators import login_required
from .forms import ArticleForm
from .models import Article


# Create your views here.
def home(request):
    articles = Article.objects.all()
    return render(request, 'index.html', {'authenticated': request.user.is_authenticated, 'articles': articles})


def article(request, slug):
    article = Article.objects.get(slug=slug)
    return render(request, 'article.html', {'authenticated': request.user.is_authenticated, 'article': article})


@login_required(login_url='login')
def new_article(request, slug=''):
    if(request.method == 'POST'):
        try:
            article =  Article.objects.get(slug=slug)
        except Article.DoesNotExist:
            article = None
        if(article):
            form = ArticleForm(request.POST, request.FILES, instance=article)
        else:
            form = ArticleForm(request.POST, request.FILES)
        if(form.is_valid()):
            form.save()
            return redirect('nuevo_articulo')
    else:
        if(slug):
            article = Article.objects.get(slug=slug)
            form = ArticleForm(instance=article)
        else:
            form = ArticleForm()

    return render(request, 'new_article.html', {'authenticated': request.user.is_authenticated, 'form': form})


def logout(request):
    do_logout(request)
    return redirect('home')


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
