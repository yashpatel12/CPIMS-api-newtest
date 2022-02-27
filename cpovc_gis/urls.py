"""Urls for GIS."""
from django.urls import path

# This should contain urls related to GIS Module ONLY
urlpatterns = [
    'cpovc_gis.views',
    path(r'^$', 'gis_home', name='gis_home'),
    path(r'^data/$', 'gis_data', name='gis_data'),
]
