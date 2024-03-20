from django.contrib import admin
from .models import Mechanic

class MechanicAdmin(admin.ModelAdmin):
    list_display = ('user', 'specializations', 'phone_number', 'email', 'is_available')
    list_filter = ('is_available', 'specializations')
    search_fields = ('user__username', 'phone_number', 'email', 'specializations')

admin.site.register(Mechanic, MechanicAdmin)
