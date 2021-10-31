from django.shortcuts import render
from .models import Post
# Create your views here.
def index(request):
    posts = Post.objects.filter(status='Published')
    return render(request, 'index.html',{'posts' : posts})

def article(request, slug):
    post = Post.objects.get(slug=slug)
    return render(request, 'article.html',{'post' : post})

def signup(request):
    return render(request, 'signup.html',)

def signin(request):
    return render(request, 'signin.html',)
