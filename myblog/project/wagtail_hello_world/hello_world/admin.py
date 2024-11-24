from django.contrib import admin
from .models import ToDoItem

@admin.register(ToDoItem)
class ToDoItemAdmin(admin.ModelAdmin):
    """Admin configuration for ToDoItem."""
    list_display = ('title', 'is_completed', 'created_at', 'updated_at')
    list_filter = ('is_completed', 'created_at')
    search_fields = ('title', 'description')
    ordering = ('-created_at',)
