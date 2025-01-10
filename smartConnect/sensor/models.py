import uuid
from django.db import models
from api.models import Device

class SensorData(models.Model):
    SENSOR_DATA_TYPES = [
        ('float', 'Float'),
        ('int', 'Integer'),
        ('bool', 'Boolean'),
        ('text', 'Text'),
        ('json', 'JSON'),
    ]

    device = models.ForeignKey(Device, on_delete=models.CASCADE, related_name='data')
    timestamp = models.DateTimeField()
    data_type = models.CharField(max_length=10, choices=SENSOR_DATA_TYPES)  # Type of data
    data_name = models.CharField(max_length=20, null=False, blank=False)
    data_unit = models.CharField(max_length=20, null=False, blank=False)
    
    # Fields for different types of data
    float_value = models.FloatField(null=True, blank=True)
    int_value = models.IntegerField(null=True, blank=True)
    bool_value = models.BooleanField(null=True, blank=True)
    text_value = models.TextField(null=True, blank=True)
    json_value = models.JSONField(null=True, blank=True)

    class Meta:
        indexes = [
            models.Index(fields=['device', 'timestamp']),
        ]
        ordering = ['-timestamp']

    def __str__(self):
        return f"{self.device.name} - {self.timestamp}: {self.get_value_display()}"

    def get_value(self):
        """
        Returns the value based on the data_type.
        """
        if self.data_type == 'float':
            return self.float_value
        elif self.data_type == 'int':
            return self.int_value
        elif self.data_type == 'bool':
            return self.bool_value
        elif self.data_type == 'text':
            return self.text_value
        elif self.data_type == 'json':
            return self.json_value
        return None