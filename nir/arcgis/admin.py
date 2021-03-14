from django.contrib import admin
from .models import Station


class StationAdmin(admin.ModelAdmin):
    list_display = ['name', 'IAGA', 'lat', 'lon', 'mlat', 'mlon']


admin.site.register(Station, StationAdmin)
