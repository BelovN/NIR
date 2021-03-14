from .schemas import StationSchema
from .models import Station


def get_all_stations_json():
    stations = Station.objects.all()
    stations_schema = StationSchema(only=['IAGA', 'lat', 'lon']).dump(stations, many=True)
    return stations_schema

