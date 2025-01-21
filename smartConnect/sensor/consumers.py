from channels.generic.websocket import AsyncWebsocketConsumer
from django.contrib.auth.models import AnonymousUser
from django.core.exceptions import PermissionDenied
from asgiref.sync import sync_to_async
import json
from .models import Device  # Replace with your Device model

class DeviceDataConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Get the device ID from the URL route
        self.device_id = self.scope['url_route']['kwargs']['device_id']
        self.group_name = f"device_{self.device_id}"

        # Check if the user is authenticated
        # if isinstance(self.scope["user"], AnonymousUser):
        #     await self.close()
        #     raise PermissionDenied("Unauthorized")

        # Check if the user is authorized to access the device
        try:
            device = await sync_to_async(Device.objects.get)(device_key=self.device_id)
            # if device.owner != self.scope["user"]:
            #     await self.close()
            #     raise PermissionDenied("Forbidden")
        except Device.DoesNotExist:
            await self.close()
            raise PermissionDenied("Device not found")

        # Add the WebSocket connection to the group
        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        # Remove the WebSocket connection from the group
        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        # Handle client messages (optional)
        pass

    async def send_device_data(self, event):
        # Send device data to the WebSocket client
        data = event["data"]
        await self.send(text_data=json.dumps(data))
