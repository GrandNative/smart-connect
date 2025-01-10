from django.contrib import admin
from .models import SensorData

class SensorDataAdmin(admin.ModelAdmin):
    list_display = ('device', 'data_name', 'data_type')
    list_filter = ('device', 'timestamp')
    search_fields = ('device__name',)
    readonly_fields = ('timestamp',)

# class HumidityDataAdmin(admin.ModelAdmin):
#     list_display = ('device', 'humidity', 'timestamp')
#     list_filter = ('device', 'timestamp')
#     search_fields = ('device__name',)
#     readonly_fields = ('timestamp',)

# class StatusDataAdmin(admin.ModelAdmin):
#     list_display = ('device', 'status', 'timestamp')
#     list_filter = ('device', 'status', 'timestamp')
#     search_fields = ('device__name',)
#     readonly_fields = ('timestamp',)
    
admin.site.register(SensorData, SensorDataAdmin)
# admin.site.register(HumidityData, HumidityDataAdmin)
# admin.site.register(StatusData, StatusDataAdmin)