from django.apps import AppConfig


class RedditAppConfig(AppConfig):
    name = 'reddit_app'

    def ready(self):
        from .signals import create_notification