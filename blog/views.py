from django.shortcuts import render
import markdown
from blog.models import Post, Post2

# Create your views here.
def home(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts': posts, 'title': 'Pakito'})


def article(request, slug):
    post = Post2()
    return render(request, 'article_detail.html', {'post': post, 'title': "sad"})

