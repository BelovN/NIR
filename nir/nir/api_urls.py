from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('arcgis/', include('arcgis.api_urls')),
]
