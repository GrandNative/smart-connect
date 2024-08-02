from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TemplateModelViewSet, DeviceViewSet, DeviceTemplateAssociationViewSet, DevicePortViewSet

router = DefaultRouter()
router.register(r'templates', TemplateModelViewSet)
router.register(r'devices', DeviceViewSet)
router.register(r'associations', DeviceTemplateAssociationViewSet)
router.register(r'ports', DevicePortViewSet)


urlpatterns = [
    path('', include(router.urls)),
]