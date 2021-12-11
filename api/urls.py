from django.urls import path
from .views import *

app_name = 'api'

urlpatterns = [
    path('flight/', flight_search, name='flight_search'),
    path('weather/', weather_search, name='weather_search'),
    path('weather_api_marge_data/', weather_api_marge_data, name='weather_api_marge_data'),
    path('airport_search_by_free_text/<city>/', airport_search_by_free_text, name='airport_search_by_free_text'),
    path('airport_data/', airport_data, name='airport_data'),
]
