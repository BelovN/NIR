from django.urls import path
from .views import main_view, get_json_stations


urlpatterns = [
    path('', main_view, name='arcgis_main'),
    path('stations-json/', get_json_stations, name='stations-json'),
]
