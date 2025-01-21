from django.urls import path
from .consumers import DeviceDataConsumer
import json
from channels.generic.websocket import AsyncWebsocketConsumer

websocket_urlpatterns = [
    path("ws/device/<uuid:device_id>/", DeviceDataConsumer.as_asgi()),
]

# class TestConsumer(AsyncWebsocketConsumer):
#     async def connect(self):
#         await self.accept()
#         await self.send(json.dumps({"message": "WebSocket connected successfully!"}))

# websocket_urlpatterns = [
#     path("ws/test/", TestConsumer.as_asgi()),
# ]
# 