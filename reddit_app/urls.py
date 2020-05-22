from django.urls import path
from . import views

app_name = 'reddit_app'

urlpatterns = [
    path("", views.index, name="index"), 
    path("profile/", views.profile, name="profile"), 
    path("post/<int:post_id>", views.single_post, name="single_post"), 
    path("post/<int:post_id>/comment", views.comment, name="comment"), 
    path("post/<int:post_id>/upvote", views.upvote, name="upvote"), 
]