from rest_framework import serializers
from .models import Template, Device, DeviceTemplateAssociation, DevicePort

class TemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Template
        fields = '__all__'

class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = '__all__'


class DevicePortSerializer(serializers.ModelSerializer):
    class Meta:
        model = DevicePort
        fields = '__all__'


class DeviceTemplateAssociationSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceTemplateAssociation
        fields = '__all__'
