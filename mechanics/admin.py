from django.contrib import admin
from .models import Mechanic

class MechanicAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone_number', 'email', 'is_available')
    list_filter = ('is_available',)
    search_fields = ('user__username', 'phone_number', 'email')

admin.site.register(Mechanic, MechanicAdmin)
