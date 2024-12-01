from django.contrib import admin
from .models import Threat


@admin.register(Threat)
class ThreatAdmin(admin.ModelAdmin):
    list_display = ('name', 'severity', 'timestamp')  # Columns to display
    list_filter = ('severity',)  # Filter options in the admin panel
    search_fields = ('name', 'description')  # Search box for these fields
    ordering = ('-timestamp',)  # Default ordering (newest first)
