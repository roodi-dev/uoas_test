from django.contrib import admin
from django.contrib.auth.hashers import make_password
from .models import Manager

@admin.register(Manager)
class ManagerAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_active', 'created_at')
    search_fields = ('username', 'email')
    list_filter = ('is_active', 'created_at')
    
    # Passwords are now stored as plain text (not recommended for production)
