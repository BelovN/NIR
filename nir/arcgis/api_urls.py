from django.urls import path

from .api_view import stations_json


urlpatterns = [
    path('stations/', stations_json, name='stations-json'),

]
