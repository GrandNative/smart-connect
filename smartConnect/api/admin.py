from django.contrib import admin
from .models import Template, Device, DevicePort, DeviceTemplateAssociation

class TemplateAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'owner', 'created_at', 'updated_at')
    search_fields = ('name', 'description')
    list_filter = ('owner', 'created_at')
    readonly_fields = ('created_at', 'updated_at')

class DeviceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'type', 'owner', 'location', 'status', 'created_at', 'updated_at')
    search_fields = ('name', 'type', 'location', 'status')
    list_filter = ('type', 'owner', 'status', 'created_at')
    readonly_fields = ('created_at', 'updated_at')

class DeviceTemplateAssociationAdmin(admin.ModelAdmin):
    list_display = ('device', 'template')
    search_fields = ('device__name', 'template__name')
    list_filter = ('device__type', 'template__name')


class DevicePortAdmin(admin.ModelAdmin):
    list_display = ('device', 'port_type')
    search_fields = ('device__name', 'port_type')
    list_filter = ('device__type', 'port_type')

admin.site.register(Template, TemplateAdmin)
admin.site.register(Device, DeviceAdmin)
admin.site.register(DeviceTemplateAssociation, DeviceTemplateAssociationAdmin)
admin.site.register(DevicePort, DevicePortAdmin)