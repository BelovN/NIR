import os
import pandas as pd

from django.http.response import HttpResponse, Http404
from django.shortcuts import render
from django.conf import settings


def get_json_stations(request):
    df = pd.read_csv(
        os.path.join(settings.BASE_DIR, 'data/stations.csv'),
        error_bad_lines=False
    )
    stations_json = df.to_json(orient="records")
    return HttpResponse(stations_json, content_type='application/json')


def main_view(request):
    return render(request, 'arcgis/main.html')
