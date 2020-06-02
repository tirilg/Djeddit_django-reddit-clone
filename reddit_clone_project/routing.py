from django.urls import path
from channels.routing import ProtocolTypeRouter, URLRouter, ChannelNameRouter
from channels.auth import AuthMiddlewareStack
import reddit_app.routing

application = ProtocolTypeRouter({ 
    # Websocket chat handler
    'websocket': AuthMiddlewareStack (  # Session Authentication, required to use if we want to access the user details in the consumer 
            URLRouter(
                reddit_app.routing.websocket_urlpatterns,    # Url path for connecting to the websocket to send notifications.
            )
        ),
})