from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TemplateModelViewSet, DeviceViewSet, DeviceTemplateAssociationViewSet, DevicePortViewSet
from .views import RegisterView

router = DefaultRouter()
router.register(r'templates', TemplateModelViewSet)
router.register(r'devices', DeviceViewSet)
router.register(r'associations', DeviceTemplateAssociationViewSet)
router.register(r'ports', DevicePortViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegisterView.as_view(), name='register'),
]