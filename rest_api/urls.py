from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from rest_api import views


urlpatterns = [
    path('weather/', views.WeatherList.as_view(),name='weather-list'),
    path('weather/<int:pk>/', views.WeatherDetail.as_view(),name='weather-highlight'),
]

urlpatterns = format_suffix_patterns(urlpatterns)