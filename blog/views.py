from django.shortcuts import render
import markdown
from blog.models import Post

# Create your views here.
def home(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts': posts, 'title': 'Pakito'})


def article(request, slug):
    post = Post.objects.filter(slug__exact=slug)[0]
    return render(request, 'article_detail.html', {'post': post, 'title': post.title})

