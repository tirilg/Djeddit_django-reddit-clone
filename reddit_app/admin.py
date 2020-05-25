from django.contrib import admin
from .models import Post, Comment, Vote, Notification

# Register your models here.
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Vote)
admin.site.register(Notification)
