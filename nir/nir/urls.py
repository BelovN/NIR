from django.contrib import admin
from django.urls import path, include

from django.views.i18n import JavaScriptCatalog


urlpatterns = [
    path('admin/', admin.site.urls),
    path('jsi18n/', JavaScriptCatalog.as_view(), name='js-catalog'),
    path('distributions/', include('distributions.urls')),
    path('', include('arcgis.urls')),
]
