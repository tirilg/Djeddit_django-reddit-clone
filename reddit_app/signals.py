from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Comment, Notification

@receiver(post_save, sender=Comment, dispatch_uid="create_notification")
def create_notification(sender, instance, created, **kwargs):
    print("**** signal recieved")
    if created:
        if not instance.post.author.id == instance.author.id:
            notification = Notification()
            notification.reciever_id = instance.post.author.id
            notification.post_id = instance.post.id
            notification.sender_id = instance.author.id
            notification.save()
