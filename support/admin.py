from django.contrib import admin
from .models import SupportTicket

class SupportTicketAdmin(admin.ModelAdmin):
    list_display = ('user', 'issue_description', 'status', 'created_at')

admin.site.register(SupportTicket, SupportTicketAdmin)
