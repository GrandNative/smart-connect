from django.contrib import admin
from .models import Template, Device, DeviceTemplateAssociation

class TemplateAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'owner', 'created_at', 'updated_at')
    search_fields = ('name', 'description')
    list_filter = ('owner', 'created_at')
    readonly_fields = ('created_at', 'updated_at')

class DeviceAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'device_key')
    search_fields = ('name', 'device_key')
    readonly_fields = ('device_key',)

class DeviceTemplateAssociationAdmin(admin.ModelAdmin):
    list_display = ('device', 'template')
    search_fields = ('device__name', 'template__name')
    list_filter = ('device__name', 'template__name')

admin.site.register(Template, TemplateAdmin)
admin.site.register(Device, DeviceAdmin)
admin.site.register(DeviceTemplateAssociation, DeviceTemplateAssociationAdmin)


# class DevicePortAdmin(admin.ModelAdmin):
#     list_display = ('device', 'port_type')
#     search_fields = ('device__name', 'port_type')
#     list_filter = ('device__name', 'port_type')

# admin.site.register(DevicePort, DevicePortAdmin)