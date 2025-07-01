from django.contrib import admin
from .models import PlateLog

@admin.register(PlateLog)
class PlateLogAdmin(admin.ModelAdmin):
    list_display = ('plate_number', 'country', 'confidence', 'timestamp')
    search_fields = ('plate_number', 'country')
