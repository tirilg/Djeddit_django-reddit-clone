from django.shortcuts import render, get_object_or_404, redirect
from . models import Post, Comment

# Create your views here.

def index(request):
    if request.method == "POST":
        title = request.POST["title"]
        text = request.POST["text"]
        post = Post()

        post.title = title
        post.text = text
        post.author = request.user

        post.save()

    posts = Post.objects.all()
    context = {"posts": posts}
    
    return render(request, "reddit_app/index.html", context)

def profile(request):
    user = request.user
    posts = Post.objects.filter(author=user)
    context = {"posts": posts, "user": user}

    return render(request, "reddit_app/profile.html", context)

def single_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comment = Comment()
    comments = Comment.objects.filter(post=post)
    context = {"post": post, "comments": comments}
    return render(request, "reddit_app/single_post.html", context)

def comment(request, post_id):
    if request.method == "POST":
        text = request.POST["text"]
        author = request.user

        Comment.objects.create(text=text, author=author, post_id=post_id)
        return redirect("reddit_app:single_post", post_id=post_id)

def update_post(request):
    pass

def delete_post(request):
    pass
