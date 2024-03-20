from django.contrib import admin
from .models import Motorist

class MotoristAdmin(admin.ModelAdmin):
    list_display = ('user', 'location', 'phone_number')

admin.site.register(Motorist, MotoristAdmin)
