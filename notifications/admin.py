from django.contrib import admin
from .models import UserNotification

@admin.register(UserNotification)
class UserNotificationAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message')
