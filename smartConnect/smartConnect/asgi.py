import os
from django.core.asgi import get_asgi_application
from channels.security.websocket import AllowedHostsOriginValidator

# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "smartConnect.settings")
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'smartConnect.settings')
django_asgi_app = get_asgi_application()

from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from .middleware import JWTAuthMiddleware
from sensor.routing import websocket_urlpatterns

application = ProtocolTypeRouter({
    "http": django_asgi_app,
    "websocket": AllowedHostsOriginValidator(
        AuthMiddlewareStack(
            URLRouter(websocket_urlpatterns)
        )
    ),
})