from django.shortcuts import render
from . models import Post

# Create your views here.

def index(request):
    posts = Post.objects.all()
    context = {"posts": posts}
    
    return render(request, "reddit_app/index.html", context)

def profile(request):
    user = request.user
    posts = Post.objects.filter(author=user)
    context = {"posts": posts, "user": user}

    return render(request, "reddit_app/profile.html", context)