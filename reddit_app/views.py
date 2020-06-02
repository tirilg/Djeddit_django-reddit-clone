from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect, reverse
from django.contrib.auth.decorators import login_required
from . models import Post, Comment, Vote, Notification

def index(request):
    posts = Post.objects.all().order_by('-created_at')
    context = {"posts": posts}
    
    return render(request, "reddit_app/index.html", context)


def trending(request):
    posts = Post.objects.all().order_by('-votes')
    context = {"posts": posts}

    return render(request, "reddit_app/trending.html", context)


def single_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comment = Comment()
    comments = Comment.objects.filter(post=post)
    context = {"post": post, "comments": comments}
    return render(request, "reddit_app/single_post.html", context)


def profile(request):
    user = request.user
    posts = Post.objects.filter(author=user)
    context = {"posts": posts, "user": user}

    return render(request, "reddit_app/profile.html", context)


@login_required
def comment(request, post_id):
    if request.method == "POST":
        text = request.POST["text"]
        author = request.user
        Comment.objects.create(text=text, author=author, post_id=post_id)
        
        return redirect("reddit_app:single_post", post_id=post_id)


@login_required
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    post.delete()
    
    return HttpResponseRedirect(reverse('reddit_app:profile'))


def notifications(request):
    user = request.user
    notifications = Notification.objects.filter(reciever=user, read=False)
    read_notifications = Notification.objects.filter(reciever=user, read=True)

    if request.method == "POST":
        notifications.update(read=True)
 
    context = {"notifications": notifications, "read_notifications": read_notifications}
    
    return render(request, "reddit_app/notifications.html", context)



