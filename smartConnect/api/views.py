from rest_framework import viewsets, permissions, serializers
from .models import Template, Device, DeviceTemplateAssociation, DevicePort
from .serializers import TemplateSerializer, DeviceSerializer, DeviceTemplateAssociationSerializer, DevicePortSerializer

class IsOwnerOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_staff:
            return True
        return obj.owner == request.user

# views.py

from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .serializers import RegisterSerializer

class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        return Response({
            "user": {
                "username": user.username,
                "email": user.email,
            },
            "message": "User created successfully"
        }, status=status.HTTP_201_CREATED)


class TemplateModelViewSet(viewsets.ModelViewSet):
    queryset = Template.objects.all()
    serializer_class = TemplateSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrAdmin]

    def get_queryset(self):
        if self.request.user.is_staff:
            return Template.objects.all()
        return Template.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class DeviceViewSet(viewsets.ModelViewSet):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrAdmin]

    def get_queryset(self):
        if self.request.user.is_staff:
            return Device.objects.all()
        return Device.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class DeviceTemplateAssociationViewSet(viewsets.ModelViewSet):
    queryset = DeviceTemplateAssociation.objects.all()
    serializer_class = DeviceTemplateAssociationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_staff:
            return DeviceTemplateAssociation.objects.all()
        return DeviceTemplateAssociation.objects.filter(device__owner=self.request.user, template__owner=self.request.user)

    def perform_create(self, serializer):
        device = serializer.validated_data['device']
        template = serializer.validated_data['template']
        if device.owner != self.request.user or template.owner != self.request.user:
            raise serializers.ValidationError("Device and Template must belong to the current user")
        serializer.save()


class DevicePortViewSet(viewsets.ModelViewSet):
    queryset = DevicePort.objects.all()
    serializer_class = DevicePortSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_staff:
            return DevicePort.objects.all()
        return DevicePort.objects.filter(device__owner=self.request.user)

    def perform_create(self, serializer):
        device = serializer.validated_data['device']
        if device.owner != self.request.user:
            raise serializers.ValidationError("Device must belong to the current user")
        serializer.save()