from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import reddit_app.routing

application = ProtocolTypeRouter({ 
    'websocket': AuthMiddlewareStack (
            URLRouter(
                reddit_app.routing.websocket_urlpatterns,
            )
        ),
})