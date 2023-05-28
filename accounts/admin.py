from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    fieldsets = [
        ('User', {
            'fields': ('username', 'password')
        }),
        ('Personal info', {
            'fields': ('first_name', 'last_name', 'email')
        }),
        ('Statistic', {
            'fields': ('experience', 'score')
        }),
        ('Permissions', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')
        }),
        ('Important dates', {
            'fields': ('last_login', 'date_joined')
        }),
    ]
    list_display = ['id', 'username', 'first_name', 'last_name', 'email', 'experience', 'is_active', 'is_staff']
    list_display_links = ['id', 'username', 'first_name', 'last_name', 'experience', 'is_active', 'is_staff']
    list_filter = ['experience', 'is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions']
    list_per_page = 25
    search_fields = ['username', 'first_name', 'last_name', 'email']
