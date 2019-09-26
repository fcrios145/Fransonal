from django.shortcuts import render, redirect, reverse
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as do_login
from django.contrib.auth import logout as do_logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import View, DetailView, CreateView, UpdateView
from .forms import ArticleForm
from .models import Article


class HomeView(View):
    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()
        return render(request, 'index.html', {'authenticated': request.user.is_authenticated, 'articles': articles})


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article.html'
    context_object_name = 'article'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['authenticated'] = self.request.user.is_authenticated
        return context


@method_decorator(login_required, name='dispatch' )
class ArticleCreateView(CreateView):
    model = Article
    template_name = 'new_article.html'
    form_class = ArticleForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['authenticated'] = self.request.user.is_authenticated
        return context

    def form_valid(self, form):
        form.save()
        return redirect(reverse("editar_articulo", kwargs={
            'slug': form.instance.slug
        }))


@method_decorator(login_required, name='dispatch')
class ArticleUpdateView(UpdateView):
    model = Article
    template_name = 'new_article.html'
    form_class = ArticleForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['authenticated'] = self.request.user.is_authenticated
        return context

    def form_valid(self, form):
        form.save()
        return redirect(reverse("editar_articulo", kwargs={
            'slug': form.instance.slug
        }))


def logout(request):
    do_logout(request)
    return redirect('home')


class LoginView(View):
    def post(self, request, *args, **kwargs):
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username=username, password=password)
            if user is not None:
                do_login(request, user)
                return redirect(request.GET.get('next'))
        return render(request, 'login.html')

    def get(self, request, *args, **kwargs):
        form = AuthenticationForm()
        return render(request, 'login.html')

