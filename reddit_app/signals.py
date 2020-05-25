from django.db.models.signals import post_save
from django.dispatch import receiver, Signal
from .models import Comment
from . models import Notification

@receiver(post_save, sender=Comment, dispatch_uid="create_notification")
def create_notification(sender, instance, created, **kwargs):
    print("**** signal recieved")
    print("sender", sender)
    print("kwargs", kwargs)
    print("comment author", instance.author.id)
    print("comment", instance.text)
    print("post author", instance.post.author.id)
    print("post", instance.post.id)
    print("created", created)

    if created:
        notification = Notification()
        notification.reciever_id = instance.post.author.id
        notification.post_id = instance.post.id
        notification.sender_id = instance.author.id
        notification.save()
