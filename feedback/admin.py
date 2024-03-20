from django.contrib import admin
from .models import Feedback

class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('user', 'mechanic', 'rating', 'comment', 'created_at')
    readonly_fields = ('created_at',)

admin.site.register(Feedback, FeedbackAdmin)
