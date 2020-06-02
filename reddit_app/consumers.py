from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
import json

class NotificationConsumer(WebsocketConsumer):

    def connect(self):
       self.accept()
       user = self.scope["user"]
       user_room = f"user-{user.id}"
       async_to_sync(self.channel_layer.group_add)(
           user_room, self.channel_name
       )

    def disconnect(self, close_code):
        self.close()
        async_to_sync(self.channel_layer.group_discard)(
           user_room, self.channel_name
        )

    def notify(self, event):
        self.send(
            text_data=json.dumps(
                {
                    "message":event["text"],
                    "type": event["ws_type"]
                }
            )
        )