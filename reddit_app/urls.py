from django.urls import path, include
from . import views
from .api import PostView, VoteView, PostDetail

app_name = 'reddit_app'

urlpatterns = [
    path("", views.index, name="index"), 
    path("profile/", views.profile, name="profile"), 
    path("post/<int:post_id>", views.single_post, name="single_post"), 
    path("post/<int:post_id>/comment", views.comment, name="comment"), 
    path("post/<int:post_id>/delete", views.delete_post, name="delete_post"), 
    path("post/<int:post_id>/upvote", views.upvote, name="upvote"), 
    path("post/<int:post_id>/downvote", views.downvote, name="downvote"), 
    path('posts/', PostView.as_view()),
    path('posts/<int:pk>', PostDetail.as_view()),
    path('votes/', VoteView.as_view()),
    path('rest-auth/', include('rest_auth.urls')),
]