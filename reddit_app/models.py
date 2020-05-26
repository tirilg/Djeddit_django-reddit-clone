""" import django_rq """
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    votes = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Author: {self.author} // Title: {self.title}"


    def date_posted(self):
        return self.created_at.strftime('%B %d %Y')

class Comment(models.Model):
    text = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"User: {self.author} // Commented: {self.text} // On post: {self.post}"
    
    def date_commented(self):
        return self.created_at.strftime('%B %d %Y')

class Vote(models.Model):
    vote = models.BooleanField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.vote} - {self.user} - {self.post}"

class Notification(models.Model):
    reciever = models.ForeignKey(User, related_name='notifications', on_delete=models.CASCADE)
    sender = models.ForeignKey(User, related_name='sent_notifications', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Sender: {self.sender} // Reciever: {self.reciever} // On post: {self.post}"
    

    def date_sent(self):
        return self.created_at.strftime('%B %d %Y')

    