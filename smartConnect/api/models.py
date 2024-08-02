from django.db import models
from django.contrib.auth.models import User

class Template(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Device(models.Model):
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class DeviceTemplateAssociation(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    template = models.ForeignKey(Template, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('device', 'template')
    
    def __str__(self):
        return f"{self.device.name} - {self.template.name}"


class DevicePort(models.Model):
    PORT_TYPE_CHOICES = [
        ('char', 'Character'),
        ('int', 'Integer'),
        ('float', 'Float'),
        # ...
    ]
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    port_type = models.CharField(choices=PORT_TYPE_CHOICES, max_length=125)