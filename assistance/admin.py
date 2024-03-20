from django.contrib import admin
from .models import AssistanceRequest

class AssistanceRequestAdmin(admin.ModelAdmin):
    list_display = ('user', 'mechanic', 'location', 'is_confirmed')
    list_filter = ('is_confirmed',)
    search_fields = ('user__username', 'mechanic__name', 'description')

from django.contrib import admin
from .models import AssistanceResponse

class AssistanceResponseAdmin(admin.ModelAdmin):
    list_display = ('request', 'mechanic', 'response_text', 'is_completed')
    list_filter = ('is_completed',)
    search_fields = ('request__user__username', 'mechanic__name', 'response_text')

admin.site.register(AssistanceRequest, AssistanceRequestAdmin)
admin.site.register(AssistanceResponse, AssistanceResponseAdmin)

