from channels.generic.websocket import WebsocketConsumer
import json
from asgiref.sync import async_to_sync

class NotificationConsumer(WebsocketConsumer):
    
    # Function to connect to the websocket
    def connect(self):
       self.accept()
       user = self.scope["user"]
       user_room = f"user-{user.id}"
       async_to_sync(self.channel_layer.group_add)(
           user_room, self.channel_name
       )

    # Function to disconnet the Socket
    def disconnect(self, close_code):
        self.close()
        async_to_sync(self.channel_layer.group_discard)(
           user_room, self.channel_name
        )
        # pass

    def receive(self, text_data=None, bytes_data=None):
        self.send(text_data="Hi tirial how u doin?")

    # Custom Notify Function which can be called from Views or api to send message to the frontend
    def notify(self, event):
        self.send(
            text_data=json.dumps(
                {
                    "message":event["text"],
                    "type": event["ws_type"]
                }
            )
        )