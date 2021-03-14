from django.http.response import JsonResponse

from .services import get_all_stations_json


def stations_json(request):
    return JsonResponse(get_all_stations_json(), safe=False)
