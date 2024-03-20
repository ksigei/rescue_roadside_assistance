from django.contrib import admin
from .models import Notification

class NotificationAdmin(admin.ModelAdmin):
    list_display = ('message', 'is_read', 'created_at')
    
admin.site.register(Notification, NotificationAdmin)
